from unittest import TestCase

from deepdiff import DeepDiff

from pyharmonytools.guitar_neck.fingering import Fingering
from pyharmonytools.guitar_neck.neck import Neck


class TestFingering(TestCase):
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
        expected = [0, 0, 0, 0, 0, 0]
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
        expected = [2, 0, 0, 0, 0, 2]
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
        expected = [2, 0, 0, 0, -1, 2]
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
        expected = [2, 0, 0, 0, 3, 2]
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
        expected = [3, 2, 0, 0, 0, 3]
        assert res == expected

    def test_get_tab_from_array(self):
        f = Fingering()
        ca = [-1, 1, 0, 0, 3, 2]
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

    def test_is_string_index_between_before_fret_G(self):
        f = Fingering()
        tab = {'E': ['-', '-', '2', '-'],
               'A': ['-', '1', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['0', '-', '-', '-'],
               'e': ['-', '-', '2', '-']}
        chord_array = f.get_array_from_tab(tab)
        barres = f.find_possible_barres(chord_array)
        string = 'A'
        fret = chord_array[Neck.TUNING.index(string)]
        res = f.is_string_fingered_before_fret(barres, chord_array, fret, string)
        assert not res

    def test_is_string_index_between_before_fret_C(self):
        f = Fingering()
        tab = {'E': ['-', '-', '-', '3'],
               'A': ['-', '-', '-', '3'],
               'D': ['-', '-', '2', '-'],
               'G': ['0', '-', '-', '-'],
               'B': ['-', '1', '-', '-'],
               'e': ['0', '-', '-', '-']}
        chord_array = f.get_array_from_tab(tab)
        barres = f.find_possible_barres(chord_array)
        string = 'A'
        fret = 3
        res = f.is_string_fingered_before_fret(barres, chord_array, fret, string)
        assert (not res)

    def test_is_string_index_between_before_fret_partial_D(self):
        f = Fingering()
        tab = {'E': ['X', '-', '-', '-'],
               'A': ['0', '-', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['-', '-', '1', '-'],
               'B': ['-', '-', '-', '?'],
               'e': ['0', '-', '?', '-']}
        chord_array = f.get_array_from_tab(tab)
        barres = f.find_possible_barres(chord_array)
        for string in Neck.TUNING:
            fret = chord_array[Neck.TUNING.index(string)]
            res = f.is_string_fingered_before_fret(barres, chord_array, fret, string)
            assert (not res)

    def test_is_string_index_between_before_fret_D(self):
        f = Fingering()
        tab = {'E': ['X', '-', '-', '-'],
               'A': ['0', '-', '-', '-'],
               'D': ['0', '-', '-', '-'],
               'G': ['-', '-', '1', '-'],
               'B': ['-', '-', '-', '2'],
               'e': ['0', '-', '1', '-']}
        chord_array = f.get_array_from_tab(tab)
        barres = f.find_possible_barres(chord_array)
        for string in Neck.TUNING:
            fret = chord_array[Neck.TUNING.index(string)]
            res = f.is_string_fingered_before_fret(barres, chord_array, fret, string)
            assert (not res)

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

    def test_find_barres_F(self):
        f = Fingering()
        chord_layout = [1, 3, 3, 2, 1, 1]
        res = f.find_possible_barres(chord_layout)
        expected = {"1": [0, 4, 5], "2": [3], "3": [1, 2]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_barres_G(self):
        f = Fingering()
        chord_layout = [3, 5, 5, 4, 3, 3]
        res = f.find_possible_barres(chord_layout)
        expected = {"3": [0, 4, 5], "4": [3], "5": [1, 2]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_barres_C(self):
        f = Fingering()
        chord_layout = [3, 3, 2, 0, 1, 0]
        res = f.find_possible_barres(chord_layout)
        expected = {"3": [0, 1], "2": [2], "1": [4]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.assertEqual(diff, {})

    def test_find_barres_D(self):
        f = Fingering()
        chord_layout = [-1, 0, 0, 1, 2, 1]
        res = f.find_possible_barres(chord_layout)
        expected = {"2": [4], "1": [3, 5]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.assertEqual(diff, {})
