from unittest import TestCase

from src.guitar_neck.neck import find_note_from_position, find_positions_from_note


class Test(TestCase):
    def test_find_note_from_position_string_E(self):
        string = "E"
        fret = 0
        res = find_note_from_position(string, fret)
        assert (res == "E")

        string = "E"
        fret = 5
        res = find_note_from_position(string, fret)
        assert (res == "A")

    def test_find_note_from_position_string_D(self):
        string = "D"
        fret = 0
        res = find_note_from_position(string, fret)
        assert (res == "D")

        string = "D"
        fret = 5
        res = find_note_from_position(string, fret)
        assert (res == "G")

    def test_find_positions_from_note(self):
        res = find_positions_from_note("E")
        assert(res == [['E', 0], ['E', 12], ['A', 7], ['D', 2], ['G', 9], ['B', 5], ['e', 0], ['e', 12]])