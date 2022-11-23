from unittest import TestCase

from pychord import Chord
from src.guitar_tab.guitar_tab import GuitarTab
from src.harmony.cof_chord import CofChord


class TestGuitarTab(TestCase):
    def test_digest_tab_dgbd(self):
        tab = """
        e|--11-----11-----10-----11------------------------------------------------|
        B|--11-----12-----11-----11------------------------------------------------|
        G|--11-----13-----10-----11------------------------------------------------|
        D|-------------------------------------------------------------------------|
        A|-------------------------------------------------------------------------|
        E|-------------------------------------------------------------------------|
        """
        expected = {"2": Chord("D#m"), "8": Chord("G#m"), "15": Chord("Bb"), "22": Chord("D#m")}
        res = GuitarTab.digest_tab_simplest_chords_in_a_bar(tab)
        for (chord_res, chord_expected)  in zip(res.keys(), expected.keys()):
            if CofChord(str(chord_res[0])) != CofChord(str(chord_expected)):
                assert False
        assert True

    def test_digest_tab_d(self):
        tab = """
        e|--11---------------|
        B|------11-----------|
        G|-----------11------|
        D|-------------------|
        A|-------------------|
        E|-------------------|
        """
        expected = {"2": Chord("D#m")}
        res = GuitarTab.digest_tab_simplest_chords_in_a_bar(tab)
        assert res == expected

    def test_digest_tab_eb(self):
        tab = """
        e|--11---|
        B|-------|
        G|-------|
        D|-------|
        A|-------|
        E|-------|
        """
        expected = {"2": Chord("Eb")}
        res = GuitarTab.digest_tab_simplest_chords_in_a_bar(tab)
        assert res == expected
