from unittest import TestCase

from deepdiff import DeepDiff

from src.guitar_neck.fingering import Fingering


class Test(TestCase):
    def test_same_finger_same_fret_with_lower_fingers_between1(self):
        f = Fingering()
        tab = {
            "e": ["-", "-", "3", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["-", "1", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        chord_array = f.get_array_from_tab(tab)
        res = f.same_finger_same_fret_with_lower_fingers_between(tab, chord_array)
        assert not res

    def test_same_finger_same_fret_with_lower_fingers_between2(self):
        f = Fingering()
        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        chord_array = f.get_array_from_tab(tab)
        res = f.same_finger_same_fret_with_lower_fingers_between(tab, chord_array)
        assert res

    def test_get_array_from_tab(self):
        f = Fingering()
        tab = {
            "e": ["0", "-", "-", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["0", "-", "-", "-"]
        }
        res = f.get_array_from_tab(tab)
        expected = ["0", "0", "0", "0", "0", "0"]
        assert res == expected

        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["0", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        res = f.get_array_from_tab(tab)
        expected = ["2", "0", "0", "0", "0", "2"]
        assert res == expected

        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["X", "-", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        res = f.get_array_from_tab(tab)
        expected = ["2", "0", "0", "0", "X", "2"]
        assert res == expected

        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["-", "-", "-", "3"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        res = f.get_array_from_tab(tab)
        expected = ["2", "0", "0", "0", "3", "2"]
        assert res == expected

    def test_get_tab_from_array(self):
        f = Fingering()
        ca = ["X", "1", "0", "0", "3", "2"]
        res = f.get_tab_from_array(ca)
        expected_tab = {
            "e": ["-", "-", "?", "-"],
            "B": ["-", "-", "-", "?"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["-", "?", "-", "-"],
            "E": ["X", "-", "-", "-"]
        }
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_same_finger_same_fret_with_lower_fingers_between(self):
        f = Fingering()
        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["-", "-", "-", "3"],
            "G": ["-", "-", "-", "3"],
            "D": ["-", "-", "-", "3"],
            "A": ["-", "-", "-", "3"],
            "E": ["-", "-", "2", "-"]
        }
        chord_array = f.get_array_from_tab(tab)
        res = f.same_finger_same_fret_with_lower_fingers_between(tab, chord_array)
        self.assertFalse(res)

        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["-", "1", "-", "-"],
            "G": ["0", "-", "-", "-"],
            "D": ["0", "-", "-", "-"],
            "A": ["0", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        chord_array = f.get_array_from_tab(tab)
        res = f.same_finger_same_fret_with_lower_fingers_between(tab, chord_array)
        self.assertTrue(res)

        tab = {
            "e": ["-", "-", "2", "-"],
            "B": ["X", "-", "-", "-"],
            "G": ["X", "-", "-", "-"],
            "D": ["X", "-", "-", "-"],
            "A": ["X", "-", "-", "-"],
            "E": ["-", "-", "2", "-"]
        }
        chord_array = f.get_array_from_tab(tab)
        res = f.same_finger_same_fret_with_lower_fingers_between(tab, chord_array)
        self.assertTrue(res)
