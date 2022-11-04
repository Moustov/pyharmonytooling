## OVERVIEW ##
Series of tools to handle harmony in music

## Links ##
* PyChord project: https://github.com/yuma-m/pychord
* Circle of Fifths: 
  * https://websemantics.uk/tools/circle-of-fifths-chord-wheel/
  * https://en.wikipedia.org/wiki/Circle_of_fifths

## Features ##

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