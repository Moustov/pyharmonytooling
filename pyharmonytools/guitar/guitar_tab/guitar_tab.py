from pychord import Chord
from pyharmonytools.guitar.guitar_neck.fingering import Fingering
from pyharmonytools.guitar.guitar_neck.neck import Neck
from pyharmonytools.guitar.guitar_tab.chord_and_fingering import ChordAndFingering
from pyharmonytools.guitar.guitar_tab.note_fret_caret import NoteFretCaret
from pyharmonytools.guitar.guitar_tab.string_and_cell import StringAndCell
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.harmony.note import Note


class GuitarTab:
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

    def __init__(self, tab: str):
        self.tab_ascii = tab
        self._bars_tab_dict = []
        self.bars_ascii = self._split_tab_in_bars(tab)
        bar_id = 0
        for b in self.bars_ascii:
            self._bars_tab_dict.append({})
            self._get_fingerings_from_tab_bar(b, bar_id)
            bar_id += 1

    def get_nb_chars_in_bar(self, bar: int) -> int:
        """
        return the nb of chars in the bar
        :param bar:
        :return:
        """
        bar_lines = self.bars_ascii[bar].split("\n")
        return len(bar_lines[0])

    def get_number_of_bars(self) -> int:
        """
        return the number of digested bars
        :return:
        """
        return len(self.bars_ascii)

    def _get_fret_from_fingering(self, bar_id: int, string_number: int, caret_position_start: int,
                                 caret_position_end: int) -> []:
        """
        return the used fret found on the string_number between caret_position_start and caret_position_end
        :param bar_id: a bar
        :param string_number:
        :param caret_position_start:
        :param caret_position_end:
        :return: [caret pos, fret number]
        """
        string_name = list(self._bars_tab_dict[bar_id].keys())[string_number]
        for cell in self._bars_tab_dict[bar_id][string_name]:
            if type(cell) != int:  # todo use polymorphism !
                if caret_position_start <= cell[1] <= caret_position_end:
                    return cell
        return None

    def get_simplest_progressive_chords_in_a_bar(self, bar_id: int) -> {}:
        """
        provide the simplest chord at the tab fret position in the bar
        e|--11-----11-----10-----11-----|
        B|--11-----12-----11-----11-----|
        G|--11-----13-----10-----11-----|
        D|------------------------------|
        A|------------------------------|
        E|------------------------------|
        would return {"2": Chord("D#m"), "8": Chord("G#m"), "15": Chord("Bb"), "22": Chord("D#m")}
        Note 1: the involved method is based on building chords
                    as long as the fret range is acceptable (Fingering.FINGERING_WIDTH)
                    and you have enough fingers or a tab
                    therefore, sometimes the chord guessing is not inaccurate
                    since musical phrases are not taken into account
                    see unit tests test_digest_bach_bar_1_2 and test_digest_bach_bar_1_2_with_bar
        Note 2: the resulted chords can be post-processed
                - to use appropriate notation (eg Bb instead of A#) and renversed chord names
                - improve chord names from context
                - to guess some rythm and introduce visual rythmic signs (1/4th or 1/8th with a "+")
                - display the decorated tab
        :return: the keys would be the nb of chars from '|' (bar delimiter)
        """
        res = {}
        finger_qty = 0
        chord_notes = []
        current_caret = -1
        first_caret = -1
        first_fret = -1
        note_fret_caret = self._get_next_caret_position_across_strings_note_or_chord(current_caret, bar_id)
        if note_fret_caret:
            first_fret = note_fret_caret.fret
            first_caret = note_fret_caret.current_caret
            finger_qty = 0
            current_caret = note_fret_caret.current_caret
        while note_fret_caret:
            caf = None
            if GuitarTab.is_note_fret_caret_in_same_chord(chord_notes, note_fret_caret, first_fret, finger_qty):
                caf = GuitarTab._add_notes_or_chord(chord_notes, note_fret_caret)
                chord_notes = caf.chord_notes
                finger_qty += caf.fingers
            else:
                possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=True,
                                                           simplest_chord_only=True)
                if possible_chord:
                    res[str(first_caret)] = possible_chord[0]
                else:
                    possible_chord = CofChord.guess_chord_name(chord_notes, is_strictly_compliant=False,
                                                               simplest_chord_only=True)
                    res[str(first_caret)] = possible_chord[0]
                caf = GuitarTab._add_notes_or_chord([], note_fret_caret)
                chord_notes = caf.chord_notes
                first_fret = note_fret_caret.fret
                finger_qty = caf.fingers
                current_caret = note_fret_caret.current_caret
                first_caret = note_fret_caret.current_caret
            note_fret_caret = self._get_next_caret_position_across_strings_note_or_chord(current_caret, bar_id)
            if note_fret_caret:
                # first_fret = note_fret_caret.fret
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

    def _get_fingerings_from_tab_bar(self, tab_bar_ascii: str, bar_number: int) -> dict:
        """
        translates the tab into fingerings.
        result will be returned & set in self.tab_dict
        :param bar_number: the bar ID
        :param tab_bar_ascii: must be a simple bar tab - eg.
                e|--11---|
                B|-------|
                G|-------|
                D|-------|
                A|-------|
                E|-------|
        :return: fingerings = {
                'e': [-1, [11, 2], -1, ...],
                'B': [-1, -1 , -1, ...],
                ...}
                        -1: no finger
                        [11, 2]: 11th fret found at caret 2 from the '|' (bar start)
        """
        self._bars_tab_dict[bar_number] = {}
        strings = tab_bar_ascii.split('\n')  # todo define Neck.TUNING from strings
        tab_size = 0
        if strings:
            for s in strings:
                bars = s.split("|")
                timeline = ""
                for b in bars[1:]:
                    timeline += b
                if tab_size < len(timeline):
                    tab_size = len(timeline)
        for string in strings:
            if string.strip() == "":
                continue
            parts = string.strip()
            print("-", string)
            string_name = parts[0].strip()
            string_name = string_name[0]
            part_position = 2
            self._bars_tab_dict[bar_number][string_name] = [Fingering.FRET_MUTE] * tab_size
            pos_on_string = 0
            fret = 0
            while part_position < len(parts):
                fret_s = ""
                while parts[part_position] != "-" and parts[part_position] != "|":  # todo use "|" to delimit bars
                    if ord(parts[part_position]) in range(ord('0'), ord('9')):  # todo handle hammering, pull off, etc.
                        fret_s += parts[part_position]
                    pos_on_string += 1
                    part_position += 1
                if fret_s:
                    fret = int(fret_s)
                    self._bars_tab_dict[bar_number][string_name][pos_on_string - len(fret_s)] = [fret,
                                                                                                 pos_on_string - len(fret_s)]
                else:
                    pos_on_string += 1
                    part_position += 1
        return self._bars_tab_dict[bar_number]

    @staticmethod
    def _get_notes_from_chord_layout(chord_layout: []) -> [Note]:
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
    def _is_next_string_and_cell_beyond_cluster(previous_string_and_cell: StringAndCell,
                                                current_string_and_cell: StringAndCell,
                                                next_string_and_cell: StringAndCell,
                                                max_sac: StringAndCell) -> bool:
        is_there_a_next_sac = next_string_and_cell
        is_next_sac_in_a_next_cluster = next_string_and_cell.caret > max_sac.caret
        res = is_there_a_next_sac and is_next_sac_in_a_next_cluster
        return res

    def _get_next_caret_position_across_strings_note_or_chord(self, caret_start: int, bar_id: int) -> NoteFretCaret:
        """
        browse vertically the neck from the nut to find the first used fret caret_start wise
        :param bar_id:
        :param caret_start:
        :return:
        """
        res = None
        notes = None
        current_pos = 0
        current_caret = -1
        chord_layout = [-1] * len(Neck.TUNING)
        fret = -1
        strings = list(self._bars_tab_dict[bar_id].keys())
        string = "X"
        # a tab timeline is browsed following what is available on the 1st string
        reference_string_name = strings[0]
        for cell in self._bars_tab_dict[bar_id][reference_string_name]:
            notes = []
            # then we look vertically at a fret
            for string_name_vertical in self._bars_tab_dict[bar_id].keys():
                cell_vertical = self._bars_tab_dict[bar_id][string_name_vertical][current_pos]
                if type(cell_vertical) != int:  # todo use polymorphism !
                    if cell_vertical[GuitarTab.CARET] > caret_start:
                        current_caret = cell_vertical[GuitarTab.CARET]
                        note = Neck.find_note_from_position(string_name_vertical, cell_vertical[GuitarTab.FRET])
                        notes.append(note)
                        fret = cell_vertical[GuitarTab.FRET]
                        chord_layout[Neck.TUNING.index(string_name_vertical)] = fret
                        string = string_name_vertical
            if len(notes) >= 1:
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
            if not possible_chord:
                possible_chord = CofChord.guess_chord_name(notes, is_strictly_compliant=False,
                                                           simplest_chord_only=True)
            if not possible_chord:
                raise ValueError(f"Could not find a chord name for {notes}")
            note_or_chord = possible_chord[0]

        fingers_involved_qty = len(list(dict.fromkeys(chord_layout)))
        # fingers_involved_qty must not be impacted with fret == 0
        if fret == 0:
            fingers_involved_qty -= 1
        # fingers_involved_qty must not take "-1" notes
        if -1 in chord_layout:
            fingers_involved_qty -= 1
        if len(notes) > 0:
            res = NoteFretCaret(note_or_chord, fret, current_caret, fingers_involved_qty, string)
        return res

    @staticmethod
    def _add_notes_or_chord(chord_notes: [], note_fret_caret: NoteFretCaret) -> ChordAndFingering:
        added_fingers = GuitarTab._extra_required_fingers_qty(chord_notes, note_fret_caret)
        if type(note_fret_caret.note_or_chord) == Note:  # todo use polymorphism !
            if str(note_fret_caret.note_or_chord) not in chord_notes:
                chord_notes.append(str(note_fret_caret.note_or_chord))
        elif type(note_fret_caret.note_or_chord) == Chord:
            components = note_fret_caret.note_or_chord.components()
            for note in components:
                if note not in chord_notes:
                    chord_notes.append(note)
        else:
            raise ValueError(f"Bad type of note found in {note_fret_caret.note_or_chord}")
        # remove dupes
        res = ChordAndFingering()
        res.fingers = added_fingers
        res.chord_notes = []
        for note in chord_notes:
            note_name = str(note)
            if note_name not in res.chord_notes:
                res.chord_notes.append(note_name)
        return res

    @staticmethod
    def is_note_fret_caret_in_same_chord(chord_notes: [], note_fret_caret: NoteFretCaret,
                                         first_fret: int, finger_qty: int) -> bool:
        """
        True if the fingering is kept unchanged
        :param chord_notes:
        :param note_fret_caret:
        :param first_fret:
        :param finger_qty:
        :return:
        """
        extra_fingers = GuitarTab._extra_required_fingers_qty(chord_notes, note_fret_caret)
        is_fingering_not_too_wide = note_fret_caret.fret - first_fret <= Fingering.FINGERING_WIDTH
        is_there_enough_fingers = extra_fingers + finger_qty <= Fingering.FINGERING_AVAILABLE_FINGERS
        return is_there_enough_fingers and is_fingering_not_too_wide

    @staticmethod
    def _extra_required_fingers_qty(chord_notes: [], note_fret_caret: NoteFretCaret) -> int:
        """
        return the extra amount of required fingers with note_fret_caret from chord_notes
        :param chord_notes:
        :param note_fret_caret:
        :return:    the qty of extra required fingers
        """
        # is the next note still in the same chord_notes ?
        is_next_tab_still_in_chord_notes = True
        finger_qty = 0
        note_found = False
        if type(note_fret_caret.note_or_chord) == Note:  # todo use polymorphism !
            for n in chord_notes:
                note_found = Note(n) == note_fret_caret.note_or_chord
                if note_found:
                    break
            if not note_found:
                finger_qty = 1
        elif type(note_fret_caret.note_or_chord) == Chord:
            for n in chord_notes:
                # if all the notes of the chord are not in the chord_notes
                notes_in_chord = note_fret_caret.note_or_chord.components()
                is_next_tab_still_in_chord_notes = True
                for c in notes_in_chord:
                    is_next_tab_still_in_chord_notes = is_next_tab_still_in_chord_notes \
                                                       and (Note(n) == Note(c))
                    if Note(n) != Note(c):
                        finger_qty += 1
        elif type(note_fret_caret.note_or_chord) == type([]):
            for n in chord_notes:
                set1 = set(chord_notes)
                set2 = set(note_fret_caret.note_or_chord)
                newList = list(set1.union(set2))
                is_next_tab_still_in_chord_notes = is_next_tab_still_in_chord_notes \
                                                   and len(newList) == len(chord_notes)
                finger_qty += len(newList) - len(chord_notes)
        else:
            raise ValueError(f"Bad type of note found in {note_fret_caret.note_or_chord}")
        if finger_qty == 0 and not note_found:
            finger_qty = 1
        return finger_qty

    def _split_tab_in_bars(self, tab: str) -> [str]:
        """
            e|-3----|-3----|
            B|------|------|
            G|------|------|
            D|------|------|
            A|------|------|
            E|------|------|

            e|-2----|-3----|
            B|------|------|
            G|------|------|
            D|------|------|
            A|------|------|
            E|------|------|

        returns 4 bars tabs
        :param tab:
        :return:
        """
        lines = tab.split("\n")
        bar_id = -1
        bars = []
        bars.append("")
        for li in lines:
            if li.strip() == "":
                bar_id += 1
                bars.append("")
            else:
                bars[bar_id] += li.strip() + "\n"
        res = []
        bar_id = 0
        for b in bars:
            if b != "":
                lines = b.split("\n")
                for li in lines:
                    string_bar = li.strip().split("|")
                    for b in string_bar[1:]:
                        if len(b) > 2:  # heuristic: if bigger than 4 char => it's a string content
                            res.append("")
        bar_id = 0
        for b in bars:
            if b != "":
                lines = b.split("\n")
                added_bars = 0
                for li in lines:
                    string_bar = li.strip().split("|")
                    bar_in_string = 0
                    for b in string_bar[1:]:
                        if len(b) > 2:  # heuristic: if bigger than 4 char => it's a string content
                            res[bar_id + bar_in_string] += f"{string_bar[0]}|{b}|\n"
                            bar_in_string += 1
                            added_bars = bar_in_string
                bar_id += added_bars + 1
        self.bars_ascii = []
        for b in res:
            if b.strip() != "":
                self.bars_ascii.append(b)
        return self.bars_ascii

    @staticmethod
    def are_same_digested_tabs(res: dict, expected: dict):
        """
        ensure carets & chords match are the same
        => compares both tab decorations (eg. { "2": xxx, "17": xxxx, ...})
            and ensure each chords match (at component level)
        :param res:
        :param expected:
        :return:
        """
        for chord_res in res.keys():
            if chord_res not in expected.keys():
                return False
            if not CofChord.are_chord_equals(expected[chord_res], res[chord_res]):
                return False
        for chord_expected in expected.keys():
            if chord_expected not in res.keys():
                return False
            if not CofChord.are_chord_equals(expected[chord_expected], res[chord_expected]):
                return False
        return True

