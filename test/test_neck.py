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

    def test_all_possible_C_chords_with_all_string(self):
        n = Neck()
        Fingering.FINGERING_WIDTH = 3
        n.FRET_QUANTITY = n.FRET_QUANTITY_CLASSIC
        n.TUNING = ['E', 'A', 'D', 'G', 'B', 'e']
        fng = Fingering()
        possible_fingerings = fng.get_fingering_from_chord(Chord("C"), all_strings=True)
        res = []
        for f in possible_fingerings:
            # remove any impossible fingering
            try:
                tab = fng.find_finger_layout(f)
                res.append(f)
            except NeckException as neck_err:
                print(f"issue with tab {str(f)}: {str(neck_err)}")
            except Exception as err:
                print(f"issue with tab {str(f)}: {str(err)}")

        # expected_tab = [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3], [3, 3, 2, 0, 1, 0], [3, 3, 2, 0, 1, 3],
        #              [3, 3, 2, 5, 1, 3], [3, 3, 2, 5, 5, 3], [3, 3, 5, 5, 1, 3], [3, 3, 5, 5, 5, 3],
        #              [3, 7, 5, 5, 5, 3], [8, 7, 5, 5, 5, 8], [8, 7, 5, 5, 8, 8], [8, 7, 5, 9, 5, 8],
        #              [8, 7, 5, 9, 8, 8], [8, 7, 10, 9, 8, 8], [8, 10, 10, 9, 8, 8], [8, 10, 10, 9, 8, 12],
        #              [8, 10, 10, 12, 8, 8], [8, 10, 10, 12, 8, 12], [12, 10, 10, 9, 8, 8],
        #              [12, 10, 10, 9, 8, 12], [12, 10, 10, 12, 8, 8], [12, 10, 10, 12, 8, 12]]

        # impossible
        # [3, 3, 2, 0, 1, 3], [3, 3, 2, 5, 1, 3], [3, 3, 2, 5, 5, 3], [3, 3, 5, 5, 1, 3], [8, 7, 5, 5, 5, 8],
        # [8, 7, 5, 5, 8, 8], [8, 7, 5, 9, 5, 8],
        # [8, 7, 5, 9, 8, 8], [8, 7, 10, 9, 8, 8], [12, 10, 10, 9, 8, 12], [12, 10, 10, 12, 8, 12]

        expected_tab = [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3],
                        [3, 3, 2, 0, 1, 0], [3, 3, 2, 0, 1, 3], [3, 3, 5, 5, 5, 3], [3, 7, 5, 5, 5, 3],
                        [8, 10, 10, 9, 8, 8], [8, 10, 10, 9, 8, 12],
                        [8, 10, 10, 12, 8, 8], [8, 10, 10, 12, 8, 12],
                        [12, 10, 10, 9, 8, 8], [12, 10, 10, 12, 8, 8]]

        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_C_chords(self):
        f = Fingering()
        # C
        Fingering.FINGERING_WIDTH = 4
        fingerable_chords = [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3], [3, 3, 2, 0, 1, 0],
                             [3, 3, 5, 5, 5, 3], [3, 7, 5, 5, 5, 3],
                             [8, 10, 10, 9, 8, 8], [8, 10, 10, 9, 8, 12],
                             [8, 10, 10, 12, 8, 8], [8, 10, 10, 12, 8, 12], [12, 10, 10, 9, 8, 8],
                             [12, 10, 10, 12, 8, 8]]
        for fc in fingerable_chords:
            try:
                res = f.find_finger_layout(chord_layout=fc)
                print(f"successful fingerable_chords {fc}")
                assert True
            except NeckException as impossible_fingering:
                print(f"failing fingerable_chords {fc}: {impossible_fingering}")
                assert False

    def test_find_finger_layout_C(self):
        f = Fingering()
        # C
        Fingering.FINGERING_WIDTH = 4
        res = f.find_finger_layout(chord_layout=[0, 3, 2, 0, 1, 0])
        expected_tab = {
            "E": ["0", "-", "-", "-"],
            "A": ["-", "-", "-", "3"],
            "D": ["-", "-", "2", "-"],
            "G": ["0", "-", "-", "-"],
            "B": ["-", "1", "-", "-"],
            "e": ["0", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_G(self):
        f = Fingering()

        # G
        expected_tab = {
            "e": ["-", "-", "3", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["-", "1", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        res = f.find_finger_layout(chord_layout=[3, 2, 0, 0, 0, 3])
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_all_muted(self):
        f = Fingering()

        # all muted
        res = f.find_finger_layout(chord_layout=[-1, -1, -1, -1, -1, -1, ])
        expected_tab = {
            "e": ["X", "-", "-", "-"],
            "B": ["X", "-", "-", "-"],
            "G": ["X", "-", "-", "-"],
            "D": ["X", "-", "-", "-"],
            "A": ["X", "-", "-", "-"],
            "E": ["X", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_all_open(self):
        f = Fingering()

        # all open
        res = f.find_finger_layout(chord_layout=[0, 0, 0, 0, 0, 0])
        expected_tab = {
            "e": ["0", "-", "-", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["0", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_E(self):
        f = Fingering()

        # E
        res = f.find_finger_layout(chord_layout=[0, 2, 2, 1, 0, 0])
        expected_tab = {
            "e": ["0", "-", "-", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["-", "1", "-", "-"],
            "D": ["-", "-", "2", "-"],
            "A": ["-", "-", "2", "-"],
            "E": ["0", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_finger_layout_D(self):
        f = Fingering()

        # D
        res = f.find_finger_layout(chord_layout=[-1, 0, 0, 2, 3, 2])
        expected_tab = {
            "e": ["-", "-", "1", "-"],
            "B": ["-", "-", "-", "2"],
            "G": ["-", "-", "1", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["X", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})
