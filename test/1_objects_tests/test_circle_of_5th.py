from unittest import TestCase

from deepdiff import DeepDiff
from pychord import Chord

from src.harmony.circle_of_5th import CircleOf5thNaturalMajor
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

    def test_find_substitutes_g6(self):
        chord = "G6"
        substitutes = CofChord.find_substitutes(Chord(chord))
        print("substitutes from :", chord, substitutes)
        expected = [Chord("Em7"), Chord("Em7/9"), Chord("Em7/11"), Chord("Em7/13"), Chord("Em/D"),
                    Chord("Em7/B"), Chord("Em7/D"), Chord("Em7/G"), Chord("Em7/9/B"), Chord("Em7/9/D"),
                    Chord("Em7/9/G"), Chord("Em7/11/B"), Chord("Em7/11/D"), Chord("Em7/11/G"),
                    Chord("Em7/13/B"), Chord("Em7/13/D"), Chord("Em7/13/G"),
                    Chord("G6"), Chord("G6/9"), Chord("G/E"),
                    Chord("G6/B"), Chord("G6/D"), Chord("G6/E"), Chord("G6/9/B"), Chord("G6/9/D"), Chord("G6/9/E")]
        assert CofChord.same_array_of_chords(substitutes, expected)

    def test_find_substitutes_c(self):
        chord = "C"
        substitutes = CofChord.find_substitutes(Chord(chord))
        expected = [Chord("C"), Chord("C/E"), Chord("C/G"), Chord("C5/E")]
        print("substitutes from :", chord, substitutes)
        assert CofChord.same_array_of_chords(substitutes, expected)

