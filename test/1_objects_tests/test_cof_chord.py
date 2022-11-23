from unittest import TestCase
from pychord import Chord
from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class TestCofChord(TestCase):
    def test_guess_chord_name_C(self):
        expected = CofChord.find_substitutes(Chord("C"))
        notes = [Note("C"), Note("G"), Note("E")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
        assert res == expected

    def test_guess_chord_name_Cm(self):
        expected = [Chord("C5/D#"), Chord("Cm"), Chord("Cm/D#"), Chord("Cm/G")]
        notes = [Note("C"), Note("Eb"), Note("G")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
        assert res == expected

    def test_guess_chord_name_Cm_only(self):
        expected = [Chord("Cm")]
        notes = [Note("C"), Note("Eb"), Note("G")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=True)
        assert res == expected

    def test_guess_chord_name_Cmaj7_only(self):
        expected = [Chord("Cmaj7")]
        notes = [Note("C"), Note("E"), Note("G"), Note("B")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=True)
        assert res == expected

    def test_cofchord_equals_conb_emc(self):
        conb = CofChord("C/B")
        emc = CofChord("Em/C")
        assert CofChord.is_same_chord_from_components(conb, emc)

    def test_cofchord_equals_c_c(self):
        c = CofChord("C")
        assert CofChord.is_same_chord_from_components(c, c)

    def test_cofchord_equals_ebmaj7_dsmaj7(self):
        ebmaj7 = CofChord("EbM7")
        dsmaj7 = CofChord("D#M7")
        assert CofChord.is_same_chord_from_components(ebmaj7, dsmaj7)

    def test_cofchord_equals_cbmaj7_bsmaj7(self):
        cbmaj7 = CofChord("CbM7")
        bsmaj7 = CofChord("BM7")
        assert CofChord.is_same_chord_from_components(cbmaj7, bsmaj7)

    def test_cofchord_not_equals_c_d(self):
        c = CofChord("C")
        d = CofChord("D")
        assert not CofChord.is_same_chord_from_components(c, d)
