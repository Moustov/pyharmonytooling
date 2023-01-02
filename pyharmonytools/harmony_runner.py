from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.song.text_song import TextSongWithLineForChords

song = """
       Dm
Hevenu Sha- lom halerem
       Gm
Hevenu Sha- lom halerem
       A7       Gm
Hevenu Sha- lom ha- lerem
       A7        A7        A7           Dm
Hevenu Sha- lom, Sha- lom, Sha- lom halerem
 
[Verse 1]
             Dm
Nous vous a- nnoncons la paix,
             Gm
Nous vous a- nnonçons la paix,
             A7            Dm
Nous vous a- nnon- çons la paix
                    A7       A7       A7           Dm
Nous vous annonçons la paix, la paix, la paix en Jésus
 
[Verse 2]
             Dm
Nous vous a- nnoncons la joie,
             Gm
Nous vous a- nnonçons la joie,
             A7            Dm
Nous vous a- nnon- çons la joie
                    A7       A7       A7           Dm
Nous vous annonçons la joie, la joie, la joie en Jésus-Christ
 
[Verse 3]
             Dm
Nous vous a- nnoncons l'amour,
             Gm
Nous vous a- nnonçons l'amour,
             A7           Dm
Nous vous a- nnon- çons l'amour
                      A7       A7       A7       Dm
Nous vous annonçons l'amour, l'amour, l'amour en Jésus
 
[Verse 4]
             Dm
Nous vous a- nnoncons la paix,
             Gm
Nous vous a- nnonçons la joie,
             A7           Dm
Nous vous a- nnon- çons l'amour
                    A7       A7         A7       Dm
Nous vous annonçons la paix, la joie, l'amour en Jésus        """
_HarmonyLogger.outcome_level_of_detail = _HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
