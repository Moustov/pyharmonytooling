from src.harmony.harmony_tools import digest_song, guess_tone_and_mode

song = """
[Verse 1]
D
I wanna run
I want to hide
I wanna tear down the walls
                G
That hold me inside
               Bm
I wanna reach out
               A
And touch the flame
            C
Where the streets have no name
 
[Verse 2]
          D
I wanna feel sunlight on my face
I see the dust-cloud disappear
            G
Without a trace
             Bm                       A
I wanna take shelter from the poison rain
            C
Where the streets have no name
 
[Chorus]
                           D
Where the streets have no name
                         G
We're still building and burning down love
Burning down love
 
[Post-Chorus]
           Bm
And when I go there
           A
I go there with you
              D
It's all I can do
 
[Verse 3]
              D
The city's a flood and our love turns to rust
We're beaten and blown by the wind
             G
Trampled in dust
                Bm
I'll show you a place
                  A
High on a desert plain
           C
Where the streets have no name
 
[Chorus]
                         D
Where the streets have no name
                          G
We're still building and burning down love
Burning down love
 
[Post-Chorus]
           Bm
And when I go there
            A
I go there with you
               D
It's all I can do
 
[Verse 4]
Our love turns to rust
                 G
We're beaten and blown by the wind
Blown by the wind
          D
Oh, and I see love
See our love turn to rust
                 G
We're beaten and blown by the wind
Blown by the wind
 
[Post-Chorus]
           Bm
Oh, when I go there
            A
I go there with you
               D
It's all I can do
"""
cp = digest_song(song)
compliance_level_max = guess_tone_and_mode(cp)
print(compliance_level_max)

