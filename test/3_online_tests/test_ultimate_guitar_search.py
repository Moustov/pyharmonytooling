from unittest import TestCase

from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class TestUltimateGuitarSearch(TestCase):
    def test_search(self):
        ug_searcher = UltimateGuitarSearch()
        songs = ug_searcher.search('Bm7 E7', 3, matches_exactly=True)
        print(songs)
        assert len(songs) > 0   # this assert cannot be 100% repeatable because it depends on google

    def test_search_cadence_iim7_v7_imaj7(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES["ANATOLE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)

        are_all_search_empty = True
        is_there_one_song_found = False
        search_query_failed_qty = 0
        for k in songs.keys():
            if len(songs[k]) == 0:
                search_query_failed_qty += 1
                are_all_search_empty = False
            else:
                is_there_one_song_found = True

        assert is_there_one_song_found

    def test_search_cadence_vm_ivm6_v(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES["PHRYGIAN_HALF_CADENCE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)

        are_all_search_empty = True
        is_there_one_song_found = False
        search_query_failed_qty = 0
        for k in songs.keys():
            if len(songs[k]) == 0:
                search_query_failed_qty += 1
                are_all_search_empty = False
            else:
                is_there_one_song_found = True

        assert is_there_one_song_found

    def test_search_cadence_iv_ivm_i(self):
        ugs = UltimateGuitarSearch()
        cadence = Cadence.REMARQUABLE_CADENCES["MINOR_PLAGAL_CADENCE"]

        cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
        MAX_SONG_PER_SEARCH = 5

        songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        print(songs)

        are_all_search_empty = True
        is_there_one_song_found = False
        search_query_failed_qty = 0
        for k in songs.keys():
            if len(songs[k]) == 0:
                search_query_failed_qty += 1
                are_all_search_empty = False
            else:
                is_there_one_song_found = True

        assert is_there_one_song_found
