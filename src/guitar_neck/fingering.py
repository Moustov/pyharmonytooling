from pychord import Chord

from src.guitar_neck.neck_exception import NeckException
from src.guitar_neck.neck import Neck


class Fingering:
    FINGERING_WIDTH = 3
    FINGERING_AVAILABLE_FINGERS = 4
    FRET_UNDEFINED = -100
    FRET_MUTE = -1
    FRET_OPEN = 0

    TAB_MUTE = "X"
    TAB_OPEN = "0"
    TAB_THUMB = "T"
    TAB_INDEX = "1"
    TAB_MIDDLE_FINGER = "2"
    TAB_RING_FINGER = "3"
    TAB_PINKY = "4"
    TAB_UNDEFINED = "?"
    TAB_EMPTY = "-"

    def __init__(self, a_neck: Neck = Neck()):
        self.neck = a_neck

    def get_tab_from_array(self, chord_array: [int]) -> dict:
        """
        turns [2, 0, 0, 0, 0, 2]
        into {
                "e": ["-", "-", "?", "-"],
                "B": ["0", "-", "-", "-"],
                "G": ["0", "-", "-", "-"],
                "D": ["0", "-", "-", "-"],
                "A": ["0", "-", "-", "-"],
                "E": ["-", "-", "?", "-"]
            }
        where "?" is the placeholder for the fingering
        :param chord_array:
        :return:
        """
        tab = {}
        for string in self.neck.TUNING:
            tab[string] = []
            for fret in range(1, self.FINGERING_WIDTH + 2):
                tab[string].append(Fingering.TAB_EMPTY)

        for string in self.neck.TUNING:
            if chord_array[self.neck.TUNING.index(string)] in [1, 2, 3, 4]:
                tab[string][int(chord_array[self.neck.TUNING.index(string)])] = Fingering.TAB_UNDEFINED
            elif chord_array[self.neck.TUNING.index(string)] == self.FRET_OPEN:
                tab[string][0] = Fingering.TAB_OPEN
            elif chord_array[self.neck.TUNING.index(string)] == self.FRET_MUTE:
                tab[string][0] = Fingering.TAB_MUTE
            else:
                raise Exception(f"incorrect Fret {chord_array[self.neck.TUNING.index(string)]}")
        return tab

    def get_array_from_tab(self, tab: dict) -> [int]:
        """
         turns  {
                "e": ["-", "-", "2", "-"],
                "B": ["0", "-", "-", "-"],
                "G": ["0", "-", "-", "-"],
                "D": ["0", "-", "-", "-"],
                "A": ["0", "-", "-", "-"],
                "E": ["-", "-", "2", "-"]
            }
        into [2, 0, 0, 0, 0, 2]
        :param tab:
        :return:
        """
        res = [self.FRET_UNDEFINED, self.FRET_UNDEFINED, self.FRET_UNDEFINED, self.FRET_UNDEFINED, self.FRET_UNDEFINED,
               self.FRET_UNDEFINED]
        for string in self.neck.TUNING:
            string_index = self.neck.TUNING.index(string)
            if tab[string][0] == Fingering.TAB_OPEN:
                res[string_index] = Fingering.FRET_OPEN
            elif tab[string][0] == Fingering.TAB_MUTE:
                res[string_index] = Fingering.FRET_MUTE
            else:
                for fret in range(1, len(tab[string]) + 1):
                    if tab[string][fret] != Fingering.TAB_EMPTY:
                        res[string_index] = int(fret)
                        break
        return res

    def is_string_fingered_before_fret(self, barres: dict, chord_array: [int],
                                       reference_fret: int,
                                       reference_string: str) -> bool:
        """

        :param barres:
        :param chord_array:
        :param reference_fret:
        :param reference_string:
        :return:
        """
        is_string_fingered = chord_array[Neck.TUNING.index(reference_string)] not in [self.FRET_OPEN,
                                                                                      self.FRET_MUTE,
                                                                                      self.FRET_UNDEFINED]
        is_finger_before = False
        frets = sorted(barres.keys(), reverse=True)
        for fret in frets:
            if int(fret) < reference_fret:
                for string in barres[fret]:
                    # for lower_fret in range(1, Neck.TUNING.index(fret)):
                    for lower_fret in range(1, int(fret)):
                        if str(lower_fret) in frets:
                            for s in barres[str(lower_fret)]:
                                if s == string:
                                    is_finger_before = True
                                    break
                    if is_finger_before:
                        break
                if is_finger_before:
                    break
        return is_string_fingered and is_finger_before

    def find_possible_barres(self, chord_layout: [int]) -> {}:
        """
        eg. chord_layout = [1, 3, 3, 2, 1, 1]
        => {"1": [0, 1, 2, 3, 4, 5], "2": [3], "3": [1,2]}
        * keys are the fret numbers
        * lists : the fingered strings numbers
        /!\ barres with lower frets inside must be handled to adapt fingering (eg. open G chord)
        :param chord_layout:
        :return:
        """
        local_chord_layout = chord_layout.copy()
        barres_found = {}
        for string in Neck.TUNING:
            fret_index = chord_layout[Neck.TUNING.index(string)]
            if fret_index not in [self.FRET_OPEN, self.FRET_MUTE]:
                if str(fret_index) in barres_found.keys():
                    barres_found[str(fret_index)].append(Neck.TUNING.index(string))
                else:
                    barres_found[str(fret_index)] = [Neck.TUNING.index(string)]
        self.remove_muted_strings(local_chord_layout)
        for fret in range(min(local_chord_layout), max(local_chord_layout) + 1):
            s_fret = str(fret)
            if s_fret in barres_found.keys():
                min_f = min(barres_found[s_fret])
                max_f = max(barres_found[s_fret])
                barres_found[s_fret] = []
                for f in range(min_f, max_f + 1):
                    barres_found[s_fret].append((f))
        return barres_found

    def find_finger_layout(self, chord_layout: [int]) -> [chr]:
        """
        finds an appropriate finger layout from a chord
        :param chord_layout:
        :return: X: mute / 0: open / T: thumb / 1: index / 2: major / 3:ring finger / 4: pinky
        """
        if self.all_chord_are_mute_or_open(chord_layout):
            # convenient way to provide a tab with "0" & "X"
            # since there is no fingering on cells
            return self.get_tab_from_array(chord_layout)
        used_neck_length = self.get_highest_used_neck(chord_layout)
        fret_start = self.get_lowest_used_fret(chord_layout)
        tab = {}
        for string in self.neck.TUNING:
            tab[string] = []
            for fret in range(1, used_neck_length + 1):
                tab[string].append(Fingering.TAB_EMPTY)
        i = 0
        for cell in chord_layout:
            if cell == self.FRET_MUTE:
                tab[self.neck.TUNING[i]][0] = Fingering.TAB_MUTE
            elif cell == self.FRET_OPEN:
                tab[self.neck.TUNING[i]][0] = Fingering.TAB_OPEN
            else:
                tab[self.neck.TUNING[i]][cell] = Fingering.TAB_UNDEFINED
            i += 1

        involved_fingers = 0
        new_finger_found = False
        barres = self.find_possible_barres(chord_layout)
        keys = sorted(barres.keys())
        for fret in keys:
            f = int(fret)
            for string in barres[fret]:
                new_finger_found = False
                if tab[Neck.TUNING[string]][f] == Fingering.TAB_UNDEFINED:
                    tab[Neck.TUNING[string]][f] = str(f - fret_start + 1)
                    new_finger_found = True
                    if self.is_string_fingered_before_fret(barres, chord_layout, int(fret), Neck.TUNING[string]):
                        tab[Neck.TUNING[string]][f] = str(int(tab[Neck.TUNING[string]][f]) + 1)
                        involved_fingers += 1
            if new_finger_found:
                involved_fingers += 1
        if involved_fingers > 4:
            raise NeckException(f"Too many fingers required for the tab {chord_layout}")
        return tab

    @staticmethod
    def get_max_finger(tab: {}):
        """
        returns the highest fingering value in a tab
        :param tab:
        :return: 0 if no fingering has been found
        """
        max_finger = 0
        for string in Neck.TUNING:
            for fret in tab[string]:
                if fret not in [Fingering.TAB_MUTE, Fingering.TAB_EMPTY, Fingering.TAB_UNDEFINED, Fingering.TAB_OPEN]:
                    if int(fret) > max_finger:
                        max_finger = int(fret)
        return max_finger

    def fingering_is_possible(self, fret_positions: [int]) -> bool:
        m = self.neck.FRET_QUANTITY
        for fret in fret_positions:
            if fret not in [self.FRET_OPEN, self.FRET_MUTE] \
                    and fret <= m:
                m = fret
        x = max(fret_positions)
        return abs(x - m) <= Fingering.FINGERING_WIDTH

    def get_fingering_from_chord(self, chord: Chord, all_strings: bool = True) -> [[int]]:
        """
        https://www.musicnotes.com/now/tips/how-to-read-guitar-tabs/
        :param all_strings: # todo: True if all string are plucked/strummed
        :param chord:
        :return:
        """
        guitar = {}
        possible_fingerings = []
        chord_positions = {}
        for note in chord.components():
            chord_positions[note] = []
            for string in self.neck.TUNING:
                p = self.neck.find_positions_on_string_from_note(string, note)
                for pos in p:
                    chord_positions[note].append(pos)
        for string in self.neck.TUNING:
            guitar[string] = []
        for pos in chord_positions.keys():
            for p in chord_positions[pos]:
                guitar[p[0]].append(p[1])
        for string in self.neck.TUNING:
            guitar[string].sort()

        for E in guitar["E"]:
            for A in guitar["A"]:  # todo break when width > self.FINGERING_WIDTH
                for D in guitar["D"]:  # todo break when width > self.FINGERING_WIDTH
                    for G in guitar["G"]:  # todo break when width > self.FINGERING_WIDTH
                        for B in guitar["B"]:  # todo break when width > self.FINGERING_WIDTH
                            for e in guitar["e"]:  # todo break when width > self.FINGERING_WIDTH
                                fingering_combination = [E, A, D, G, B, e]
                                if self.fingering_is_possible(fingering_combination):
                                    possible_fingerings.append(fingering_combination)
        return possible_fingerings

    def get_highest_used_neck(self, layout: [int]) -> int:
        chord_layout = layout.copy()
        self.remove_muted_strings(chord_layout)
        highest_used_neck = max(chord_layout)
        highest_used_neck = max(self.FINGERING_WIDTH + 1, highest_used_neck + 1)  # +1 due to the nut
        return highest_used_neck

    def get_lowest_used_fret(self, layout: [int]) -> int:
        chord_layout = layout.copy()
        self.remove_muted_strings(chord_layout)
        self.remove_open_strings(chord_layout)
        lowest_used_fret = min(chord_layout)
        return lowest_used_fret

    def remove_muted_strings(self, chord_layout: [int]):
        try:
            while self.FRET_MUTE in chord_layout: chord_layout.remove(self.FRET_MUTE)
        except Exception:
            pass

    def remove_open_strings(self, chord_layout: [int]):
        try:
            while self.FRET_OPEN in chord_layout: chord_layout.remove(self.FRET_OPEN)
        except Exception:
            pass

    def all_chord_are_mute_or_open(self, chord_layout):
        for cell in chord_layout:
            if cell not in [self.FRET_OPEN, self.FRET_MUTE]:
                return False
        return True
