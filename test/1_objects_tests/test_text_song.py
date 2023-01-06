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
        self.ut_report.assertTrue(the_song.degrees == ['i', 'iv', 'V7', 'iv', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'V7',
                                                        'i', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'V7', 'i', 'V7', 'V7',
                                                        'V7', 'i', 'i', 'iv', 'V7', 'i', 'V7', 'V7', 'V7', 'i', 'i',
                                                        'iv', 'V7', 'i', 'V7', 'V7', 'V7', 'i'])

    def test_degrees_sometimes(self):
        song = """
        [Verse]
        A          G
        Tough, you think you've got the stuff
               F#m            D
        You're telling me and anyone
               A
        You're hard enough
            A
        You don't have to put up a fight
            G
        You don't have to always be right
        F#m                     D
        Let me take some of the punches
            A
        For you tonight

        [Verse]
        [F -> C -> Dm]
        I know that we don't talk
        [F -> C -> Am]
        I'm sick of it all
        [F -> C -> Dm]         A
        Can you hear me when I Sing,
               F#m
        you're the reason I sing
        D                 E       A
        You're the reason why the opera is in me

        [Pre Chorus]
              D
        Yeah, hey now
                             A
        Still got to let you know
                                     F#m
        A house still doesn't make a home
                             D
        Don't leave me here alone

        [Chorus]
                 F#m                       E
        And it's you when I look in the mirror
                 D                             D
        And it's you that makes it hard to let go
        F#m                 E               D
        Sometimes you can't make it on your own
        F#m                 E
        Sometimes you can't make it
                     D
        The best you can do is to fake it
        F#m                 E        D
        Sometimes you can't make it on your own
        """
        the_song = TextSongWithLineForChords()
        the_song.digest(song)
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['I', 'VI#', 'vii', 'IV', 'I', 'I', 'VI#', 'vii', 'IV', 'I',
                                                       'VII', 'VII', 'VII', 'I', 'vii', 'IV', 'V', 'I', 'IV', 'I',
                                                       'vii', 'I', 'IV', 'vii', 'V', 'IV', 'IV', 'vii', 'V', 'IV',
                                                       'vii', 'V', 'IV', 'vii', 'V', 'IV'])
