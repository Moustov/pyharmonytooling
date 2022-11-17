from google.modules.utils import _get_search_url, get_html


class UltimateGuitarSearch:
    def __init__(self):
        self.html_parts = []

    def extract_link(self, part: str) -> str:
        res = part.split("&amp")
        return "https://tabs.ultimate-guitar.com/tab/" + res[0]

    def search(self, query: str) -> [str]:
        query = "D Dm A site:ultimate-guitar.com"
        url = _get_search_url(query, 0, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
        html = str(get_html(url))
        self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
        res = []
        for part in self.html_parts[1:]:
            res.append(self.extract_link(part))
        return res