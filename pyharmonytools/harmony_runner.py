from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.song.text_song import TextSongWithLineForChords

song = """
[Verse]
A          G
Tough, you think you've got the stuff
       F#m            D
You're telling me and anyone
       A
You're hard enough
    A
You don't have to put up a fight
    G
You don't have to always be right
F#m                     D
Let me take some of the punches
    A
For you tonight
  
[Verse]
[F -> C -> Dm]
I know that we don't talk
[F -> C -> Am]
I'm sick of it all
[F -> C -> Dm]         A
Can you hear me when I Sing,
       F#m
you're the reason I sing
D                 E       A
You're the reason why the opera is in me
 
[Pre Chorus]
      D
Yeah, hey now
                     A
Still got to let you know
                             F#m
A house still doesn't make a home
                     D
Don't leave me here alone
 
[Chorus]
         F#m                       E
And it's you when I look in the mirror
         D                             D
And it's you that makes it hard to let go
F#m                 E               D
Sometimes you can't make it on your own
F#m                 E
Sometimes you can't make it
             D
The best you can do is to fake it
F#m                 E        D
Sometimes you can't make it on your own
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
