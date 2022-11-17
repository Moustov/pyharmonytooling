import urllib


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
        self.extract_tabs(html)
        self.page_title = self.extract_page_title(html)
        self.song_title = self.page_title.split("CHORDS")[0].strip()
        artist_and_site = self.page_title.split("by")[1]
        self.artist = artist_and_site.split("@")[0].strip()

    def get_string(self) -> str:
        res = f"Title: {self.song_title}\n"
        res += f"Artist: {self.artist}\n"
        res += f"URL: {self.url}\n"
        res += "\n".join(self.tabs)
        return res

    def extract_tabs(self, html: str):
        self.tabs = []
        tabs_with_extra = html.split("[tab]")[1:]
        for tab in tabs_with_extra:
            tab = "[tab]" + tab
            tab = tab.replace("&eacute;", "é")
            tab = tab.replace("&Agrave;", "À")
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



