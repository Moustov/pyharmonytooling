from unittest import TestCase

from pychord import Chord

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.guitar_tab.guitar_tab import GuitarTab
from pyharmonytools.guitar_tab.note_fret_caret import NoteFretCaret
from pyharmonytools.harmony.note import Note


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
