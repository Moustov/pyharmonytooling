from pychord import Chord

from pyharmonytools.guitar_neck.fingering import Fingering
from pyharmonytools.guitar_neck.neck import Neck
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

    def __init__(self):
        pass

    @staticmethod
    def digest_tab_simplest_splitted_chords_in_a_bar(tab: str) -> {}:
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

        print(fingerings)
        # todo imagine different clusters to guess chords
        string_names = list(fingerings.keys())
        chord_layout = [-1] * len(Neck.TUNING)
        clusters = {}  # {"caret_pos": chord_layout, ...}
        previous_string_and_cell = GuitarTab.get_first_caret_position_across_strings(fingerings)
        current_string_and_cell = previous_string_and_cell
        max_sac = GuitarTab.get_next_caret_position_across_strings(fingerings, start_from=current_string_and_cell.caret)
        while current_string_and_cell:
            string_number = string_names.index(current_string_and_cell.string_name)
            chord_layout[string_number] = current_string_and_cell.fret  # warning: chord_layout[0] <==> 'e'
            clusters[str(previous_string_and_cell.caret)] = chord_layout
            next_string_and_cell = GuitarTab.get_next_caret_position_across_strings(fingerings, start_from=current_string_and_cell.caret)
            if next_string_and_cell and next_string_and_cell.caret >= max_sac.caret \
                    and next_string_and_cell.string_name == max_sac.string_name:
                previous_string_and_cell = current_string_and_cell
                chord_layout = [-1] * len(Neck.TUNING)
                max_sac = GuitarTab.get_next_caret_position_across_strings(fingerings,
                                                                           start_from=current_string_and_cell.caret)
            current_string_and_cell = next_string_and_cell

        print(clusters)
        for k in clusters.keys():
            chord_layout = list(reversed(clusters[k]))
            cn = GuitarTab.get_notes_from_chord_layout(chord_layout)
            # remove all muted string & dupes
            chord_notes = []
            for n in cn:
                if n and n not in chord_notes:
                    chord_notes.append(n)
            possible_chords = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=True,
                                                        simplest_chord_only=True)
            try:
                res[k] = possible_chords[0]
            except IndexError:
                res[k] = None
        return res

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
    def digest_tab_simplest_vertical_chords_in_a_bar(tab: str) -> {}:
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
        print(fingerings)
        # todo imagine different clusters to guess chords
        first_string_name = list(fingerings.keys())[0]
        tab_size = len(fingerings[first_string_name])
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
                possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=False,
                                                           simplest_chord_only=True)
                print(possible_chord)
                for string_name in fingerings.keys():
                    if type(fingerings[string_name][fingering_sequence]) != int:
                        res[str(fingerings[string_name][fingering_sequence][1])] = possible_chord[0]
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
    def get_first_caret_position_across_strings(fingerings) -> StringAndCell:
        """
        returns the 1st caret position found with a note
        :param fingerings: {'e': [-1, -1, [11, 2]], 'B': [-1, [11,1], -1]} returns 1
        :return: a StringAndCell
                    StringAndCell.caret = the first position or -1 if not found
        """
        first_caret_position = GuitarTab.get_next_caret_position_across_strings(fingerings, -1)
        return first_caret_position

    @staticmethod
    def get_next_caret_position_across_strings(fingerings, start_from: int) -> StringAndCell:
        """
        return the next caret position from a previous_pos
        :param fingerings:
        :param start_from: the start_from position is excluded
        :return: a StringAndCell
                    StringAndCell.caret = the first position or -1 if not found
        """
        previous_pos = -1
        found_string = None
        for string_name in fingerings.keys():
            for cell in fingerings[string_name]:
                if type(cell) != int:
                    if cell[1] > start_from:
                        if previous_pos == -1:
                            previous_pos = cell
                            found_string = string_name
                        else:
                            if cell[1] < previous_pos[1]:
                                previous_pos = cell
                                found_string = string_name
        if found_string:
            return StringAndCell(found_string, caret=previous_pos[1], fret=previous_pos[0])
        else:
            return None

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
