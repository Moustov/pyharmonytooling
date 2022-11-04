from unittest import TestCase

from pychord import Chord

from src.harmony.harmony_tools import digest_song, guess_tone_and_mode, get_chord_possible_qualities, \
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

    def test_get_chord_possible_qualities(self):
        for tone in circle_of_fifths_natural_majors:
            for chord_tone in circle_of_fifths_natural_majors[tone]:
                possible_chord_qualities = get_chord_names_possible_qualities(chord_tone)
                for c in possible_chord_qualities:
                    try:
                        a_chord = Chord(c)
                    except Exception as err:
                        print(c, "cannot be turned into a Chord", err)
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
        assert (borrowed_chords == [])

    def test_get_borrowed_chords_C(self):
        song = """
                C Dm Em F G Am Bdim Cm
                """
        cp = digest_song(song)
        tone = circle_of_fifths_natural_majors["C"]
        borrowed_chords = get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        assert (borrowed_chords == {"Cm": True})
