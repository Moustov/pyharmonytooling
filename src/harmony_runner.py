from src.harmony.harmony_tools import digest_song, guess_tone_and_mode, circle_of_fifths_natural_majors, \
    get_borrowed_chords

song = """
      DANCING QUEEN CHORDS


INTRO:   G   C/G    G  (2x )       D/F#   Em

D               B
You can dance, you can jive, 
Em          Em7          A
having the time of your life, ooh
C	        D		               
See that girl, watch that scene,   
             G           C/G
dig in the dancing queen

G	                         C/G
Friday night and the lights are low        
G                            Em
Looking out for the place to go
D		                  D/F#
Where they play the right music, getting in the swing 
		        Em   D, Em, Em	
You come  to look for a king

G	               C/G                 			        
Anybody could be that guy      
G                               Em
Night is young and the musics high
D	                   D/F#	 
With a bit of rock music, everything is fine 
               Em              D,Em,Em
Youre in the mood for a dance
              Am            D
And when you get the chance...

CHORUS:
D	     G 	                   
You are the dancing queen, 
C/G                     G       C/G                
young and sweet, only seventeen
G	   	                        	          
Dancing queen, 
C/G                      G         D/F#  Em     
feel the beat from the tambourine  oh   yeah

D	        B	
You can dance, you can jive,   
Em           Em7         A
having the time of your life, Ooh
C/G	        D	  	                             
See that girl, watch that scene, 
            G
dig in the dancing queen  
"""
cp = digest_song(song)
compliance_level_max = guess_tone_and_mode(cp)
print(compliance_level_max)

tone = circle_of_fifths_natural_majors[compliance_level_max[1]]
borrowed_chords = get_borrowed_chords(tone, cp)
print("   Borrowed chords:", borrowed_chords.keys())

