import os
from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.song.ultimate_guitar_song import UltimateGuitarSong


class TestUltimateGuitarSong(TestCase):
    utr = UnitTestReport()

    def test_digest_html(self):
        ugs = self.get_test_data1()
        # transcription went through since this is the last digest() step
        self.utr.assertTrue(ugs.artist == 'Édith Piaf', f"{ugs.artist} found")

    def test_digest_get_tone_and_mode(self):
        ugs = self.get_test_data1()
        res = ugs.get_tone_and_mode()

        self.utr.assertTrue(res["tone"] == "F", f"{res['tone']} found")
        self.utr.assertTrue(res["cof_name"] == "Melodic Minor", f"{res['cof_name']} found")

    def test_digest_get_borrowed_chords(self):
        ugs = self.get_test_data1()
        tone = ugs.get_tone_and_mode()
        res = ugs.get_borrowed_chords()
        expected = ['Db', 'A', 'A7', 'Em', 'Cm', 'Am', 'Bm', 'D9', 'G#', 'G#6', 'G#M7']
        self.utr.assertTrue(res == expected, f"{res} found")

    def get_test_data1(self) -> UltimateGuitarSong:
        """
        data initializer with a UG not based on [tab] tags
        :return:
        """
        ugs = UltimateGuitarSong()
        # let's get the test file regardless from where the UT in run
        #dir_path = self.ut_report.get_project_path()
        file_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(os.path.abspath(file_path))
        html_file = rf"{dir_path}\no_tab_tags-progression_song.html"
        with open(html_file, 'r') as f:
            html = f.read()
        ugs.digest(html)
        return ugs
