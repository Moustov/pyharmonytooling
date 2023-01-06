from unittest import TestCase

from pychord import Chord

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.song.text_song import TextSongWithLineForChords


class TestTextSong(TestCase):
    ut_report = UnitTestReport()

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
        self.ut_report.assertTrue(the_song.chords_sequence == [Chord("A"), Chord("E"), Chord("E"), Chord("A"),
                                                               Chord("A7"), Chord("D"), Chord("A"), Chord("E"),
                                                               Chord("A")])

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
        self.ut_report.assertTrue(compliance_level_max["compliance_rate"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == "A")
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")
        print(the_song.chords_sequence)
        borrowed_chords = the_song.get_borrowed_chords()
        print("Borrowed chords:", borrowed_chords)
        self.ut_report.assertTrue(borrowed_chords == [])

    def test_degrees_happy_birthday(self):
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
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['I', 'V', 'V', 'I', 'I7', 'IV', 'I', 'V', 'I'])

    def test_degrees_evenou(self):
        song = """
               Dm
        Hevenu Sha- lom halerem
               Gm
        Hevenu Sha- lom halerem
               A7       Gm
        Hevenu Sha- lom ha- lerem
               A7        A7        A7           Dm
        Hevenu Sha- lom, Sha- lom, Sha- lom halerem

        [Verse 1]
                     Dm
        Nous vous a- nnoncons la paix,
                     Gm
        Nous vous a- nnonçons la paix,
                     A7            Dm
        Nous vous a- nnon- çons la paix
                            A7       A7       A7           Dm
        Nous vous annonçons la paix, la paix, la paix en Jésus

        [Verse 2]
                     Dm
        Nous vous a- nnoncons la joie,
                     Gm
        Nous vous a- nnonçons la joie,
                     A7            Dm
        Nous vous a- nnon- çons la joie
                            A7       A7       A7           Dm
        Nous vous annonçons la joie, la joie, la joie en Jésus-Christ

        [Verse 3]
                     Dm
        Nous vous a- nnoncons l'amour,
                     Gm
        Nous vous a- nnonçons l'amour,
                     A7           Dm
        Nous vous a- nnon- çons l'amour
                              A7       A7       A7       Dm
        Nous vous annonçons l'amour, l'amour, l'amour en Jésus

        [Verse 4]
                     Dm
        Nous vous a- nnoncons la paix,
                     Gm
        Nous vous a- nnonçons la joie,
                     A7           Dm
        Nous vous a- nnon- çons l'amour
                            A7       A7         A7       Dm
        Nous vous annonçons la paix, la joie, l'amour en Jésus        """
        the_song = TextSongWithLineForChords()
        the_song.digest(song)
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['ii', 'iv', 'V7', 'iv', 'V7', 'V7', 'V7', 'ii', 'ii', 'iv',
                                                       'V7', 'ii', 'V7', 'V7', 'V7', 'ii', 'ii', 'iv', 'V7', 'ii',
                                                       'V7', 'V7', 'V7', 'ii', 'ii', 'iv', 'V7', 'ii', 'V7', 'V7',
                                                       'V7', 'ii', 'ii', 'iv', 'V7', 'ii', 'V7', 'V7', 'V7', 'ii'])
