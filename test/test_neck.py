from unittest import TestCase

from deepdiff import DeepDiff
from pychord import Chord

from src.guitar_neck.fingering import Fingering
from src.guitar_neck.neck import Neck
from src.guitar_neck.neck_exception import NeckException


class Test(TestCase):
    def test_find_note_from_position_string_E(self):
        n = Neck()
        string = "E"
        fret = 0
        res = n.find_note_from_position(string, fret)
        assert (res == "E")

        string = "E"
        fret = 5
        res = n.find_note_from_position(string, fret)
        assert (res == "A")

    def test_find_note_from_position_string_D(self):
        n = Neck()
        string = "D"
        fret = 0
        res = n.find_note_from_position(string, fret)
        assert (res == "D")

        string = "D"
        fret = 5
        res = n.find_note_from_position(string, fret)
        assert (res == "G")

    def test_find_positions_from_note(self):
        n = Neck()
        res = n.find_positions_from_note("E")
        assert (res == [['E', 0], ['E', 12], ['A', 7], ['D', 2], ['G', 9], ['B', 5], ['e', 0], ['e', 12]])

    def test_find_finger_layout2(self):
        fng = Fingering()
        f = [0, 7, 5, 5, 5, 8]
        try:
            res = fng.find_finger_layout(f)
            self.assertTrue(True, msg=f"tab {f} has a possible fingering: {res}")
        except NeckException as neck_err:
            self.assertFalse(False, msg=f"issue with tab {str(f)}: {str(neck_err)}")
        except Exception as err:
            print(f"issue with tab {str(f)}: {str(err)}")
            self.assertFalse(False, msg=f"issue with tab {str(f)}: {str(err)}")

