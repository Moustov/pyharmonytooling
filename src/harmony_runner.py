from pychord import Chord

from src.guitar_neck.neck import get_fingering_from_chord
from src.harmony.circle_of_5th import find_substitutes, find_similar_chords
from src.output.console import LOD_ALL, LOD_TONE

# song = """
#               A           E
#         Happy Birthday to you
#               E           A
#         Happy Birthday to you
#               A7            D
#         Happy Birthday dear (name)
#               A        E    A
#         Happy Birthday to you
#         """
# outcome_level_of_detail = LOD_NONE
# cp = digest_song(song)
# compliance_level_max = guess_tone_and_mode(cp)
# print("Compliance:", compliance_level_max)
#
# tone = circle_of_fifths_natural_majors[compliance_level_max[1]]
# borrowed_chords = get_borrowed_chords(tone, cp)
# print("Borrowed chords:", borrowed_chords.keys())
from src.output.console_for_guitar_neck import GuitarNeck

outcome_level_of_detail = LOD_TONE
chord = "G6"
print("substitutes from :", chord, find_substitutes(Chord(chord)))
# print(find_similar_chords())


f = get_fingering_from_chord(Chord("Cmaj7/9/13"))
print(len(f), f)
a_grid = GuitarNeck()
grid = a_grid.blank_grid()
print(grid)
for c in f:
    print("***********")
    grid = a_grid.blank_grid()
    grid = a_grid.set_finger(grid, "E", c[0])
    grid = a_grid.set_finger(grid, "A", c[1])
    grid = a_grid.set_finger(grid, "D", c[2])
    grid = a_grid.set_finger(grid, "G", c[3])
    grid = a_grid.set_finger(grid, "B", c[4])
    grid = a_grid.set_finger(grid, "e", c[5])
    print(grid)