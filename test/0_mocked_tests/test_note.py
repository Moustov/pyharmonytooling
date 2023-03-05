from unittest import TestCase

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.harmony.note import Note


class TestNote(TestCase):
    ut_report = UnitTestReport()

    def test_weird_notes(self):
        self.ut_report.assertTrue(Note("Cb") != Note("D"))
        self.ut_report.assertTrue(Note("Cb") == Note("B"))
        self.ut_report.assertTrue(Note("Fb") == Note("E"))
        self.ut_report.assertTrue(Note("B#") == Note("C"))
        self.ut_report.assertTrue(Note("E#") == Note("F"))

    def test_notes_equals(self):
        # canonics
        self.ut_report.assertTrue(Note("C") == Note("C"))
        self.ut_report.assertTrue(Note("C") != Note("B"))
        self.ut_report.assertTrue(Note("C#") != Note("D"))
        # tempered equivalences
        self.ut_report.assertTrue(Note("A#") == "Bb")
        self.ut_report.assertTrue(Note("C#") == Note("Db"))
        self.ut_report.assertTrue(Note("C#") == "Db")
        # limits
        self.ut_report.assertTrue(Note("G#") == "Ab")

    def test_enharmonic_notes(self):
        self.ut_report.assertTrue(Note("C##") == "D")
        self.ut_report.assertTrue(Note("Cbb") == "Bb")

    def test_all_equals(self):
        # todo add Note.CHROMATIC_SCALE_WEIRD_NOTES
        for n1, n2 in zip(Note.CHROMATIC_SCALE_SHARP_BASED, Note.CHROMATIC_SCALE_FLAT_BASED):
            print(n1, "==", n2)
            self.ut_report.assertTrue(Note(n1) == Note(n2))
        for n1 in Note.CHROMATIC_SCALE_SHARP_BASED:
            for n2 in Note.CHROMATIC_SCALE_FLAT_BASED:
                print(n1, "!=", n2)
                if Note(n1) != Note(n2):
                    self.ut_report.assertTrue(Note(n1) != Note(n2))

    def test_get_interval_c_e(self):
        c = Note("C")
        e = Note("E")
        res = c.get_interval_in_half_tones(e)
        self.ut_report.assertTrue(res == 4)

    def test_get_interval_e_c(self):
        c = Note("C")
        e = Note("E")
        res = e.get_interval_in_half_tones(c)
        self.ut_report.assertTrue(res == -4)

    def test_get_interval_c_g(self):
        c = Note("C")
        g = Note("G")
        res = c.get_interval_in_half_tones(g)
        self.ut_report.assertTrue(res == 7)

    def test_get_interval_cs_es(self):
        cs = Note("C#")
        es = Note("E#")  # the get_interval() should translate this into F
        res = cs.get_interval_in_half_tones(es)
        self.ut_report.assertTrue(res == 4)

    def test_get_interval_gs_ab(self):
        gs = Note("G#")
        ab = Note("Ab")  # the get_interval() should translate this into F
        res = gs.get_interval_in_half_tones(ab)
        self.ut_report.assertTrue(res == 0)

    def test_get_interval_ab_gs(self):
        gs = Note("G#")
        ab = Note("Ab")  # the get_interval() should translate this into F
        res = gs.get_interval_in_half_tones(ab)
        self.ut_report.assertTrue(res == 0)

    def test_all_note_index(self):
        index = 0
        for n in Note.CHROMATIC_SCALE_FLAT_BASED:
            print(n)
            self.ut_report.assertTrue(Note.get_index(n) == index)
            index += 1
        index = 0
        for n in Note.CHROMATIC_SCALE_SHARP_BASED:
            print(n)
            self.ut_report.assertTrue(Note.get_index(n) == index)
            index += 1
        index = 0
        for n in Note.CHROMATIC_SCALE_ENHARMONIC_NOTES:
            print(n)
            self.ut_report.assertTrue(Note.get_index(n) == index)
            index += 1

    def test_get_all_interval(self):
        # todo add Note.CHROMATIC_SCALE_WEIRD_NOTES
        for n1, n2 in zip(Note.CHROMATIC_SCALE_SHARP_BASED, Note.CHROMATIC_SCALE_FLAT_BASED):
            print(n1, " - ", n2)
            d = Note(n1).get_interval_in_half_tones(Note(n2))
            print(" = ", d)
            self.ut_report.assertTrue(d == 0)
        i_n1 = 0
        for n1 in Note.CHROMATIC_SCALE_SHARP_BASED:
            i_n2 = 0
            for n2 in Note.CHROMATIC_SCALE_FLAT_BASED:
                # print(n1, " - ", n2)
                if Note(n1) != Note(n2):
                    d = Note(n1).get_interval_in_half_tones(Note(n2))
                    expected = (i_n2 - i_n1)
                    # print(expected, " = ", d)
                    self.ut_report.assertTrue(d == expected)
                i_n2 += 1
            i_n1 += 1

    def test_get_note_name(self):
        assert Note.find_closest_note(440) == ("A3", 440)
        assert Note.find_closest_note(32.703) == ('C0', 32.70319566257483)
        assert Note.find_closest_note(16744) == ('C9', 16744.036179238312)
        assert Note.find_closest_note(31609) == ('B9', 31608.53128039195)
        assert Note.find_closest_note(32.700) == ('C0', 32.70319566257483)
        assert Note.find_closest_note(31610) == ('B9', 31608.53128039195)

    def test_note_with_octave(self):
        n = Note("C")
        assert n.name == "C"
        assert n.octave == -1
        n = Note("C6")
        assert n.name == "C"
        assert n.octave == 6
        n = Note("C#6")
        assert n.name == "C#"
        assert n.octave == 6

    def test_str_note_with_octave(self):
        n = Note("C")
        assert str(n) == "C"
        n = Note("C6")
        assert str(n) == "C6"
        n = Note("C#6")
        assert str(n) == "C#6"

    def test_neq_note_with_octave(self):
        n1 = Note("C")
        n2 = Note("C")
        assert not n1 != n2
        n1 = Note("C2")
        n2 = Note("C2")
        assert not n1 != n2
        n1 = Note("C1")
        n2 = Note("C2")
        assert n1 != n2
        n1 = Note("C1")
        n2 = Note("C")
        assert n1 != n2

    def test_eq_note_with_octave(self):
        n1 = Note("C")
        n2 = Note("C")
        assert n1 == n2
        n1 = Note("C2")
        n2 = Note("C2")
        assert n1 == n2
        n1 = Note("C1")
        n2 = Note("C2")
        assert not n1 == n2
        n1 = Note("C1")
        n2 = Note("C")
        assert not n1 == n2

    def test_transpose(self):
        n = Note("C")
        assert n.transpose(0) == "C"
        n = Note("C")
        assert n.transpose(1) == "C#"
        n = Note("C")
        assert n.transpose(-1) == "B"
        n = Note("C")
        assert n.transpose(11) == "B"
        n = Note("C")
        assert n.transpose(11+12) == "B"
        n = Note("C")
        assert n.transpose(-11) == "C#"
        n = Note("C")
        assert n.transpose(-11-12) == "C#"
        n = Note("C1")
        assert n.transpose(0) == "C1"
        n = Note("C1")
        assert n.transpose(1) == "C#1"
        n = Note("C1")
        assert n.transpose(11) == "B1"
        n = Note("C2")
        assert n.transpose(-1) == "B1"

