from src.harmony.circle_of_5th import digest_song, guess_tone_and_mode, \
    circle_of_fifths_natural_majors, get_borrowed_chords
from src.output.console import LOD_NONE

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
outcome_level_of_detail = LOD_NONE
cp = digest_song(song)
compliance_level_max = guess_tone_and_mode(cp)
print("Compliance:", compliance_level_max)
tone = circle_of_fifths_natural_majors[compliance_level_max[1]]
borrowed_chords = get_borrowed_chords(tone, cp)
print("Borrowed chords:", borrowed_chords.keys())
#
# tone = circle_of_fifths_natural_majors[compliance_level_max[1]]
# borrowed_chords = get_borrowed_chords(tone, cp)
# print("Borrowed chords:", borrowed_chords.keys())



#
# from src.output.console_for_guitar_neck import GuitarNeck
#
# outcome_level_of_detail = LOD_TONE
# chord = "G6"
# print("substitutes from :", chord, find_substitutes(Chord(chord)))
# # print(find_similar_chords())
#
#
# f = get_fingering_from_chord(Chord("C"))
# print(len(f), f)
# a_grid = GuitarNeck()
# grid = a_grid.blank_grid()
#
# for c in f:
#     fl = find_finger_layout(c)
#     print("***********")
#     grid = a_grid.blank_grid()
#     grid = a_grid.set_finger(grid, "E", c[0], fl[0])
#     grid = a_grid.set_finger(grid, "A", c[1], fl[1])
#     grid = a_grid.set_finger(grid, "D", c[2], fl[2])
#     grid = a_grid.set_finger(grid, "G", c[3], fl[3])
#     grid = a_grid.set_finger(grid, "B", c[4], fl[4])
#     grid = a_grid.set_finger(grid, "e", c[5], fl[5])
#     print(grid)