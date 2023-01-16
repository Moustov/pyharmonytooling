from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor_triads


class TestCircleOf5th(TestCase):
    ut_report = UnitTestReport()

    def test_get_chords_sequences_simple(self):
        cadence = Cadence()
        cof = CircleOf5thNaturalMajor_triads()
        res = cadence.get_chords_sequences("I", cof)
        expected = {'A': 'A ', 'A#': 'A# ', 'B': 'B ', 'C': 'C ', 'C#': 'C# ',
                    'D': 'D ', 'D#': 'D# ', 'E': 'E ', 'F': 'F ', 'F#': 'F# ',
                    'G': 'G ', 'G#': 'G# '}
        self.ut_report.assertTrue(res == expected)

    def test_get_chords_sequences_altered(self):
        cadence = Cadence()
        cof = CircleOf5thNaturalMajor_triads()
        res = cadence.get_chords_sequences("#ii7", cof)
        expected = {'A': 'Cm7 ', 'A#': 'C#m7 ', 'B': 'Dm7 ', 'C': 'D#m7 ', 'C#': 'Em7 ',
                    'D': 'Fm7 ', 'D#': 'F#m7 ', 'E': 'Gm7 ', 'F': 'G#m7 ', 'F#': 'Am7 ',
                    'G': 'A#m7 ', 'G#': 'Bm7 '}
        self.ut_report.assertTrue(res == expected)
