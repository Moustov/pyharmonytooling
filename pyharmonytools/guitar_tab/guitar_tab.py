from pychord import Chord

from pyharmonytools.guitar_neck.fingering import Fingering
from pyharmonytools.guitar_neck.neck import Neck
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.harmony.note import Note


class GuitarTab():
    """
    handling guitar tabs

    todo: handle
             /  slide up
             \  slide down
             h  hammer-on
             p  pull-off
             ~  vibrato
             +  harmonic
             x  Mute note

    todo handle guitar tuning
        E|---|
        B|---|
        G|---|
        D|---|
        A|---|
        D|---|

    todo handle bars & repeats
        F||-----6-4-|-----7-6-|-----7-6|-----7-6||
        C||---2-----|---4-----|---6----|---6----||
        G||-0-------|-0-------|-0------|-0------||
        D||---------|---------|--------|--------||
        A||---------|---------|--------|--------||
        E||---------|---------|--------|--------||

    todo handle multiple tabs: the fretboard is repeated over to continue the song
    """

    def __init__(self):
        pass

    @staticmethod
    def digest_tab_simplest_chords_in_a_bar(tab: str) -> {}:
        """
        provide the simplest chord at the tab fret position in the bar
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
        fingerings = {}
        strings = tab.split('\n')   # todo define Neck.TUNING from strings
        tab_size = 0
        if strings:
            for s in strings:
                if tab_size < len(s):
                    tab_size = len(s)
        for string in strings:
            if string.strip() == "":
                continue
            parts = string.strip().split("-")
            print("-", string)
            string_name = parts[0].strip()
            string_name = string_name[0]
            part_position = 0
            fingerings[string_name] = [Fingering.FRET_MUTE] * tab_size
            pos_on_string = 1
            fret = 0
            for part in parts[1:]:
                if "-" not in part and part != "" and part != "|":   # todo use "|" to delimit bars
                    fret = int(part)    # todo handle hammering, pull off, etc.
                    fingerings[string_name][part_position] = [int(fret), pos_on_string]
                    pos_on_string += len(str(fret)) + 1
                else:
                    pos_on_string += 1
                part_position += 1


        print(fingerings)
        # todo imagine different clusters to guess chords
        for fingering_sequence in range(0, tab_size):
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
