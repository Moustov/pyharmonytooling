import html
import os
import urllib

from pychord import Chord

from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.song.song import Song


def turn_html_accents(tab: str) -> str:
    """
    change all coded accent character into extended ASCII
    :param tab:
    :return:
    """
    tab = tab.replace("&egrave;", "è")
    tab = tab.replace("&eacute;", "é")
    tab = tab.replace("&Agrave;", "À")
    tab = tab.replace('Ã‰', "É")
    return tab


class UltimateGuitarSong(Song):
    def __init__(self):
        super().__init__()
        self.tabs = []
        self.artist = ""
        self.song_title = ""
        self.page_title = ""
        self.html = ""
        self.url = ""
        self.cof = CircleOf5th()
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []

    def digest(self, html: str):
        """
        digest song informations & tabs from a UG html page content
        :param html: a UG html page content
        """
        self.html = html
        try:
            self.extract_tabs_with_tab(html)
            if not self.chords_sequence:  # to handle weird formats such as https://tabs.ultimate-guitar.com/tab/trans-siberian-orchestra/christmas-canon-rock-tabs-3465077
                self.extract_tabs_with_chless_tabs(html)
        except:
            try:
                self.extract_tabs_without_tab(html)
            except:
                print("Could not extract the song - format unknown")
        self.page_title = turn_html_accents(self.extract_page_title(html))
        self.song_title = self.page_title.split("CHORDS")[0].strip()
        artist_and_site = self.page_title.split("by")[1]
        self.artist = artist_and_site.split("@")[0].strip()

    def __str__(self):
        """
        returns a string synthesis of a song
        :return:
        """
        res = super().__str__()
        res += f"URL: {self.url}\n"
        res += "\n".join(self.tabs)
        return res

    @staticmethod
    def to_path_name(s: str) -> str:
        res = s.replace("|", "")
        res = res.replace("/", "")
        res = res.replace(":", "")
        res = res.replace("#", "")
        res = res.replace("&039;", "'")
        return html.unescape(res)

    def store_song(self, path):
        """
        write the song on the HDD @ f"{path}/{self.artist}/{self.song_title}.html"
        :param path: path to the storage folder - "/" at the end
        :return:
        """
        title = UltimateGuitarSong.to_path_name(self.song_title)
        artist = UltimateGuitarSong.to_path_name(self.artist)
        song_title = UltimateGuitarSong.to_path_name(self.song_title)
        final_path = f"{path}/{artist}/{title}"
        if not os.path.isdir(final_path):
            os.makedirs(final_path)

        with open(f"{final_path}/{song_title}.html", "w", encoding="utf-8") as html_file:
            html_file.write(self.html)

    def extract_tabs_without_tab(self, html: str):
        """
        extracts song data from a UG html page is not formatted with [tab] markups
        :param html:
        :return:
        """
        self.tabs = []
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        tabs_with_extra = html.split("{&quot;content&quot;:&quot;")[1:]
        song = tabs_with_extra[len(tabs_with_extra) - 1].split("&quot;,&quot;revision_id&quot;:")[0]
        lines = song.split(r"\r\n")
        for line in lines:
            line = turn_html_accents(line)
            chords_b = line.split("[ch]")
            if len(chords_b) > 1:
                for c in chords_b:
                    c = c.strip()
                    if c != '':
                        chords = c.split("[/ch]")
                        for chord_name in chords:
                            try:
                                chord_name = chord_name.strip()
                                if chord_name != '' and "N.C." not in chord_name:
                                    if chord_name[0] == '/':
                                        chord_name = chord_name[1:]
                                    if CofChord.is_like_a_chord(chord_name):
                                        a_chord = Chord(chord_name)
                                        self.chords_sequence.append(a_chord)
                            except Exception as err:
                                print(chord_name, err)
                                print(f">>> '{chord_name}' could not be set as a chord")
                                self.chords_sequence.append(chord_name)
            elif line.strip() != '':
                self.lyrics.append(line)
        pass

    def extract_tabs_with_tab(self, html: str):
        """
        extracts song data from a UG html page is formatted with [tab] markups
        :param html:
        :return:
        """
        self.tabs = []
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        tabs_with_extra = html.split("[tab]")[1:]
        for tab in tabs_with_extra:
            tab = "[tab]" + tab
            tab = turn_html_accents(tab)
            s = tab.split(r"\r\n")
            self.line_of_chords.append(s[0])
            loc = s[0].split()
            for c in loc[1:]:
                if "[ch]" in c and "[/ch]" in c and "N.C." not in c:
                    chord_name = c.split("[/ch]")[0]  # filtering [ch] & [/ch]
                    chord_name = chord_name.split("[ch]")[1]
                    try:
                        if CofChord.is_like_a_chord(chord_name):
                            a_chord = Chord(chord_name)
                            self.chords_sequence.append(a_chord)
                    except:
                        print(f">>> '{chord_name}' could not be set as a chord")
            self.lyrics.append(s[1])
            self.tabs.append(tab)
        self.tabs[len(self.tabs) - 1] = self.tabs[len(self.tabs) - 1].split("&quot;,&quot;revision_id&quot;:")[0]

    def extract_page_title(self, html: str) -> str:
        """
        return the html page title
        :param html:
        :return:
        """
        part = html.split("<title>")
        title = part[1].split("</title>")[0]
        return title

    def extract_song_from_url(self, url: str):
        """
        retrieve the song from the URL and digest it into self
        :param url:
        """
        print(f"Trying to retrieve {url}...")
        self.url = url
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
            }
        )
        f = urllib.request.urlopen(req)
        self.html = f.read().decode('utf-8')
        self.digest(self.html)
        self.url = url

    def extract_tabs_with_chless_tabs(self, html):
        """
        to handle weird formats such as https://tabs.ultimate-guitar.com/tab/trans-siberian-orchestra/christmas-canon-rock-tabs-3465077
        :param html:
        :return:
        """
        self.tabs = []
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        tabs_with_extra = html.split("[tab]")[1:]
        for tab in tabs_with_extra:
            tab = "[tab]" + tab
            tab = turn_html_accents(tab)
            s = tab.split(r"\r\n")
            for l in s:
                tab_less = l.split("[/tab]")
                self.line_of_chords.append(tab_less[0])
                loc = tab_less[0].split()
                a_chord = None
                tab_line = []
                for c in loc[1:]:
                    chord_name = c.strip()
                    if CofChord.is_like_a_chord(chord_name):
                        try:
                            a_chord = Chord(chord_name)
                            tab_line.append(a_chord)
                            self.chords_sequence.append(a_chord)
                        except:
                            print(f">>> '{chord_name}' could not be set as a chord")
                            self.lyrics.append(s)
                if not a_chord:
                    self.lyrics.append(s)
                else:
                    self.tabs.append(tab_line)
