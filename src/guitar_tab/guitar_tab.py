from pychord import Chord

from src.guitar_neck.fingering import Fingering
from src.guitar_neck.neck import Neck
from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class GuitarTab():
    def __init__(self):
        pass

    @staticmethod
    def digest_tab(tab: str) -> [Chord]:
        """
        todo implementation on going here
        e|--11-----11-----10-----11------------------------------------------------|
        B|--11-----12-----11-----11------------------------------------------------|
        G|--11-----13-----10-----11------------------------------------------------|
        D|-------------------------------------------------------------------------|
        A|-------------------------------------------------------------------------|
        E|-------------------------------------------------------------------------|

        :param tab:
        :return: [<Chord("Gb6")>, <Chord("G#m")>, <Chord("F6sus")>, <Chord("Gb6")>]
        """
        res = []
        MAX_SEQUENCE = 20
        fingerings = {}
        strings = tab.strip().split('\n')   # todo define Neck.TUNING from strings
        for string in strings:
            parts = string.split("-")
            string_name = parts[0].strip()
            string_name = string_name[0]
            part_position = 0
            fingerings[string_name] = [Fingering.FRET_MUTE] * MAX_SEQUENCE
            for part in parts[1:]:
                if "-" not in part and part != "" and part != "|":   # todo use "|" to delimit bars
                    fret = int(part)    # todo handle hammering, pull off, etc.
                    fingerings[string_name][part_position] = int(fret)
                part_position += 1

        print(fingerings)
        # todo imagine different clusters to guess chords
        for fingering_sequence in range(0, MAX_SEQUENCE):
            chord_layout = []
            chord_notes = []
            chord = None
            for string_name in fingerings.keys():
                fret = fingerings[string_name][fingering_sequence]
                chord_layout.append(fret)
                if fret != -1:
                    chord_notes.append(Note(Neck.find_note_from_position(string_name, fret)))
            if len(chord_notes) > 0:
                chord = CofChord.guess_chord_name(chord_notes)
                print(chord)
                res.append(chord)
        return res
