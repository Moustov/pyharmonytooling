from unittest import TestCase

from src.song.ultimate_guitar_search import UltimateGuitarSearch


class TestUltimateGuitarSearch(TestCase):
    def test_search(self):
        ug_searcher = UltimateGuitarSearch()
        songs = ug_searcher.search('Bm7 E7', 3, True)
        print(songs)
        assert len(songs) > 0   # this assert cannot be 100% repeatable because it depends on google
