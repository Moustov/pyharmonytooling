from unittest import TestCase

from pyharmonytools.harmony.note import Note


class TestNote(TestCase):

    def test_weird_notes(self):
        assert Note("Cb") != Note("D")
        assert Note("Cb") == Note("B")
        assert Note("Fb") == Note("E")
        assert Note("B#") == Note("C")
        assert Note("E#") == Note("F")

    def test_notes_equals(self):
        # canonics
        assert Note("C") == Note("C")
        assert Note("C") != Note("B")
        assert Note("C#") != Note("D")
        # tempered equivalences
        assert Note("A#") == "Bb"
        assert Note("C#") == Note("Db")
        assert Note("C#") == "Db"
        # limits
        assert Note("G#") == "Ab"

    def test_all_equals(self):
        # todo add Note.CHROMATIC_SCALE_WEIRD_NOTES
        for n1, n2 in zip(Note.CHROMATIC_SCALE_SHARP_BASED, Note.CHROMATIC_SCALE_FLAT_BASED):
            print(n1, "==", n2)
            assert Note(n1) == Note(n2)
        for n1 in Note.CHROMATIC_SCALE_SHARP_BASED:
            for n2 in Note.CHROMATIC_SCALE_FLAT_BASED:
                print(n1, "!=", n2)
                if Note(n1) != Note(n2):
                    assert Note(n1) != Note(n2)

    def test_get_interval_c_e(self):
        c = Note("C")
        e = Note("E")
        res = c.get_interval_in_half_tones(e)
        assert res == 4

    def test_get_interval_e_c(self):
        c = Note("C")
        e = Note("E")
        res = e.get_interval_in_half_tones(c)
        assert res == -4

    def test_get_interval_c_g(self):
        c = Note("C")
        g = Note("G")
        res = c.get_interval_in_half_tones(g)
        assert res == 7

    def test_get_interval_cs_es(self):
        cs = Note("C#")
        es = Note("E#") # the get_interval() should translate this into F
        res = cs.get_interval_in_half_tones(es)
        assert res == 4

    def test_get_interval_gs_ab(self):
        gs = Note("G#")
        ab = Note("Ab") # the get_interval() should translate this into F
        res = gs.get_interval_in_half_tones(ab)
        assert res == 0

    def test_get_interval_ab_gs(self):
        gs = Note("G#")
        ab = Note("Ab")  # the get_interval() should translate this into F
        res = gs.get_interval_in_half_tones(ab)
        assert res == 0

    def test_all_note_index(self):
        index = 0
        for n in Note.CHROMATIC_SCALE_FLAT_BASED:
            print(n)
            assert Note.get_index(n) == index
            index += 1
        index = 0
        for n in Note.CHROMATIC_SCALE_SHARP_BASED:
            print(n)
            assert Note.get_index(n) == index
            index += 1
        index = 0
        for n in Note.CHROMATIC_SCALE_WEIRD_NOTES:
            print(n)
            assert Note.get_index(n) == index
            index += 1

    def test_get_all_interval(self):
        # todo add Note.CHROMATIC_SCALE_WEIRD_NOTES
        for n1, n2 in zip(Note.CHROMATIC_SCALE_SHARP_BASED, Note.CHROMATIC_SCALE_FLAT_BASED):
            print(n1, " - ", n2)
            d = Note(n1).get_interval_in_half_tones(Note(n2))
            print(" = ", d)
            assert d == 0
        i_n1 = 0
        for n1 in Note.CHROMATIC_SCALE_SHARP_BASED:
            i_n2 = 0
            for n2 in Note.CHROMATIC_SCALE_FLAT_BASED:
                # print(n1, " - ", n2)
                if Note(n1) != Note(n2):
                    d = Note(n1).get_interval_in_half_tones(Note(n2))
                    expected = (i_n2 - i_n1)
                    # print(expected, " = ", d)
                    assert d == expected
                i_n2 += 1
            i_n1 += 1

