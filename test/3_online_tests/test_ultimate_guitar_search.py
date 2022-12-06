from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class _TestUltimateGuitarSearch(TestCase):
    """
    rename class with TestUltimateGuitarSearch to enable unit test running
    """
    ut_report = UnitTestReport()

    def _test_search(self):
        ug_searcher = UltimateGuitarSearch()
        songs = ug_searcher.search('Bm7 E7', 3, artist=None, matches_exactly=True)
        print(songs)
        self.ut_report.assertTrue(len(songs) > 0)   # this assert cannot be 100% repeatable because it depends on google

    def _test_search_cadence_iim7_v7_imaj7(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES_NATURAL_MAJOR["ANATOLE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)
        self.ut_report.assertTrue(UltimateGuitarSearch.found_matches(songs=songs, all_song=False))

    def _test_search_cadence_vm_ivm6_v(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES_HYBRID["PHRYGIAN_HALF_CADENCE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)
        self.ut_report.assertTrue(UltimateGuitarSearch.found_matches(songs=songs, all_song=False))

    def _test_search_cadence_iv_ivm_i(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES_HYBRID["MINOR_PLAGAL_CADENCE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)
        self.ut_report.assertTrue(UltimateGuitarSearch.found_matches(songs=songs, all_song=False))
