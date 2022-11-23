from pychord import Chord

from src.guitar_neck.fingering import Fingering
from src.guitar_neck.neck import Neck
from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class GuitarTab():
    def __init__(self):
        pass

    @staticmethod
    def digest_tab_simplest_chords_in_a_bar(tab: str) -> {}:
        """
        provide the simplest chord at each char position in the bar
        e|--11-----11-----10-----11-----|
        B|--11-----12-----11-----11-----|
        G|--11-----13-----10-----11-----|
        D|------------------------------|
        A|------------------------------|
        E|------------------------------|
        would return {"2": Chord("D#m"), "8": Chord("G#m"), "15": Chord("Bb"), "22": Chord("D#m")}
        :param tab:
        :return: the keys would be the nb of chars from '|' (bar delimiter)
        """
        res = {}
        MAX_SEQUENCE = 20
        fingerings = {}
        strings = tab.strip().split('\n')   # todo define Neck.TUNING from strings
        for string in strings:
            parts = string.split("-")
            string_name = parts[0].strip()
            string_name = string_name[0]
            part_position = 0
            fingerings[string_name] = [Fingering.FRET_MUTE] * MAX_SEQUENCE
            pos_on_string = 1
            fret = 0
            for part in parts[1:]:
                if "-" not in part and part != "" and part != "|":   # todo use "|" to delimit bars
                    fret = int(part)    # todo handle hammering, pull off, etc.
                    fingerings[string_name][part_position] = [int(fret), pos_on_string]
                part_position += 1
                pos_on_string += len(str(fret))

        print(fingerings)
        # todo imagine different clusters to guess chords
        for fingering_sequence in range(0, part_position):
            chord_layout = []
            chord_notes = []
            chord = None
            fret = None
            for string_name in fingerings.keys():
                cell = fingerings[string_name][fingering_sequence]
                if type(cell) != int:
                    fret = fingerings[string_name][fingering_sequence][0]
                    chord_layout.append(fret)
                    if fret != -1:
                        chord_notes.append(Note(Neck.find_note_from_position(string_name, fret)))
            if len(chord_notes) > 0:
                possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=False, simplest_chord_only=True)
                print(possible_chord)
                for string_name in fingerings.keys():
                    if type(fingerings[string_name][fingering_sequence]) != int:
                        res[str(fingerings[string_name][fingering_sequence][1])] = possible_chord[0]
        return res
