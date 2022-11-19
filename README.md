
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
    from src.displays.console import HarmonyLogger
    from src.harmony.circle_of_5th import CircleOf5th, CircleOf5thNaturalMajor

    HarmonyLogger.outcome_level_of_detail = HarmonyLogger.LOD_NONE
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

ouput:

    [1.0, 'A', 'Natural Major', ['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab', 'Ab']]

#### Guess borrowed chords in a song from a tone point of view
    song = """
                C Dm Em F G Am Bdim Cm
                """
    cof = CircleOf5thNaturalMajor()
    cp = cof.digest_song(song)
    tone = cof.generate_circle_of_fifths()["C"]
    borrowed_chords = cof.get_borrowed_chords(tone, cp)
    print("   Borrowed chords:", borrowed_chords.keys())
ouput:

    Borrowed chords: dict_keys(['Cm'])

#### Find substitutes from a chord
    from pychord import Chord 
    from src.harmony.circle_of_5th import CircleOf5th

    cof = CircleOf5th()
    chord = "G6"
    substitutes = cof.find_substitutes(Chord(chord))
    print("substitutes from :", chord, substitutes)
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
    from src.guitar_neck.fingering import Fingering

    outcome_level_of_detail = LOD_ALL
    fng = Fingering()
    f = fng.get_fingering_from_chord(Chord("C"))
    print(f)
output:

    [[0, 3, 2, 0, 1, 0], [0, 3, 2, 0, 1, 3], [3, 3, 2, 0, 1, 0], ... ]

### Song Processing
#### Song search & processing tools on Ultimate Guitar through Google.com
You may search and handle song lyrics & tabs

    from src.song.song import UltimateGuitarSong
    from src.song.ultimate_guitar_search import UltimateGuitarSearch
    
    ug_engine = UltimateGuitarSearch()
    query = "D Dm A"
    urls = ug_engine.search(query, 20)
    song = UltimateGuitarSong()
    for link in urls:
        print("===================================")
        song.extract_song_from_url(link)
        print(song.get_string())

This piece of code will display 20 songs matching the query (songs holding the "D/Dm/A" cadence)

Output:

    ===================================
    Title: AUTREFOIS
    Artist: Pink Martini
    [tab][ch]A[/ch]                                     [ch]D[/ch]\r\nJ'ai ecris des mots doux а toutes les filles de France[/tab]\r\n
    [tab][ch]Dm[/ch]                    [ch]A[/ch]\r\nJ'espere qu'elles y repondent[/tab]\r\n
    [tab][ch]A[/ch]                  [ch]D[/ch]           [ch]Dm[/ch]               [ch]A[/ch]\r\nJ'ai jure que je serai content avant la fin de l'annee[/tab]\r\n
    [tab][ch]A[/ch]                                     [ch]D[/ch]\r\nJ'ai ecris des mots doux а toutes les filles de France[/tab]\r\n
    [tab][ch]Dm[/ch]                    [ch]A[/ch]\r\nChaque jour et chaque nuit[/tab]\r\n
    ...

#### Song processing tools on simple text song
        from pychord import Chord 
        from src.song.text_song import TextSongWithLineForChords

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
        the_song = TextSongWithLineForChords()
        the_song.digest(song)
        print(the_song.chords_sequence)
output: 

    [<Chord: A>, <Chord: E>, <Chord: E>, <Chord: A>, <Chord: A7>, <Chord: D>, <Chord: A>, <Chord: E>, <Chord: A>]

# Release Notes
* 19/NOV/22
  * starting API to ultimate-guitar.com
  * querying UG through google.com to retrieve pattern matching over possibilities found in UG
  * circle of 5th extended to Natural/Melodic/Harmonic minors
* 12/NOV/22: 
  * bugs when finding chord fingering on a guitar on vertical fingering such a barres

# Additional links
* https://codepen.io/2kool2/pen/bmVxpZ
* https://github.com/victorfontes/python-ultimate-guitar