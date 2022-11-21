from unittest import TestCase

from pychord import Chord

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
        print(the_song.chords_sequence)
        assert the_song.chords_sequence == [Chord("A"), Chord("E"), Chord("E"), Chord("A"), Chord("A7"),
                                            Chord("D"), Chord("A"), Chord("E"), Chord("A")]

    def test_compliance(self):
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
        print(the_song.chords_sequence)
        borrowed_chords = the_song.get_borrowed_chords()
        print("Borrowed chords:", borrowed_chords)
        assert borrowed_chords == []
