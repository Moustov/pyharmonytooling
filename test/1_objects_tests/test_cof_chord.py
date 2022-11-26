from unittest import TestCase
from pychord import Chord

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.harmony.note import Note


class TestCofChord(TestCase):
    ut_report = UnitTestReport()

    def test_guess_chord_name_C(self):
        expected = CofChord.find_substitutes(Chord("C"))
        notes = [Note("C"), Note("G"), Note("E")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
        self.ut_report.assertTrue(CofChord.same_array_of_chords(res, expected))

    def test_guess_chord_name_Cm(self):
        expected = [Chord("C5/D#"), Chord("Cm"), Chord("Cm/D#"), Chord("Cm/G")]
        notes = [Note("C"), Note("Eb"), Note("G")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
        self.ut_report.assertTrue(CofChord.same_array_of_chords(res, expected))

    def test_guess_chord_name_Cm_only(self):
        expected = [Chord("Cm")]
        notes = [Note("C"), Note("Eb"), Note("G")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=True)
        self.ut_report.assertTrue(CofChord.same_array_of_chords(res, expected))

    def test_guess_chord_name_Gb6_only(self):
        expected = Chord("Gb6")
        notes = [Note("Bb"), Note("Eb"), Note("Gb")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=False, simplest_chord_only=True)
        self.ut_report.assertTrue(CofChord.is_chord_in_array(expected, res))

    def test_guess_chord_name_Cmaj7_only(self):
        expected = Chord("CM7")
        notes = [Note("C"), Note("E"), Note("G"), Note("B")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=True)
        status = CofChord.is_chord_in_array(expected, res)
        self.ut_report.assertTrue(status)

    def test_cofchord_equals_conb_emc(self):
        conb = CofChord("C/B")
        emc = CofChord("Em/C")
        self.ut_report.assertTrue(CofChord.is_same_chord_from_components(conb, emc))

    def test_cofchord_equals_c_c(self):
        c = CofChord("C")
        self.ut_report.assertTrue(CofChord.is_same_chord_from_components(c, c))

    def test_cofchord_equals_ebmaj7_dsmaj7(self):
        ebmaj7 = CofChord("EbM7")
        dsmaj7 = CofChord("D#M7")
        self.ut_report.assertTrue(CofChord.is_same_chord_from_components(ebmaj7, dsmaj7))

    def test_cofchord_equals_cbmaj7_bsmaj7(self):
        cbmaj7 = CofChord("CbM7")
        bsmaj7 = CofChord("BM7")
        self.ut_report.assertTrue(CofChord.is_same_chord_from_components(cbmaj7, bsmaj7))

    def test_cofchord_not_equals_c_d(self):
        c = CofChord("C")
        d = CofChord("D")
        self.ut_report.assertTrue(not CofChord.is_same_chord_from_components(c, d))
