from unittest import TestCase

from pychord import Chord

from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class TestCofChord(TestCase):
    def test_guess_chord_name_C(self):
        expected = [Chord("C"), Chord("C/E"), Chord("C/G"), Chord("C5/E")]
        notes = [Note("C"), Note("G"), Note("E")]
        res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
        assert res == expected

    def test_guess_chord_name_Cm(self):
        expected = [Chord("Cm"), Chord("Cm/G"), Chord("Cm/D#"), Chord("C5/D#")]
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
