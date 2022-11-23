from unittest import TestCase

from src.harmony.note import Note


class TestNote(TestCase):
    def test_notes_equals(self):
        # canonics
        assert Note("C") == Note("C")
        assert Note("C") != Note("B")
        assert Note("C#") != Note("D")
        assert Note("Cb") != Note("D")
        # tempered equivalences
        assert Note("A#") == "Bb"
        assert Note("C#") == Note("Db")
        assert Note("C#") == "Db"
        # limits
        assert Note("G#") == "Ab"

    def test_get_interval_c_e(self):
        c = Note("C")
        e = Note("E")
        assert c.get_interval_in_half_tones(e) == 4

    def test_get_interval_e_c(self):
        c = Note("C")
        e = Note("E")
        assert e.get_interval_in_half_tones(c) == -8

    def test_get_interval_c_g(self):
        c = Note("C")
        g = Note("G")
        assert c.get_interval_in_half_tones(g) == 7

    def test_get_interval_cs_es(self):
        cs = Note("C#")
        es = Note("E#") # the get_interval() should translate this into F
        assert cs.get_interval_in_half_tones(es) == 4

    def test_get_interval_gs_ab(self):
        gs = Note("G#")
        ab = Note("Ab") # the get_interval() should translate this into F
        assert gs.get_interval_in_half_tones(ab) == 0

    def test_get_interval_ab_gs(self):
        gs = Note("G#")
        ab = Note("Ab") # the get_interval() should translate this into F
        assert ab.get_interval_in_half_tones(gs) == 0
