from unittest import TestCase

from pychord import Chord

from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.circle_of_5th import CircleOf5th, CircleOf5thNaturalMajor
from pyharmonytools.harmony.cof_chord import CofChord


class Test(TestCase):
    ut_report = UnitTestReport()

    def test_guess_tone_and_mode_C(self):
        song = """
        C Dm Em F G Am Bdim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'C')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_guess_tone_and_mode_Db(self):
        song = """
        C# D#m E#m F# G# A#m B#dim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'Db')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_guess_tone_and_mode_E(self):
        song = """
        E F#m G#m A B C#m D#dim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'E')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_guess_tone_and_mode_F(self):
        song = """
        F Gm Am Bb C Dm Edim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'F')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_guess_tone_and_mode_Bb(self):
        song = """
        Bb, Cm, Dm, E, F, Gm, Adim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'Bb')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_guess_tone_and_mode_happy_birthday_chords(self):
        _HarmonyLogger.outcome_level_of_detail = _HarmonyLogger.LOD_NONE
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
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        print(compliance_level_max)
        self.ut_report.assertTrue(compliance_level_max["compliance_level"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == 'A')
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")

    def test_get_chord_possible_qualities(self):
        cof = CircleOf5thNaturalMajor()
        tones = cof.generate_circle_of_fifths()
        for tone in tones:
            for chord_tone in tones[tone]:
                possible_chord_qualities = CofChord.get_chord_names_possible_qualities(chord_tone)
                c = Chord(tone + "m")
                tc = Chord(chord_tone)
                if c in possible_chord_qualities and tc.quality.quality == "":
                    print(c, "Minor chord cannot be a possible Major chord")
                    self.fail()
        self.ut_report.assertTrue(True)

    def test_get_borrowed_chords_C(self):
        song = """
                C Dm Em F G Am Bdim
                """
        cof = CircleOf5thNaturalMajor()
        cp = cof.digest_song(song)

        tone = cof.generate_circle_of_fifths()["C"]
        borrowed_chords = cof.get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        self.ut_report.assertTrue(len(borrowed_chords) == 0)

    def test_get_borrowed_chords_Cm(self):
        song = """
                C Dm Em F G Am Bdim Cdim
                """
        cof = CircleOf5thNaturalMajor()
        cp = cof.digest_song(song)
        tone = cof.generate_circle_of_fifths()["C"]
        borrowed_chords = cof.get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        self.ut_report.assertTrue(borrowed_chords == {"Cdim": True})
