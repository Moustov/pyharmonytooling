from unittest import TestCase

from pychord import Chord

from src.guitar_tab.guitar_tab import GuitarTab


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
        expected =  [Chord("Gb6"), Chord("G#m"), Chord("Bb"), Chord("Gb6")]
        res = GuitarTab.digest_tab(tab)
        assert res == expected

