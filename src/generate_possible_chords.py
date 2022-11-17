from pychord import Chord

from src.guitar_neck.fingering import Fingering
from src.guitar_neck.neck import Neck


def all_possible_chords_with_all_string(chord_name: str):
    n = Neck()
    Fingering.FINGERING_WIDTH = 3
    n.FRET_QUANTITY = n.FRET_QUANTITY_CLASSIC
    n.TUNING = ['E', 'A', 'D', 'G', 'B', 'e']
    fng = Fingering()
    possible_fingerings = fng.get_chord_layouts_from_a_chord(Chord(chord_name), all_strings=True)
    with open(f"{chord_name} - possible_fingerings.txt", "w") as fil:
        fil.write(str(possible_fingerings))
    assert True  # hardly testable


all_possible_chords_with_all_string("D")
all_possible_chords_with_all_string("Cm")
all_possible_chords_with_all_string("Cmaj7")

