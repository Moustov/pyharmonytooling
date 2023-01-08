import os
from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.song.ultimate_guitar_song import UltimateGuitarSong


class TestUltimateGuitarSong(TestCase):
    utr = UnitTestReport()

    def get_test_song(self, song_file: str) -> UltimateGuitarSong:
        """
        data initializer with a UG not based on [tab] tags
        :return:
        """
        file_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(os.path.abspath(file_path))
        html_file = rf"{dir_path}/{song_file}"
        with open(html_file, 'r') as f:
            html = f.read()
        return html

    def test_extract_tabs_with_tab(self):
        html = self.get_test_song("song_01.html")
        # transcription went through since this is the last digest() step
        ugs = UltimateGuitarSong()
        ugs.extract_tabs_with_tab(html)
        self.utr.assertTrue(ugs.chords_sequence != [], f"No chord found")

    def test_extract_tabs_with_tab2(self):
        html = self.get_test_song("song_03.html")
        # transcription went through since this is the last digest() step
        ugs = UltimateGuitarSong()
        ugs.extract_tabs_with_tab(html)
        self.utr.assertTrue(ugs.chords_sequence != [], f"No chord found")

    def test_extract_tabs_with_chless_tab(self):
        # https://tabs.ultimate-guitar.com/tab/trans-siberian-orchestra/christmas-canon-rock-tabs-3465077
        html = self.get_test_song("song_02.html")
        # transcription went through since this is the last digest() step
        ugs = UltimateGuitarSong()
        ugs.extract_tabs_with_chless_tabs(html)
        self.utr.assertTrue(ugs.chords_sequence != [], f"No chord found")
