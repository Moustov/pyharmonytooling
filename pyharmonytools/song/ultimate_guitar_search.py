import os.path
import datetime
from datetime import date
from datetime import datetime
import platform
from random import randint
from time import time, sleep

from google.modules.utils import _get_search_url as google_search, get_html

from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.degree import Degree
from pyharmonytools.harmony.note import Note
from pyharmonytools.song.ultimate_guitar_song import UltimateGuitarSong


class UltimateGuitarSearch:
    GOOGLE_SEARCH_SECURE_WAIT = 6   # minutes
    GOOGLE_SEARCH_WAIT_AFTER_REJECTION = 5  # minutes
    NUMBER_OF_ACCEPTABLE_NEGATIVE_CHECKS = 75
    NB_GOOGLE_SEARCHES_LOG_FILE_NAME = ".google_searches_qty.log"

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

    def search(self, query: str, limit: int, matches_exactly=False) -> [str]:
        """
        search from UG any string, not only the author / title
        **WARNING**: too many searches will result in a blocking HTTP ERROR 429
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
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
            html = self.get_google_search_page(query, page)
            if not html:
                self.set_google_max_searches_status_reached()
                raise Exception("No more query is accepted for a while - try again later...")
            self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
            more_songs = len(self.html_parts) > 1
            for part in self.html_parts[1:]:
                link = self.__extract_link(part)
                match_found = False
                if matches_exactly:
                    match_found = self.check_matches_exactly(query, link)
                if match_found or not matches_exactly:
                    if link not in res:
                        print(f"Song found at {link}")
                        res.append(link)
                        link_qty += 1
                        if link_qty >= limit:
                            break
                else:
                    numbers_of_negative_checks += 1
            page += 1
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
        for root_note in Note.CHROMATIC_SCALE_SHARP_BASED:
            search_string = ""
            for degree in degrees:
                chord = Degree.get_chord_from_degree(degree, root_note, mode)
                search_string += chord + " "
            print(search_string)
            songs[search_string] = self.search(search_string, limit_per_tone, matches_exactly)
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

    def get_google_search_page(self, query, page) -> str:
        """
        try to fetch the html page from a google search url
        A wait will be triggered after MAX_QUERIES queries
        NOTE: does not seem to be efficient because the GOOGLE_SEARCH_MAX_WAIT should be several hours
                => could be interesting for massive batches when time does not matter
        :param url:
        :return:
        """
        nb_searches = self.add_new_google_search()
        # wait a bit to avoid being blocked by google
        # see https://github.com/abenassi/Google-Search-API/issues/91
        MAX_QUERIES = 40
        if nb_searches > MAX_QUERIES:
            min_wait = UltimateGuitarSearch.GOOGLE_SEARCH_WAIT_AFTER_REJECTION \
                       - (UltimateGuitarSearch.GOOGLE_SEARCH_WAIT_AFTER_REJECTION * 0.1)
            max_wait = UltimateGuitarSearch.GOOGLE_SEARCH_WAIT_AFTER_REJECTION
            print(f"Too many queries - let's try to wait for {min_wait} to {max_wait} minutes")
            sleep(float(randint(min_wait*60, max_wait*60)))
            self.reset_google_searches()
        url = google_search(query, page, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
        return str(get_html(url))

    def add_new_google_search(self) -> int:
        """
        store the amount of google searches done
        :return:
        """
        try:
            google_searches_log_file_creation_date = self.get_creation_date_google_searches_log_file()
            today = datetime.combine(date.today(), datetime.now().time())
            delta = today - google_searches_log_file_creation_date
            if delta.seconds > UltimateGuitarSearch.GOOGLE_SEARCH_SECURE_WAIT * 60:
                self.reset_google_searches()
                nb_google_searches = 0
            else:
                with open(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME, "r") as nb_google_searches_log_file:
                    nb_google_searches = int(nb_google_searches_log_file.read())
        except Exception as err:
            print(err)
            nb_google_searches = 0
        nb_google_searches += 1
        with open(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME, "w") as nb_google_searches_log_file:
            nb_google_searches_log_file.write(str(nb_google_searches))
        return nb_google_searches

    def get_creation_date_google_searches_log_file(self) -> datetime:
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            time_stamp = os.path.getmtime(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME)
            the_date = datetime.fromtimestamp(time_stamp)
            return the_date
        else:
            stat = os.stat(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME)
            try:
                the_date = datetime.fromtimestamp(stat.st_birthtime)
                return the_date
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                the_date = datetime.fromtimestamp(stat.st_mtime)
                return the_date
        return None # should not happen

    def reset_google_searches(self):
        """
        resets the amount of google searches
        :return:
        """
        os.remove(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME)
        log_exists = os.path.exists(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME)
        # #must wait for the file to be removed
        # while log_exists:
        #     time.sleep(1)
        #     log_exists = os.path.exists(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME)

        with open(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME, "w") as nb_google_searches_log_file:
            nb_google_searches_log_file.write("1")

    def set_google_max_searches_status_reached(self):
        """
        resets the amount of google searches
        :return:
        """
        with open(UltimateGuitarSearch.NB_GOOGLE_SEARCHES_LOG_FILE_NAME, "w") as nb_google_searches_log_file:
            nb_google_searches_log_file.write("1000")

    @staticmethod
    def found_matches(self, songs: dict, all_song) -> bool:
        """
        returns all/one 1 criterion status on songs found by UltimateGuitarSearch.search_songs_from_cadence()
        :param songs:
        :param all_song:    if True => True if all search are found at all keys
                            if false => True returned if we have at least 1 song at least in 1 key
        :return:
        """
        are_all_search_empty = True
        is_there_one_song_found = False
        search_query_failed_qty = 0
        for k in songs.keys():
            if len(songs[k]) == 0:
                search_query_failed_qty += 1
                are_all_search_empty = False
            else:
                is_there_one_song_found = True

        if all_song:
            return are_all_search_empty
        else:
            return is_there_one_song_found
