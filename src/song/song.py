import urllib

from pychord import Chord


class UltimateGuitarSong:
    def __init__(self):
        self.tabs = []
        self.artist = ""
        self.song_title = ""
        self.page_title = ""
        self.html = ""
        self.url = ""

    def digest_html(self, html):
        self.html = html
        try:
            self.extract_tabs_with_tab(html)
        except:
            try:
                self.extract_tabs_without_tab(html)
            except:
                print("Could not extract the song - format unknown")
        self.page_title = self.turn_html_accents(self.extract_page_title(html))
        self.song_title = self.page_title.split("CHORDS")[0].strip()
        artist_and_site = self.page_title.split("by")[1]
        self.artist = artist_and_site.split("@")[0].strip()

    def get_string(self) -> str:
        res = f"Title: {self.song_title}\n"
        res += f"Artist: {self.artist}\n"
        res += f"URL: {self.url}\n"
        res += "\n".join(self.tabs)
        return res

    def extract_tabs_without_tab(self, html: str):
        self.tabs = []
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        tabs_with_extra = html.split("{&quot;content&quot;:&quot;")[1:]
        song = tabs_with_extra[len(tabs_with_extra) - 1].split("&quot;,&quot;revision_id&quot;:")[0]
        lines = song.split(r"\r\n")
        for line in lines:
            line = self.turn_html_accents(line)
            chords_b = line.split("[ch]")
            if len(chords_b) > 1:
                for c in chords_b:
                    c = c.strip()
                    if c != '':
                        chords = c.split("[/ch]")
                        for chord_name in chords:
                            try:
                                chord_name = chord_name.strip()
                                if chord_name != '':
                                    if chord_name[0] == '/':
                                        chord_name = chord_name[1:]
                                    a_chord = Chord(chord_name)
                                    self.chords_sequence.append(a_chord)
                            except Exception as err:
                                print(chord_name, err)
                                self.chords_sequence.append(chord_name)
            elif line.strip() != '':
                self.lyrics.append(line)
        pass
        # self.tabs[len(self.tabs) - 1] = self.tabs[len(self.tabs) - 1].split("&quot;,&quot;revision_id&quot;:")[0]

    def extract_tabs_with_tab(self, html: str):
        self.tabs = []
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        tabs_with_extra = html.split("[tab]")[1:]
        for tab in tabs_with_extra:
            tab = "[tab]" + tab
            tab = self.turn_html_accents(tab)
            s = tab.split(r"\\r\\n")
            self.line_of_chords.append(s[0])
            loc = s[0].split()
            for c in loc[1:]:
                if "[ch]" in c and "[/ch]" in c:
                    chord_name = c[4:-5]    #filtering [ch] & [/ch]
                    a_chord = Chord(chord_name)
                    self.chords_sequence.append(a_chord)
            self.lyrics.append(s[1])
            self.tabs.append(tab)
        self.tabs[len(self.tabs) - 1] = self.tabs[len(self.tabs) - 1].split("&quot;,&quot;revision_id&quot;:")[0]

    def extract_page_title(self, html: str) -> str:
        part = html.split("<title>")
        title = part[1].split("</title>")[0]
        return title

    def extract_song_from_url(self, url: str):
        """
        retrieve the song from the URL and digest it into self
        :param url:
        """
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
        self.digest_html(self.html)
        self.url = url

    def turn_html_accents(self, tab: str) -> str:
        tab = tab.replace("&egrave;", "è")
        tab = tab.replace("&eacute;", "é")
        tab = tab.replace("&Agrave;", "À")
        tab = tab.replace('Ã‰', "É")
        return tab




