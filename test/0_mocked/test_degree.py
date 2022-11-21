from unittest import TestCase

from src.harmony.circle_of_5th import CircleOf5thNaturalMajor, CircleOf5thNaturalMinor
from src.harmony.degree import Degree


class TestDegree(TestCase):
    def test_get_note_degree_major(self):
        mode = CircleOf5thNaturalMajor()
        assert Degree.get_note_degree("C", 1, mode) == "C"
        assert Degree.get_note_degree("C", 2, mode) == "D"
        assert Degree.get_note_degree("C", 3, mode) == "E"
        assert Degree.get_note_degree("C", 4, mode) == "F"
        assert Degree.get_note_degree("C", 5, mode) == "G"
        assert Degree.get_note_degree("C", 6, mode) == "A"
        assert Degree.get_note_degree("C", 7, mode) == "B"

    def test_get_note_degree_nat_minor(self):
        mode = CircleOf5thNaturalMinor()
        assert Degree.get_note_degree("C", 1, mode) == "C"
        assert Degree.get_note_degree("C", 2, mode) == "D"
        assert Degree.get_note_degree("C", 3, mode) == "D#"
        assert Degree.get_note_degree("C", 4, mode) == "F"
        assert Degree.get_note_degree("C", 5, mode) == "G"
        assert Degree.get_note_degree("C", 6, mode) == "G#"
        assert Degree.get_note_degree("C", 7, mode) == "A#"
