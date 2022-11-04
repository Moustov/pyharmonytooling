## OVERVIEW ##
Series of tools to handle harmony in music

## Links ##
* PyChord project: https://github.com/yuma-m/pychord
* Circle of Fifths: 
  * https://websemantics.uk/tools/circle-of-fifths-chord-wheel/
  * https://en.wikipedia.org/wiki/Circle_of_fifths

## Features ##
### Guess the tone & mode of a song" ###
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

ouput:

    Compliance: [1.0, 'A']

### Guess borrowed chords in a song from a tone point of view ###
    song = """
            C Dm Em F G Am Bdim Cm
            """
    cp = digest_song(song)
    tone = circle_of_fifths_natural_majors["C"]
    borrowed_chords = get_borrowed_chords(tone, cp)
    print("Borrowed chords:", borrowed_chords.keys())
ouput:

    Borrowed chords: dict_keys(['Cm'])