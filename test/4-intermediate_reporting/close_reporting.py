from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport


class TestUltimateGuitarSearch(TestCase):
    ut_report = UnitTestReport()

    def test_build_report_synthesis(self):
        self.ut_report.add_synthesis()
        assert True