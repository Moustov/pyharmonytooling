from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor, CircleOf5thNaturalMinor
from pyharmonytools.harmony.degree import Degree


class TestDegree(TestCase):
    ut_report = UnitTestReport()

    def test_get_note_degree_major(self):
        mode = CircleOf5thNaturalMajor()
        self.ut_report.assertTrue(Degree.get_note_degree("C", 1, mode) == "C")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 2, mode) == "D")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 3, mode) == "E")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 4, mode) == "F")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 5, mode) == "G")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 6, mode) == "A")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 7, mode) == "B")

    def test_get_note_degree_nat_minor(self):
        mode = CircleOf5thNaturalMinor()
        self.ut_report.assertTrue(Degree.get_note_degree("C", 1, mode) == "C")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 2, mode) == "D")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 3, mode) == "D#")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 4, mode) == "F")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 5, mode) == "G")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 6, mode) == "G#")
        self.ut_report.assertTrue(Degree.get_note_degree("C", 7, mode) == "A#")
