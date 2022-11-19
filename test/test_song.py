from unittest import TestCase

from src.song.song import UltimateGuitarSong


class TestUltimateGuitarSong(TestCase):
    def test_digest_html(self):
        ugs = self.get_test_data1()
        # transcription went through since this is the last digest() step
        assert ugs.artist == 'Édith Piaf'

    def test_digest_get_tone_and_mode(self):
        ugs = self.get_test_data1()

        res = ugs.get_tone_and_mode()
        expected = "G"
        assert res[1] == expected

    def test_digest_get_borrowed_chords(self):
        ugs = self.get_test_data1()
        res = ugs.get_borrowed_chords()
        expected = ['Bb', 'Bb6', 'BbM7', 'Db', 'A', 'Ab', 'A7', 'Cm', 'D9', 'Ab7', 'G#', 'G#6', 'G#M7']
        assert res == expected

    def get_test_data1(self) -> UltimateGuitarSong:
        ugs = UltimateGuitarSong()
        html = ""
        html_file = "C Cm A progression song.html"
        with open(html_file, 'r') as f:
            html = f.read()
        ugs.digest_html(html)
        return ugs