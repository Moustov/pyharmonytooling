from unittest import TestCase

from pychord import Chord

from src.guitar_neck.neck import find_note_from_position, find_positions_from_note, get_fingering_from_chord


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

    def test_chord_fingering(self):
        f = get_fingering_from_chord(Chord("C"))
        assert(f == [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3], [3, 3, 2, 0, 1, 0], [3, 3, 2, 0, 1, 3],
                     [3, 3, 2, 5, 1, 3], [3, 3, 2, 5, 5, 3], [3, 3, 5, 5, 1, 3], [3, 3, 5, 5, 5, 3],
                     [3, 7, 5, 5, 5, 3], [8, 7, 5, 5, 5, 8], [8, 7, 5, 5, 8, 8], [8, 7, 5, 9, 5, 8],
                     [8, 7, 5, 9, 8, 8], [8, 7, 10, 9, 8, 8], [8, 10, 10, 9, 8, 8], [8, 10, 10, 9, 8, 12],
                     [8, 10, 10, 12, 8, 8], [8, 10, 10, 12, 8, 12], [12, 10, 10, 9, 8, 8],
                     [12, 10, 10, 9, 8, 12], [12, 10, 10, 12, 8, 8], [12, 10, 10, 12, 8, 12]])
