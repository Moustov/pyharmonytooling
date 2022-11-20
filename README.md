
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

#### Song search from a cadence
Searching for songs in the 12 tones from a cadence

        from src.harmony.circle_of_5th import CircleOf5thNaturalMajor
        from src.song.ultimate_guitar_search import UltimateGuitarSearch
        
        ugs = UltimateGuitarSearch()
        cof_maj = CircleOf5thNaturalMajor()
        songs = ugs.search_songs_from_cadence("ii7-V7-Imaj7", cof_maj, 5)
        print(songs)
output:
        {'Bm7 E7 Amaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/1726600', 
                'https://tabs.ultimate-guitar.com/tab/henri-salvador/jardin-dhiver-chords-2202243', 
                'https://tabs.ultimate-guitar.com/tab/2330957', 
                'https://tabs.ultimate-guitar.com/tab/slimane/a-fleur-de-toi-chords-1873948', 
                'https://tabs.ultimate-guitar.com/tab/1707559'],
        'Cm7 F7 A#maj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/louis-armstrong/a-kiss-to-build-a-dream-on-chords-923726', 
                'https://tabs.ultimate-guitar.com/tab/amy-winehouse/mr-magic-chords-1828391', 
                'https://tabs.ultimate-guitar.com/tab/amy-winehouse/mr-magic-chords-1828391', 
                'https://tabs.ultimate-guitar.com/tab/stevie-wonder/lately-chords-173491', 
                'https://tabs.ultimate-guitar.com/tab/louis-armstrong/a-kiss-to-build-a-dream-on-chords-923726'], 
        'C#m7 F#7 Bmaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/jvke/this-is-what-falling-in-love-feels-like-chords-3871874', 
                'https://tabs.ultimate-guitar.com/tab/jvke/this-is-what-falling-in-love-feels-like-chords-3871874', 
                'https://tabs.ultimate-guitar.com/tab/jvke/this-is-what-falling-in-love-feels-like-chords-3871874', 
                'https://tabs.ultimate-guitar.com/tab/jvke/this-is-what-falling-in-love-feels-like-chords-3871874', 
                'https://tabs.ultimate-guitar.com/tab/jvke/this-is-what-falling-in-love-feels-like-chords-3871874'], 
        'Dm7 G7 Cmaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/frank-sinatra/fly-me-to-the-moon-chords-1193296', 
                'https://tabs.ultimate-guitar.com/tab/frank-sinatra/fly-me-to-the-moon-chords-1193296', 
                'https://tabs.ultimate-guitar.com/tab/grover-washington-jr-/just-the-two-of-us-chords-1095786', 
                'https://tabs.ultimate-guitar.com/tab/michel-fugain/une-belle-histoire-chords-391387', 
                'https://tabs.ultimate-guitar.com/tab/michel-fugain/une-belle-histoire-chords-391387'], 
        'D#m7 G#7 C#maj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/941025', 
                'https://tabs.ultimate-guitar.com/tab/941025', 
                'https://tabs.ultimate-guitar.com/tab/941025', 
                'https://tabs.ultimate-guitar.com/tab/941025', 
                'https://tabs.ultimate-guitar.com/tab/941025'], 
        'Em7 A7 Dmaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/eric-clapton/autumn-leaves-chords-2502690', 
                https://tabs.ultimate-guitar.com/tab/eric-clapton/autumn-leaves-chords-2502690', 
                'https://tabs.ultimate-guitar.com/tab/eric-clapton/autumn-leaves-chords-2502690', 
                https://tabs.ultimate-guitar.com/tab/eric-clapton/autumn-leaves-chords-2502690', 
                'https://tabs.ultimate-guitar.com/tab/frank-sinatra/the-way-you-look-tonight-ukulele-1485850'], 
        'Fm7 A#7 D#maj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/michael-jackson/i-just-cant-stop-loving-you-chords-967366', 
                'https://tabs.ultimate-guitar.com/tab/michael-jackson/i-just-cant-stop-loving-you-chords-967366', 
                'https://tabs.ultimate-guitar.com/tab/michael-jackson/i-just-cant-stop-loving-you-chords-967366', 
                'https://tabs.ultimate-guitar.com/tab/michael-jackson/i-just-cant-stop-loving-you-chords-967366', 
                'https://tabs.ultimate-guitar.com/tab/frank-sinatra/the-way-you-look-tonight-chords-1771608'], 
        F#m7 B7 Emaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/3709742', 
                'https://tabs.ultimate-guitar.com/tab/misc-soundtrack/la-la-land-audition-the-fools-who-dream-chords-1909336', 
                'https://tabs.ultimate-guitar.com/tab/julie-london/cry-me-a-river-chords-1499105', 
                'https://tabs.ultimate-guitar.com/tab/h-e-r-/wrong-places-chords-3119678', 
                'https://tabs.ultimate-guitar.com/tab/h-e-r-/wrong-places-chords-3119678'], 
        'Gm7 C7 Fmaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/yves-montand/les-feuilles-mortes-chords-2576898', 
                'https://tabs.ultimate-guitar.com/tab/glen-campbell/by-the-time-i-get-to-phoenix-chords-2129751', 
                'https://tabs.ultimate-guitar.com/tab/yves-montand/les-feuilles-mortes-chords-2576898', 
                'https://tabs.ultimate-guitar.com/tab/glen-campbell/by-the-time-i-get-to-phoenix-chords-2129751', 
                'https://tabs.ultimate-guitar.com/tab/glen-campbell/by-the-time-i-get-to-phoenix-chords-2129751'], 
        'G#m7 C#7 F#maj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/misc-soundtrack/la-la-land-audition-the-fools-who-dream-chords-1909336', 
                'https://tabs.ultimate-guitar.com/tab/tyler-the-creator/boredom-chords-2785219', 
                'https://tabs.ultimate-guitar.com/tab/tyler-the-creator/boredom-chords-2785219', 
                'https://tabs.ultimate-guitar.com/tab/tyler-the-creator/boredom-chords-2785219', 
                'https://tabs.ultimate-guitar.com/tab/yves-montand/les-feuilles-mortes-chords-2576898'], 
        'Am7 D7 Gmaj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/billy-joel/just-the-way-you-are-chords-1404186', 
                'https://tabs.ultimate-guitar.com/tab/laufey/falling-behind-chords-4307414', 
                'https://tabs.ultimate-guitar.com/tab/billy-joel/just-the-way-you-are-chords-1404186', 
                'https://tabs.ultimate-guitar.com/tab/billy-joel/just-the-way-you-are-chords-1404186', 
                'https://tabs.ultimate-guitar.com/tab/john-mayer/new-light-chords-3180788'], 
        'A#m7 D#7 G#maj7 ': 
                ['https://tabs.ultimate-guitar.com/tab/george-benson/give-me-the-night-chords-61898', 
                'https://tabs.ultimate-guitar.com/tab/george-benson/give-me-the-night-chords-61898', 
                'https://tabs.ultimate-guitar.com/tab/george-benson/give-me-the-night-chords-61898', 
                'https://tabs.ultimate-guitar.com/tab/tyler-the-creator/boredom-chords-2785219', 
                'https://tabs.ultimate-guitar.com/tab/tyler-the-creator/boredom-chords-2785219']
                }


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
* 20/NOV/22
  * accurate song search (param added)
  * find songs that match a cadence in degrees
* 19/NOV/22
  * starting API to ultimate-guitar.com
  * querying UG through google.com to retrieve pattern matching over possibilities found in UG
  * circle of 5th extended to Natural/Melodic/Harmonic minors
* 12/NOV/22: 
  * bugs when finding chord fingering on a guitar on vertical fingering such a barres

# Additional links
* https://codepen.io/2kool2/pen/bmVxpZ
* https://github.com/victorfontes/python-ultimate-guitar
* 🇫🇷 https://www.youtube.com/@gradusadparnassumfr