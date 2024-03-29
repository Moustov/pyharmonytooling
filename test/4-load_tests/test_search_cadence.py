from datetime import datetime, date
from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor_triads
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class _TestRobustness(TestCase):
    """
    rename class with TestRobustness to enable unit test running
    """
    ut_report = UnitTestReport()

    def _test_google_query_robustness_at_least_one(self):
        print(r"/!\ this unit test lasts 2hrs to reach the positive assert")
        ugs = UltimateGuitarSearch()
        cadence = "ii7-V7-Imaj7"
        # the mode should rather be guessed from the cadence
        cof_maj = Cadence.guess_tone_and_mode_from_cadence(cadence)

        TEST_BATCH_DURATION = 2   # in hours
        batch_start = datetime.combine(date.today(), datetime.now().time())
        batch_situation = datetime.combine(date.today(), datetime.now().time())
        delta = batch_situation - batch_start
        MAX_SONG_PER_SEARCH = 5
        while delta.seconds < TEST_BATCH_DURATION * 60 * 60:
            print("=================")
            songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True, try_avoiding_blocked_searches=True)
            print(songs)

            self.ut_report.assertTrue(UltimateGuitarSearch.found_matches(songs=songs, all_song=False))
            batch_situation = datetime.combine(date.today(), datetime.now().time())
            delta = batch_situation - batch_start

        self.ut_report.assertTrue(True)

    def _test_google_query_robustness_all(self):
        print(r"/!\ this unit test lasts 2hrs to reach the positive assert")
        ugs = UltimateGuitarSearch()
        cadence = "ii7-V7-Imaj7"
        # the mode should rather be guessed from the cadence
        cof_maj = Cadence.guess_tone_and_mode_from_cadence(cadence)

        TEST_BATCH_DURATION = 2   # in hours
        batch_start = datetime.combine(date.today(), datetime.now().time())
        batch_situation = datetime.combine(date.today(), datetime.now().time())
        delta = batch_situation - batch_start
        MAX_SONG_PER_SEARCH = 5
        while delta.seconds < TEST_BATCH_DURATION * 60 * 60:
            print("=================")
            songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True, try_avoiding_blocked_searches=True)
            print(songs)
            self.ut_report.assertTrue(UltimateGuitarSearch.found_matches(songs=songs, all_song=True))
            batch_situation = datetime.combine(date.today(), datetime.now().time())
            delta = batch_situation - batch_start

        self.ut_report.assertTrue(True)
