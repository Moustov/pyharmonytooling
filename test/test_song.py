from unittest import TestCase

from src.song.song import UltimateGuitarSong


class TestUltimateGuitarSong(TestCase):
    def test_digest_html(self):
        ugs = UltimateGuitarSong()
        html = ""
        html_file = "C Cm A progression song.html"
        with open(html_file, 'r') as f:
            html = f.read()
        ugs.digest_html(html)
        # transcription went through since this is the last digest() step
        assert ugs.artist == 'Édith Piaf'
