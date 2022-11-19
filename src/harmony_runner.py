from src.output.console import HarmonyLogger
from src.song.text_song import TextSongWithLineForChords

song = """
  Dm                                C         Dm
À ceux qui ont toujours voulu sans jamais obtenir
  Dm                             C            Dm
À tous ceux qui ont espéré sans jamais voir venir
  F                                  Eb
À tous les efforts sans couronne aux oubliés du bal
   Dm
Je veux offrir le réconfort
 N.C.
D'un morceau d'Emmental
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
      Dm                              C           Dm
Aux compagnons de la tristesse, aux habitués du noir
  Dm                                     C                Dm
À toutes ces larmes qu'ils versent sans personne pour les voir
   F                                  Eb
À ceux qui n'attendent du sort qu'un tendre point final
        Dm
Qu'ils gouttent une fois avant leur mort
N.C
Un morceau d'Emmental
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
    Dm                              C          Dm
À ceux qui avaient des copines aux ricaneurs heureux
     Dm                             C                Dm
Ceux qui le soir à la cantine crachaient dans mes cheveux
     F                        Eb
Ces gros FDP sans escales qui se sentaient garçons
    Dm                        N.C.
Je leur donnerais l'Emmental mais avec du poison
                Dm
Mais avec du poison
(D F A F G) Gm Dm (F D F E) A
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A
                  Dm
Un morceau d'Emmental
(D F A F G) Gm Dm (F D F E) A Dm
         """
HarmonyLogger.outcome_level_of_detail = HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
