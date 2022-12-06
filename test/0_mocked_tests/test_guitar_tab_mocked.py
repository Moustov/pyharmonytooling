from unittest import TestCase

from pychord import Chord

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.guitar_tab.guitar_tab import GuitarTab
from pyharmonytools.guitar_tab.note_fret_caret import NoteFretCaret
from pyharmonytools.harmony.note import Note


def is_tab_equals(res: dict, expected: dict):
    for (res_s, expected_s) in zip(res.keys(), expected.keys()):
        # if res_s != expected_s:
        #     return False
        if res[res_s] != expected[expected_s]:
            return False
    return True


class TestGuitarTab(TestCase):
    ut_report = UnitTestReport()

    def test_is_note_fret_caret_in_same_chord_1(self):
        current_caret = 2
        finger_qty = 0
        first_fret = 11
        note_or_chord = Note('Eb')
        string_name = "B"
        nfc = NoteFretCaret([], first_fret, current_caret, finger_qty, string_name)
        chord_notes = ['']
        res = GuitarTab.is_note_fret_caret_in_same_chord(chord_notes, nfc, first_fret, finger_qty)
        self.ut_report.assertTrue(res)

    def test_is_note_fret_caret_in_same_chord_2(self):
        first_fret = 11
        finger_qty = 1
        current_caret = 6
        string_name = "B"
        nfc = NoteFretCaret(['Bb'], first_fret, current_caret, finger_qty, string_name)
        chord_notes = ['Eb']
        res = GuitarTab.is_note_fret_caret_in_same_chord(chord_notes, nfc, first_fret, finger_qty)
        self.ut_report.assertTrue(res)

    def test_is_note_fret_caret_in_same_chord_3(self):
        first_fret = 11
        finger_qty = 2
        current_caret = 6
        string_name = "G"
        nfc = NoteFretCaret(['Gb'], first_fret, current_caret, finger_qty, string_name)
        chord_notes = ["Eb", "Bb"]
        res = GuitarTab.is_note_fret_caret_in_same_chord(chord_notes, nfc, first_fret, finger_qty)
        self.ut_report.assertTrue(res)

    def test_is_note_fret_caret_in_same_chord_4(self):
        first_fret = 11
        finger_qty = 3
        current_caret = 16
        string_name = "G"
        nfc = NoteFretCaret(Chord("D").components(), first_fret, current_caret, finger_qty, string_name)
        chord_notes = ["Eb", "Bb", "Gb"]
        res = GuitarTab.is_note_fret_caret_in_same_chord(chord_notes, nfc, first_fret, finger_qty)
        self.ut_report.assertTrue(not res)

    def test__get_fingerings_from_tab1(self):
        tab = """
            e|-------|
            B|-----0-|
            G|-------|
            D|---0---|
            A|-------|
            E|-3-----|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [-1, -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [0, 5], -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, -1, -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab2(self):
        tab = """
          e|---------------------|
          B|-----0---0---0-------|
          G|-------2-------------|
          D|---0-------0---0---0-|
          A|---------------------|
          E|-3---------------3---|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [0, 5], -1, -1, -1, [0, 9], -1, -1, -1, [0, 13], -1, -1, -1, -1, -1, -1,
                          -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1, [2, 7], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1, -1, -1, -1, -1, [0, 11], -1, -1, -1, [0, 15], -1, -1, -1,
                          [0, 19], -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, [3, 17], -1, -1, -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab3(self):
        tab = """
          e|---------------------------------|
          B|-----0---0---0-------0---0---0---|
          G|-------2---------------2---------|
          D|---0-------0---0---0-------0---0-|
          A|---------------------------------|
          E|-3---------------3---------------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {
            'e': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                  -1, -1, -1, -1, -1, -1, -1, -1],
            'B': [-1, -1, -1, -1, -1, [0, 5], -1, -1, -1, [0, 9], -1, -1, -1, [0, 13], -1, -1, -1, -1, -1, -1, -1,
                  [0, 21], -1, -1, -1, [0, 25], -1, -1, -1, [0, 29], -1, -1, -1],
            'G': [-1, -1, -1, -1, -1, -1, -1, [2, 7], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                  [2, 23], -1, -1, -1, -1, -1, -1, -1, -1, -1],
            'D': [-1, -1, -1, [0, 3], -1, -1, -1, -1, -1, -1, -1, [0, 11], -1, -1, -1, [0, 15], -1, -1, -1, [0, 19], -1,
                  -1, -1, -1, -1, -1, -1, [0, 27], -1, -1, -1, [0, 31], -1],
            'A': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                  -1, -1, -1, -1, -1, -1, -1, -1],
            'E': [-1, [3, 1], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, [3, 17], -1, -1, -1, -1, -1,
                  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab4(self):
        tab = """
            e|-------|
            B|-----0-|
            G|-------|
            D|---0---|
            A|-------|
            E|-3---0-|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [-1, -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [0, 5], -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, [0, 5], -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab5(self):
        tab = """
            e|0------|
            B|-----0-|
            G|-------|
            D|---0---|
            A|-------|
            E|-3---0-|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [[0, 0], -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [0, 5], -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, [0, 5], -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab6(self):
        tab = """
            e|0------|
            B|-----0-|
            G|-------|
            D|---0---|
            A|-------|
            E|-3----0|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [[0, 0], -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [0, 5], -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, -1, [0, 6]]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test__get_fingerings_from_tab7(self):
        tab = """
            e|--------|
            B|-----11-|
            G|--------|
            D|---0----|
            A|--------|
            E|-3------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'e': [-1, -1, -1, -1, -1, -1, -1, -1],
                    'B': [-1, -1, -1, -1, -1, [11, 5], -1, -1],
                    'G': [-1, -1, -1, -1, -1, -1, -1, -1],
                    'D': [-1, -1, -1, [0, 3], -1, -1, -1, -1],
                    'A': [-1, -1, -1, -1, -1, -1, -1, -1],
                    'E': [-1, [3, 1], -1, -1, -1, -1, -1, -1]}
        gt = GuitarTab(tab)
        res = gt._bars_tab_dict[0]
        diff = is_tab_equals(res, expected)
        self.ut_report.assertTrue(diff)

    def test_split_tab_in_bars(self):
        tab = """
        
            e|-1----|-2----|
            B|------|------|
            G|------|------|
            D|------|------|
            A|------|------|
            E|------|------|


            e|-3----|-4----|
            B|------|------|
            G|------|------|
            D|------|------|
            A|------|------|
            E|------|------|
"""
        gt = GuitarTab(tab)
        assert len(gt.bars_ascii) == 4
