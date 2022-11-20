from google.modules.utils import _get_search_url as google_search, get_html

from src.harmony.circle_of_5th import CircleOf5th
from src.harmony.degree import Degree


class UltimateGuitarSearch:
    def __init__(self):
        self.html_parts = []

    def __extract_link(self, part: str) -> str:
        """
        retrieve the link from a search()
        :param part:
        :return:
        """
        res = part.split("&amp")
        return "https://tabs.ultimate-guitar.com/tab/" + res[0]

    def search(self, query: str, limit: int) -> [str]:
        """
        search from UG any string, not only the author / title
        WARNING: too many searches will result in a blocking HTTP ERROR 429
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
        :param query:
        :param limit:
        :return:
        """
        query += " site:ultimate-guitar.com"
        res = []
        link_qty = 0
        page = 0
        more_songs = True
        while link_qty < limit and more_songs:
            url = google_search(query, page, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
            # html = str(self.get_html_content(url))
            html = str(get_html(url))
            self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
            more_songs = len(self.html_parts) > 1
            for part in self.html_parts[1:]:
                res.append(self.__extract_link(part))
                link_qty += 1
                if link_qty >= limit:
                    break
            page += 1
        return res

    def search_songs_from_cadence(self, cadence: str, mode: CircleOf5th, limit_per_tone: int) -> dict:
        """
        return a list of songs that match the cadence
        :param limit_per_tone:
        :param mode: major/minor...
        :param cadence: eg. "ii7–V7–Imaj"
        :return: dict keys = the tones
        """
        songs = {}
        degrees = cadence.split("-")
        for root_note in CircleOf5th.chromatic_scale:
            search_string = ""
            for degree in degrees:
                chord = Degree.get_chord_from_degree(degree, root_note, mode)
                search_string += chord + " "
            print(search_string)
            songs[search_string] = self.search(search_string, limit_per_tone)
        return songs



