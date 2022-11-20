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
        assert Note("C#") == Note("Db")
        assert Note("C#") == "Db"
        # limits
        assert Note("A#") == "Gb"   # fails
        assert Note("G#") == "Ab"   # fails
