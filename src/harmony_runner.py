from src.harmony.harmony_tools import digest_song, guess_tone_and_mode, circle_of_fifths_natural_majors, \
    get_borrowed_chords, LOD_NONE

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
outcome_level_of_detail = LOD_NONE
cp = digest_song(song)
compliance_level_max = guess_tone_and_mode(cp)
print("Compliance:", compliance_level_max)

tone = circle_of_fifths_natural_majors[compliance_level_max[1]]
borrowed_chords = get_borrowed_chords(tone, cp)
print("Borrowed chords:", borrowed_chords.keys())

