from unittest import TestCase

from deepdiff import DeepDiff
from pychord import Chord

from src.harmony.circle_of_5th import CircleOf5th, CircleOf5thNaturalMinor, CircleOf5thNaturalMajor
from src.harmony.cof_chord import CofChord


class TestCircleOf5th(TestCase):
    def test_generate_circle_of_fifths(self):
        c = CircleOf5thNaturalMajor()
        expected = {
            "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
            "G": ["G", "Am", "Bm", "C", "D", "Em", "Gbdim"],
            "D": ["D", "Em", "Gbm", "G", "A", "Bm", "Dbdim"],
            "A": ["A", "Bm", "Dbm", "D", "E", "Gbm", "Abdim"],
            "E": ["E", "Gbm", "Abm", "A", "B", "Dbm", "Ebdim"],
            "B": ["B", "Dbm", "Ebm", "E", "Gb", "Abm", "Bbdim"],
            "F#": ["F#", "Abm", "Bbm", "B", "Db", "Ebm", "Fdim"],
            "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
            "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
            "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
            "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
            "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
        }
        diff = DeepDiff(c.cof_scales, expected, ignore_order=True)
        assert diff == {}

    def test_find_substitutes(self):
        chord = "G6"
        substitutes = CofChord.find_substitutes(Chord(chord))
        print("substitutes from :", chord, substitutes)
        assert substitutes == [Chord("Em7/9"), Chord("Em7/13"), Chord("Em7/9/G"), Chord("Em7/13/G"), Chord("G6/9/G")]
