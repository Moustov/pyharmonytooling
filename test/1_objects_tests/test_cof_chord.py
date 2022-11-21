from unittest import TestCase

from pychord import Chord

from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class TestCofChord(TestCase):
    def test_guess_chord_name(self):
        expected = Chord("C")
        notes = [ Note("C"), Note("G"), Note("E")]
        res = CofChord.guess_chord_name(notes)
        assert res == expected
