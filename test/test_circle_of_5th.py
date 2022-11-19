from unittest import TestCase

from deepdiff import DeepDiff

from src.harmony.circle_of_5th import CircleOf5th


class TestCircleOf5th(TestCase):
    def test_generate_circle_of_fifths(self):
        c = CircleOf5th()
        cof = c.generate_circle_of_fifths_natural_majors()
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
        diff = DeepDiff(cof, expected, ignore_order=True)
        assert diff == {}

