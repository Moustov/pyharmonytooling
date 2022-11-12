
<img src="circle_of_5th.png" width="200" alt="Circle of 5th">

## OVERVIEW ##
Series of tools to handle harmony in music

## Links ##
* PyChord project: https://github.com/yuma-m/pychord
* Circle of Fifths: 
  * https://websemantics.uk/tools/circle-of-fifths-chord-wheel/
  * https://en.wikipedia.org/wiki/Circle_of_fifths

## Features ##
### Features on Harmony
#### Guess the tone & mode of a song"
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

#### Guess borrowed chords in a song from a tone point of view
    song = """
            C Dm Em F G Am Bdim Cm
            """
    cp = digest_song(song)
    tone = circle_of_fifths_natural_majors["C"]
    borrowed_chords = get_borrowed_chords(tone, cp)
    print("Borrowed chords:", borrowed_chords.keys())
ouput:

    Borrowed chords: dict_keys(['Cm'])

#### Find substitutes from a chord
    from pychord import Chord 
    from src.harmony.harmony_tools import LOD_ALL, find_substitutes

    outcome_level_of_detail = LOD_ALL
    chord = "G6"
    print("substitutes from :", chord, find_substitutes(Chord(chord)))
ouput:

    Number of existing chords: 5772
    Em7/9 == G6
    ['G', 'B', 'D', 'E'] vs ['G', 'B', 'D', 'E']
    Em7/13 == G6
    ['G', 'B', 'D', 'E'] vs ['G', 'B', 'D', 'E']
    Em7/9/G == G6
    ['G', 'B', 'D', 'E'] vs ['G', 'B', 'D', 'E']
    Em7/13/G == G6
    ['G', 'B', 'D', 'E'] vs ['G', 'B', 'D', 'E']
    G6/9/G == G6
    ['G', 'B', 'D', 'E'] vs ['G', 'B', 'D', 'E']
    substitutes from : G6 [<Chord: Em7/9>, <Chord: Em7/13>, <Chord: Em7/9/G>, <Chord: Em7/13/G>, <Chord: G6/9/G>]

### Guitar tools
#### Find chord fingering on a guitar

    outcome_level_of_detail = LOD_ALL
    f = get_fingering_from_chord(Chord("C"))
    print(f)
output:

    [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3], [3, 3, 2, 0, 1, 0], [3, 3, 2, 0, 1, 3], [3, 3, 2, 5, 1, 3], [3, 3, 2, 5, 5, 3], [3, 3, 5, 5, 1, 3], [3, 3, 5, 5, 5, 3], [3, 7, 5, 5, 5, 3], [8, 7, 5, 5, 5, 8], [8, 7, 5, 5, 8, 8], [8, 7, 5, 9, 5, 8], [8, 7, 5, 9, 8, 8], [8, 7, 10, 9, 8, 8], [8, 10, 10, 9, 8, 8], [8, 10, 10, 9, 8, 12], [8, 10, 10, 12, 8, 8], [8, 10, 10, 12, 8, 12], [12, 10, 10, 9, 8, 8], [12, 10, 10, 9, 8, 12], [12, 10, 10, 12, 8, 8], [12, 10, 10, 12, 8, 12]]
