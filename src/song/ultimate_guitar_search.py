from google.modules.utils import _get_search_url as google_search, get_html


class UltimateGuitarSearch:
    def __init__(self):
        self.html_parts = []

    def extract_link(self, part: str) -> str:
        res = part.split("&amp")
        return "https://tabs.ultimate-guitar.com/tab/" + res[0]

    def search(self, query: str, limit: int) -> [str]:
        """
        search from UG any string, not only the author / title
        :param query:
        :param limit:
        :return:
        """
        res = []
        link_qty = 0
        page = 0
        while link_qty < limit:
            url = google_search(query, page, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
            html = str(get_html(url))
            self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
            for part in self.html_parts[1:]:
                res.append(self.extract_link(part))
                link_qty += 1
                if link_qty >= limit:
                    break
            page += 1
        return res
