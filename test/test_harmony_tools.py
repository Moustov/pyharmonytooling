from unittest import TestCase

from pychord import Chord

from src.harmony.harmony_tools import digest_song, guess_tone_and_mode, \
    circle_of_fifths_natural_majors, get_chord_names_possible_qualities, get_borrowed_chords


class Test(TestCase):
    def test_guess_tone_and_mode_C(self):
        song = """
        C Dm Em F G Am Bdim
        """
        cp = digest_song(song)
        compliance_level_max = guess_tone_and_mode(cp)
        assert(compliance_level_max == [1.0, 'C'])

    def test_guess_tone_and_mode_Bb(self):
        song = """
        Bb, Cm, Dm, E, F, Gm, Adim
        """
        cp = digest_song(song)
        compliance_level_max = guess_tone_and_mode(cp)
        assert(compliance_level_max == [1.0, 'Bb'])

    def test_guess_tone_and_mode_happy_birthday_chords(self):
        song = """
                    A           E
            Happy Birthday to you
                  E           A
            Happy Birthday to you
                  A7            D
            Happy Birthday dear (name)
                  A        E    A
            Happy Birthday to you
        """
        cp = digest_song(song)
        compliance_level_max = guess_tone_and_mode(cp)
        print(compliance_level_max)
        assert(compliance_level_max == [1.0, 'A'])

    def test_get_chord_possible_qualities(self):
        for tone in circle_of_fifths_natural_majors:
            for chord_tone in circle_of_fifths_natural_majors[tone]:
                possible_chord_qualities = get_chord_names_possible_qualities(chord_tone)
                c = Chord(tone+"m")
                tc = Chord(chord_tone)
                if c in possible_chord_qualities and tc.quality.quality == "":
                    print(c, "Minor chord cannot be a possible Major chord")
                    self.fail()
        assert (True)

    def test_get_borrowed_chords_C(self):
        song = """
                C Dm Em F G Am Bdim
                """
        cp = digest_song(song)
        tone = circle_of_fifths_natural_majors["C"]
        borrowed_chords = get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        assert (len(borrowed_chords) == 0)

    def test_get_borrowed_chords_Cm(self):
        song = """
                C Dm Em F G Am Bdim Cm
                """
        cp = digest_song(song)
        tone = circle_of_fifths_natural_majors["C"]
        borrowed_chords = get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        assert (borrowed_chords == {"Cm": True})
