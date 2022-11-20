from random import randint
from time import time

from google.modules.utils import _get_search_url as google_search, get_html

from src.harmony.circle_of_5th import CircleOf5th
from src.harmony.degree import Degree
from src.harmony.note import Note
from src.song.ultimate_guitar_song import UltimateGuitarSong


class UltimateGuitarSearch:
    NUMBER_OF_ACCEPTABLE_NEGATIVE_CHECKS = 100

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

    def search(self, query: str, limit: int, matches_exactly=False, try_avoiding_blocked_searches=True) -> [str]:
        """
        search from UG any string, not only the author / title
        WARNING: too many searches will result in a blocking HTTP ERROR 429
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
        :param try_avoiding_blocked_searches: wait a bit to avoid being blocked by google
        :param matches_exactly: check on UG if the query matches some part of the songs found
        :param query:
        :param limit:
        :return:
        """
        query += " site:ultimate-guitar.com"
        res = []
        link_qty = 0
        page = 0
        more_songs = True
        numbers_of_negative_checks = 0
        while link_qty < limit and more_songs \
                and numbers_of_negative_checks < self.NUMBER_OF_ACCEPTABLE_NEGATIVE_CHECKS:
            url = google_search(query, page, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
            # html = str(self.get_html_content(url))
            html = str(get_html(url))
            if html:
                raise Exception("No more query is accepted for a while - try again later...")
            self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
            more_songs = len(self.html_parts) > 1
            for part in self.html_parts[1:]:
                link = self.__extract_link(part)
                match_found = False
                if matches_exactly:
                    match_found = self.check_matches_exactly(query, link)
                if match_found or not matches_exactly:
                    print(f"Song found at {link}")
                    res.append(link)
                    link_qty += 1
                    if link_qty >= limit:
                        break
                else:
                    numbers_of_negative_checks += 1
            page += 1
            if try_avoiding_blocked_searches:
                # wait a bit to avoid being blocked by google
                # see https://github.com/abenassi/Google-Search-API/issues/91
                time.sleep(randint(180, 240))
        if numbers_of_negative_checks >= self.NUMBER_OF_ACCEPTABLE_NEGATIVE_CHECKS:
            print(f"{len(res)} found - No other song found with "
                  f"{self.NUMBER_OF_ACCEPTABLE_NEGATIVE_CHECKS} attempts...")
        return res

    def search_songs_from_cadence(self, cadence: str, mode: CircleOf5th, limit_per_tone: int,
                                  matches_exactly: bool = False, try_avoiding_blocked_searches=True) -> dict:
        """
        return a list of songs that match the cadence
        :param try_avoiding_blocked_searches:
        :param matches_exactly:
        :param limit_per_tone:
        :param mode: major/minor...
        :param cadence: eg. "ii7–V7–Imaj"
        :return: dict keys = the tones
        """
        songs = {}
        degrees = cadence.split("-")
        for root_note in Note.chromatic_scale:
            search_string = ""
            for degree in degrees:
                chord = Degree.get_chord_from_degree(degree, root_note, mode)
                search_string += chord + " "
            print(search_string)
            songs[search_string] = self.search(search_string, limit_per_tone, matches_exactly,
                                               try_avoiding_blocked_searches)
        return songs

    def check_matches_exactly(self, query: str, link: str) -> bool:
        ugs = UltimateGuitarSong()
        ugs.extract_song_from_url(link)
        cs = ""
        for chord in ugs.chords_sequence:
            cs += f"{chord} "
        cs.replace("[tab]", "")
        res = query[0:len(query) - len(" site:ultimate-guitar.com")] in cs
        return res
