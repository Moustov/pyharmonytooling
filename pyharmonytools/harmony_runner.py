from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.song.text_song import TextSongWithLineForChords

song = """
Coldplay -- The Scientist

Capo 5th Fret

Standard Tuning

 

 

[Verse]

 

Em                   C                        G

Come up to meet you, tell you I'm sorry

                              Gadd2

You don't know how lovely you are

Em         C

I had to find you

               G

Tell you I need you

              Gadd2

Tell you I set you apart

Em               C

Tell me your secrets

                          G

And ask me your questions

                 Gadd2

Oh, lets go back to the start

Em             C

Running in circles

                G

Coming up tails

                Gadd2

Heads on a science apart.

 

 

[Chorus]

 

C

Nobody said it was easy

G             Gadd2

It's such a shame for us to part

C

Nobody said it was easy

G               Gadd2                  D

No one ever said it would be this hard

 

Oh, take me back to the start.

 

G - C - G - Gadd2

 

 

[Verse]

 

Em            C

I was just guessing

                        G

At numbers and figures

                Gadd2

Pulling the puzzles apart

 

Em               C

Questions of science

                 G

Science and progress

                      Gadd2

Do not speak as loud as my heart

 

Em             C

Tell me you love me

                      G

Come back and haunt me

              Gadd2

Oh, and I rush to the start

Em            C

Running in circles

                 G

Chasing our tails

             Gadd2

Coming back as we are

 

 

[Chorus]

 

C

Nobody said it was easy

G                  Gadd2

Oh it's such a shame for us to part

C

Nobody said it was easy

G               Gadd2                  D

No one ever said it would be so hard

                                      G - C - G - Gadd2

I'm going back to the start

 

Em - C - G - Gadd2 x5

"""
_HarmonyLogger.outcome_level_of_detail = _HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
the_song.generate_degrees_from_chord_progression()
print("Deg:", the_song.degrees)
rc = the_song.get_remarquable_cadences()
print("Remarkable cadences:", rc)

print(the_song.transpose(number_half_tone = -5))
