from unittest import TestCase

from pychord import Chord

from src.harmony.circle_of_5th import CircleOf5th, CircleOf5thNaturalMajor


class Test(TestCase):
    def test_guess_tone_and_mode_C(self):
        song = """
        C Dm Em F G Am Bdim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        assert compliance_level_max[0] == 1.0
        assert compliance_level_max[1] == 'C'
        assert compliance_level_max[2] == "Natural Major"


    def test_guess_tone_and_mode_Bb(self):
        song = """
        Bb, Cm, Dm, E, F, Gm, Adim
        """
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        assert compliance_level_max[0] == 1.0
        assert compliance_level_max[1] == 'Bb'
        assert compliance_level_max[2] == "Natural Major"

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
        cof = CircleOf5th()
        cp = cof.digest_song(song)
        compliance_level_max = cof.guess_tone_and_mode(cp)
        print(compliance_level_max)
        assert compliance_level_max[0] == 1.0
        assert compliance_level_max[1] == 'A'
        assert compliance_level_max[2] == "Natural Major"


    def test_get_chord_possible_qualities(self):
        cof = CircleOf5thNaturalMajor()
        tones = cof.generate_circle_of_fifths()
        for tone in tones:
            for chord_tone in tones[tone]:
                possible_chord_qualities = cof.get_chord_names_possible_qualities(chord_tone)
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
        cof = CircleOf5thNaturalMajor()
        cp = cof.digest_song(song)

        tone = cof.generate_circle_of_fifths()["C"]
        borrowed_chords = cof.get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        assert (len(borrowed_chords) == 0)

    def test_get_borrowed_chords_Cm(self):
        song = """
                C Dm Em F G Am Bdim Cm
                """
        cof = CircleOf5thNaturalMajor()
        cp = cof.digest_song(song)
        tone = cof.generate_circle_of_fifths()["C"]
        borrowed_chords = cof.get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
        assert (borrowed_chords == {"Cm": True})
