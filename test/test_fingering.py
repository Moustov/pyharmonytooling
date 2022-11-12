from unittest import TestCase

from deepdiff import DeepDiff

from src.guitar_neck.fingering import Fingering


class TestFingering(TestCase):
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
        assert not res

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

    def test_get_array_from_tab2(self):
        f = Fingering()
        tab = {'E': ['-', '-', '-', '2'],
               'A': ['-', '-', '1', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '-', '2']}
        res = f.get_array_from_tab(tab)
        expected = ["3", "2", "0", "0", "0", "3"]
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
        self.assertFalse(res)

    def test_shift_fingering(self):
        f = Fingering()
        tab = {'E': ['-', '-', '-', '2'],
               'A': ['-', '-', '1', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '-', '2']}
        fret = 3
        res = f.shift_fingering(tab)
        expected_tab = {'E': ['-', '-', '-', '2'],
                        'A': ['-', '-', '1', '-'],
                        'D': ['0', '-', '-', '-'],
                        'G': ['0', '-', '-', '-'],
                        'B': ['0', '-', '-', '-'],
                        'e': ['-', '-', '-', '3']}
        diff = DeepDiff(res, expected_tab, ignore_order=True)
        self.assertEqual(diff, {})

    def test_is_string_index_between_before_fret(self):
        f = Fingering()
        tab = {'E': ['-', '-', '2', '-'],
               'A': ['-', '1', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '2', '-']}
        chord_array = ['2', '1', '0', '0', '0', '2']
        string_index_between = 1
        string2 = 'e'
        string_index1 = 0
        res = f.is_string_index_between_fingered_before_fret(tab, chord_array, string_index_between, string_index1)
        assert (res)

    def test_get_max_finger(self):
        tab = {'E': ['-', '-', '3', '-'],
               'A': ['-', '1', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '2', '-']}
        res = Fingering.get_max_finger(tab)
        assert res == 3

        tab = {'E': ['-', '-', '2', '-'],
               'A': ['-', '1', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['X', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '?', '-']}
        res = Fingering.get_max_finger(tab)
        assert res == 2
