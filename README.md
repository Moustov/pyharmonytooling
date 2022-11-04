## OVERVIEW ##
Series of tools to handle harmony in music

## Links ##
* PyChord project: https://github.com/yuma-m/pychord
* Circle of Fifths: 
  * https://websemantics.uk/tools/circle-of-fifths-chord-wheel/
  * https://en.wikipedia.org/wiki/Circle_of_fifths

## Features ##
### Guess the tone & mode of a song" ###
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
    print("Compliance:", compliance_level_max)
ouput:

    Check tone C in Natural Major
      Check C
      Check Dm
      Check Em
      Check F
      Check G
      Check Am
      Check Bdim
    C 0.0 %
    Check tone G in Natural Major
      Check G
      Check Am
      Check Bm
      Check C
      Check D
        D found in song
      Check Em
      Check F#dim
    G 14.285714285714285 %
    Check tone D in Natural Major
      Check D
        D found in song
      Check Em
      Check F#m
      Check G
      Check A
        A found in song
        A7 found in song
      Check Bm
      Check C#dim
    D 42.857142857142854 %
    Check tone A in Natural Major
      Check A
        A found in song
        A7 found in song
      Check Bm
      Check C#m
      Check D
        D found in song
      Check E
        E found in song
      Check Fm
      Check G#dim
    A 100.0 %
    Check tone E in Natural Major
      Check E
        E found in song
      Check F#m
      Check G#m
      Check A
        A found in song
        A7 found in song
      Check B
      Check C#m
      Check D#dim
    E 42.857142857142854 %
    Check tone B in Natural Major
      Check B
      Check C#m
      Check D#m
      Check E
        E found in song
      Check F#
      Check G#m
      Check A#dim
    B 14.285714285714285 %
    Check tone F# in Natural Major
      Check F#
      Check G#m
      Check Abm
      Check Bb
      Check C#
      Check D#m
      Check Fdim
    F# 0.0 %
    Check tone Db in Natural Major
      Check Db
      Check Ebm
      Check F#m
      Check G#
      Check Ab
      Check Bbm
      Check C#dim
    Db 0.0 %
    Check tone Ab in Natural Major
      Check Ab
      Check Bbm
      Check Cm
      Check Db
      Check Eb
      Check Fm
      Check Gdim
    Ab 0.0 %
    Check tone Eb in Natural Major
      Check Eb
      Check Fm
      Check Gm
      Check Ab
      Check Bb
      Check Cm
      Check Ddim
    Eb 0.0 %
    Check tone Bb in Natural Major
      Check Bb
      Check Cm
      Check Dm
      Check Eb
      Check F
      Check Gm
      Check Adim
    Bb 0.0 %
    Check tone F in Natural Major
      Check F
      Check Gm
      Check Am
      Check Bb
      Check C
      Check Dm 
      Check Edim
    F 0.0 %
    Compliance: [1.0, 'A']

### Guess borrowed chords in a song from a tone point of view ###
    song = """
            C Dm Em F G Am Bdim Cm
            """
    cp = digest_song(song)
    tone = circle_of_fifths_natural_majors["C"]
    borrowed_chords = get_borrowed_chords(tone, cp)
    print("   Borrowed chords:", borrowed_chords.keys())
ouput:

    Borrowed chords: dict_keys(['Cm'])