from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.guitar_tab.guitar_tab import GuitarTab


class TestGuitarTab(TestCase):
    ut_report = UnitTestReport()

    def test_get_first_caret_position_across_strings_1(self):
        fingerings = {'e': [-1, -1, [11, 2]], 'B': [-1, [11, 1], -1]}
        res = GuitarTab.get_first_caret_position_across_strings(fingerings)
        self.ut_report.assertTrue(res.fret == 11 and res.caret == 1)

    def test_get_first_caret_position_across_strings_not_found(self):
        fingerings = {'e': [-1, -1], 'B': [-1, -1]}
        res = GuitarTab.get_first_caret_position_across_strings(fingerings)
        self.ut_report.assertTrue(res is None)

    def test_get_next_caret_position_across_strings_5(self):
        fingerings = {'e': [-1, -1, [11, 2], -1], 'B': [-1, -1, -1, [11, 5]]}
        previous_pos = 2
        res = GuitarTab.get_next_caret_position_across_strings(fingerings, previous_pos)
        self.ut_report.assertTrue(res.fret == 11 and res.caret == 5)
