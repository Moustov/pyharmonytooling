from unittest import TestCase

from pychord import Chord
from src.guitar_tab.guitar_tab import GuitarTab
from src.harmony.cof_chord import CofChord


class TestGuitarTab(TestCase):
    def test_digest_tab(self):
        tab = """
        e|--11-----11-----10-----11------------------------------------------------|
        B|--11-----12-----11-----11------------------------------------------------|
        G|--11-----13-----10-----11------------------------------------------------|
        D|-------------------------------------------------------------------------|
        A|-------------------------------------------------------------------------|
        E|-------------------------------------------------------------------------|
        """
        expected = [Chord("D#m"), Chord("G#m"), Chord("Bb"), Chord("D#m")]
        res = GuitarTab.digest_tab(tab)
        for (c_res, c_expected) in zip(res, expected):
            if CofChord(str(c_res[0])) != CofChord(str(c_expected)):
                assert False
        assert True

