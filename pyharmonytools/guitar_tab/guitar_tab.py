from pychord import Chord

from pyharmonytools.guitar_neck.fingering import Fingering
from pyharmonytools.guitar_neck.neck import Neck
from pyharmonytools.guitar_tab.note_fret_caret import NoteFretCaret
from pyharmonytools.guitar_tab.string_and_cell import StringAndCell
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
    CARET = 1
    FRET = 0

    def __init__(self):
        pass

    @staticmethod
    def get_fret_from_fingering(fingerings: dict, string_number: int, caret_position_start: int,
                                caret_position_end: int) -> []:
        """
        return the used fret found on the string_number between caret_position_start and caret_position_end
        :param fingerings:
        :param string_number:
        :param caret_position_start:
        :param caret_position_end:
        :return: [caret pos, fret number]
        """
        string_name = list(fingerings.keys())[string_number]
        for cell in fingerings[string_name]:
            if type(cell) != int:
                if caret_position_start <= cell[1] <= caret_position_end:
                    return cell
        return None

    @staticmethod
    def digest_tab_simplest_progressive_chords_in_a_bar(tab: str) -> {}:
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
        fingerings = GuitarTab.get_fingerings_from_tab(tab)
        finger_qty = 0
        chord_notes = []
        current_caret = -1
        first_caret = -1
        first_fret = -1
        note_fret_caret = GuitarTab.get_next_caret_position_across_strings_note_or_chord(fingerings, current_caret)
        if note_fret_caret:
            first_fret = note_fret_caret.fret
            first_caret = note_fret_caret.current_caret
            finger_qty += note_fret_caret.fingers_involved_qty
            current_caret = note_fret_caret.current_caret
        while note_fret_caret:
            if note_fret_caret.fret - first_fret < Fingering.FINGERING_WIDTH and finger_qty < Fingering.FINGERING_AVAILABLE_FINGERS:
                chord_notes = GuitarTab.add_notes_or_chord(chord_notes, note_fret_caret)
            else:
                possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=True,
                                                           simplest_chord_only=True)
                if possible_chord:
                    res[str(first_caret)] = possible_chord[0]
                else:
                    possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=False,
                                                               simplest_chord_only=True)
                    res[str(first_caret)] = possible_chord[0]
                chord_notes = GuitarTab.add_notes_or_chord([], note_fret_caret)
                # chord_notes = [note_fret_caret.current_notes]
                finger_qty = 0
                first_fret = note_fret_caret.fret
                finger_qty += note_fret_caret.fingers_involved_qty
                current_caret = note_fret_caret.current_caret
                first_caret = note_fret_caret.current_caret
            note_fret_caret = GuitarTab.get_next_caret_position_across_strings_note_or_chord(fingerings, current_caret)
            if note_fret_caret:
                first_fret = note_fret_caret.fret
                finger_qty += note_fret_caret.fingers_involved_qty
                current_caret = note_fret_caret.current_caret
            else:
                possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=True,
                                                           simplest_chord_only=True)
                if possible_chord:
                    res[str(first_caret)] = possible_chord[0]
                else:
                    possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=False,
                                                               simplest_chord_only=True)
                    res[str(first_caret)] = possible_chord[0]
        return res

    @staticmethod
    def get_fingerings_from_tab(tab: str) -> dict:
        """
        translates the tab into fingerings
        :param tab: must be a simple bar tab - eg.
                e|--11---|
                B|-------|
                G|-------|
                D|-------|
                A|-------|
                E|-------|
        :return: fingerings = {
                'e': [-1, [11, 2], -1, ...],
                'B': [-1, [11, 2], -1, ...],
                ...}
                        -1: finger
                        [11, 2]: 11th fret found at caret 2 from the '|'
        """
        fingerings = {}
        strings = tab.split('\n')  # todo define Neck.TUNING from strings
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
                if "-" not in part and part != "" and part != "|":  # todo use "|" to delimit bars
                    fret = int(part)  # todo handle hammering, pull off, etc.
                    fingerings[string_name][part_position] = [int(fret), pos_on_string]
                    pos_on_string += len(str(fret)) + 1
                else:
                    pos_on_string += 1
                part_position += 1
        return fingerings

    @staticmethod
    def get_notes_from_chord_layout(chord_layout: []) -> [Note]:
        """

        :param chord_layout:
        :return: [notes]
        """
        notes = []
        for (string_name, fret) in zip(Neck.TUNING, chord_layout):
            string_number = Neck.TUNING.index(string_name)
            if chord_layout[string_number] not in [Fingering.FRET_OPEN, Fingering.FRET_MUTE]:
                notes.append(Note(Neck.find_note_from_position(string_name, fret)))
            else:
                notes.append(None)
        return notes

    @staticmethod
    def is_next_string_and_cell_beyond_cluster(previous_string_and_cell: StringAndCell,
                                               current_string_and_cell: StringAndCell,
                                               next_string_and_cell: StringAndCell,
                                               max_sac: StringAndCell) -> bool:
        is_there_a_next_sac = next_string_and_cell
        is_next_sac_in_a_next_cluster = next_string_and_cell.caret > max_sac.caret
        res = is_there_a_next_sac and is_next_sac_in_a_next_cluster
        return res

    @staticmethod
    def get_next_caret_position_across_strings_note_or_chord(fingerings: {}, caret_start: int):
        """
        browse vertically the neck from the nut to find the first used fret caret_start wise
        :param fingerings:
        :param caret_start:
        :return:
        """
        res = None
        current_pos = 0
        current_caret = -1
        notes = []
        chord_layout = [-1] * len(Neck.TUNING)
        fret = -1
        strings = list(fingerings.keys())
        reference_string_name = strings[0]
        for cell in fingerings[reference_string_name]:
            for string_name_vertical in fingerings.keys():
                cell_vertical = fingerings[string_name_vertical][current_pos]
                if type(cell_vertical) != int:
                    if cell_vertical[GuitarTab.CARET] > caret_start:
                        note = Neck.find_note_from_position(string_name_vertical, cell_vertical[GuitarTab.FRET])
                        notes.append(note)
                        fret = cell_vertical[GuitarTab.FRET]
                        current_caret = cell_vertical[GuitarTab.CARET]
                        chord_layout[Neck.TUNING.index(string_name_vertical)] = fret
            if notes:
                break
            current_pos += 1
        note_or_chord = None
        if len(notes) == 0:
            note_or_chord = None
        elif len(notes) == 1:
            note_or_chord = Note(notes[0])
        elif len(notes) >= 1:
            possible_chord = CofChord.guess_chord_name(notes, is_strictly_compliant=True,
                                                       simplest_chord_only=True)
            note_or_chord = possible_chord[0]
        fingers_involved_qty = len(list(dict.fromkeys(chord_layout)))
        if -1 in chord_layout:
            fingers_involved_qty -= 1
        if len(notes) > 0:
            res = NoteFretCaret(note_or_chord, fret, current_caret, fingers_involved_qty)
        return res

    @staticmethod
    def add_notes_or_chord(chord_notes: [], note_fret_caret: NoteFretCaret) -> []:
        if type(note_fret_caret.current_notes) == Note:
            chord_notes.append(note_fret_caret.current_notes)
        elif type(note_fret_caret.current_notes) == Chord:
            components = note_fret_caret.current_notes.components()
            for c in components:
                chord_notes.append(c)
        # remove dupes
        res = []
        for c in chord_notes:
            if c not in res:
                res.append(c)
        return res

