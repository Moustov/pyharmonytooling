from pychord import Chord

from src.harmony.harmony_tools import find_substitutes
from src.output.console import LOD_ALL

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

outcome_level_of_detail = LOD_ALL
chord = "G6"
print("substitutes from :", chord, find_substitutes(Chord(chord)))
# print(find_similar_chords())

