from unittest import TestCase

from src.song.text_song import TextSongWithLineForChords


class TestTextSong(TestCase):
    def test_digest(self):
        song = """
                            A           E
                    Happy Birthday to you
                          E           A
                    Happy Birthday to you
                          A7            D
                    Happy Birthday dear (name)
                          A        E    A
                    Happy Birthday to you
                """
        the_song = TextSongWithLineForChords()
        the_song.digest(song)
        compliance_level_max = the_song.get_tone_and_mode()
        print("Compliance:", compliance_level_max)
        assert compliance_level_max[0] == 1.0
        assert compliance_level_max[1] == "A"
        assert compliance_level_max[2] == "Natural Major"
        borrowed_chords = the_song.get_borrowed_chords()
        print("Borrowed chords:", borrowed_chords)
        assert borrowed_chords == []
