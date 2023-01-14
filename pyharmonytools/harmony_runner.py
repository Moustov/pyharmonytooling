from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.song.text_song import TextSongWithLineForChords

song = """
Intro: E  D  C#m7  F#  F#m7  A  E  A-E

 

E               D                   C#m7  F#             F#m7

 These are the days that I've been missing  give me the taste

             A             E  A-E               D

give me the joy of summer wine   These are the days that bring

     C#m7  F#             F#m7            A              E

you meaning  I feel the stillness of the sun and I feel fine

 

A-C#7                                      F#m7

     Sometimes when the nights are closing early

B                                E

 I remember you and I start to smile

C#7                                  F#m7

   even though now you don't want to know me

          B

I get on by, and I go the extra mile

 

A-E               D                  C#m7  F#             F#m7

   These are the times for love and meaning  Eyes of the heart,

         A             E   A-E               D                C#m7

melted away in firmer light   these are the days of endless dreaming

F#             F#m7            A                   E

  Troubles of life, floating away like a bird in flight

 

E6               E7  E6               E  E6      E7          E6  E  E6

  These are the days   These are the days  These are the days

 

Solo: (E  D  C#m7  F#  F#m7  A  E  A-E)  x2

 

C#7                                          F#m7  B

   I thought you said our love would last forever   believing that the tears

      E           C#7                                      F#m7

would end for good   I told you that we'd get through any weather maybe that

 B                                           E               D

didn't work out, but we did the best we could these are the days that I've

      C#m7  F#             F#m7              A             E  A-E

been missing  give me the taste give me the joy of summer wine   these are the

 D                   C#m7  F#                               F#m7            E  E6  E

days that bring you meaning  I feel the stillness of the sun    and I feel fine



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
