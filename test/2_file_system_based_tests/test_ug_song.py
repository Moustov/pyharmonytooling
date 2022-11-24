from unittest import TestCase

from pyharmonytools.song.ultimate_guitar_song import UltimateGuitarSong


class TestUltimateGuitarSong(TestCase):
    def test_digest_html(self):
        ugs = self.get_test_data1()
        # transcription went through since this is the last digest() step
        assert ugs.artist == 'Édith Piaf'

    def test_digest_get_tone_and_mode(self):
        ugs = self.get_test_data1()
        res = ugs.get_tone_and_mode()
        assert res[1] == "F"
        assert res[2] == "Melodic Minor"

    def test_digest_get_borrowed_chords(self):
        ugs = self.get_test_data1()
        res = ugs.get_borrowed_chords()
        expected = ['Db', 'A', 'A7', 'Em', 'Cm', 'Am', 'Bm', 'D9', 'G#', 'G#6', 'G#M7']
        assert res == expected

    def get_test_data1(self) -> UltimateGuitarSong:
        """
        data initializer with a UG not based on [tab] tags
        :return:
        """
        ugs = UltimateGuitarSong()
        html_file = r".\no_tab_tags-progression_song.html"
        with open(html_file, 'r') as f:
            html = f.read()
        ugs.digest(html)
        return ugs
