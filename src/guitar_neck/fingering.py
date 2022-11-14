from pychord import Chord

from src.guitar_neck.neck_exception import NeckException
from src.guitar_neck.neck import Neck


class Fingering:
    FINGERING_WIDTH = 3
    FINGERING_AVAILABLE_FINGERS = 4
    possible_fingers = ["X", "0", "T", "1", "2", "3", "4"]

    def __init__(self, a_neck: Neck = Neck()):
        self.neck = a_neck

    def get_tab_from_array(self, chord_array: [str]) -> dict:
        """
        turns ["2", "0", "0", "0", "0", "2"]
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
                tab[string].append("-")

        for string in self.neck.TUNING:
            if chord_array[self.neck.TUNING.index(string)] in ["1", "2", "3", "4", 1, 2, 3, 4]:
                tab[string][int(chord_array[self.neck.TUNING.index(string)])] = "?"
            elif chord_array[self.neck.TUNING.index(string)] in ["0", 0]:
                tab[string][0] = "0"
            elif chord_array[self.neck.TUNING.index(string)] in ["X", -1]:
                tab[string][0] = "X"
            else:
                raise Exception(f"incorrect Fret {chord_array[self.neck.TUNING.index(string)]}")
        return tab

    def get_array_from_tab(self, tab: dict) -> []:
        """
         turns  {
                "e": ["-", "-", "2", "-"],
                "B": ["0", "-", "-", "-"],
                "G": ["0", "-", "-", "-"],
                "D": ["0", "-", "-", "-"],
                "A": ["0", "-", "-", "-"],
                "E": ["-", "-", "2", "-"]
            }
        into ["2", "0", "0", "0", "0", "2"]
        :param tab:
        :return:
        """
        res = ["?", "?", "?", "?", "?", "?"]
        for string in self.neck.TUNING:
            string_index = self.neck.TUNING.index(string)
            if tab[string][0] in ["0", "X"]:
                res[string_index] = tab[string][0]
            else:
                for fret in range(1, len(tab[string]) + 1):
                    if tab[string][fret] != "-":
                        res[string_index] = f"{fret}"
                        break
        return res

    def find_barres(self, chord_layout: [int]) -> {}:
        """
        eg. chord_layout = [1, 3, 3, 2, 1, 1]
        => {"1": [0, 1, 2, 3, 4, 5], "2": [3], "3": [1,2]}
        * keys are the fret numbers
        * lists : the fingered strings numbers
        todo : handle barres with lower frets inside (eg. open G chord)
        :param chord_layout:
        :return:
        """
        barres_found = {}
        for string in Neck.TUNING:
            fret_index = str(chord_layout[Neck.TUNING.index(string)])
            if fret_index not in ["0", "X", "-1"]:
                if fret_index in barres_found.keys():
                    barres_found[fret_index].append(Neck.TUNING.index(string))
                else:
                    barres_found[fret_index] = [Neck.TUNING.index(string)]
        try:
            while "X" in chord_layout: chord_layout.remove("X")
        except Exception:
            pass
        try:
            while -1 in chord_layout: chord_layout.remove(-1)
        except Exception:
            pass
        for fret in range(min(chord_layout), max(chord_layout) + 1):
            s_fret = str(fret)
            if s_fret in barres_found.keys():
                min_f = min(barres_found[s_fret])
                max_f = max(barres_found[s_fret])
                barres_found[s_fret] = []
                for f in range(min_f, max_f + 1):
                    barres_found[s_fret].append(f)
        return barres_found

    def find_finger_layout(self, chord_layout: [int]) -> [chr]:
        """
        finds an appropriate finger layout from a chord
        :param chord_layout:
        :return: X: mute / 0: open / T: thumb / 1: index / 2: major / 3:ring finger / 4: pinky
        """
        if chord_layout in [[0, 0, 0, 0, 0, 0], ["0", "0", "0", "0", "0", "0"],
                            [-1, -1, -1, -1, -1, -1], ["X", "X", "X", "X", "X", "X"]]:
            return self.get_tab_from_array(chord_layout)

        neck_length = self.get_highest_used_neck(chord_layout)
        fret_start = self.get_lowest_used_fret(chord_layout)
        tab = {}
        for string in self.neck.TUNING:
            tab[string] = []
            for fret in range(1, neck_length + 1):
                tab[string].append("-")
        i = 0
        for cell in chord_layout:
            if cell in ["X", -1]:
                tab[self.neck.TUNING[i]][0] = "X"
            elif cell in ["0", 0]:
                tab[self.neck.TUNING[i]][0] = "0"
            else:
                tab[self.neck.TUNING[i]][cell] = "?"
            i += 1

        involved_fingers = 0
        finger_found = False
        barres = self.find_barres(chord_layout)
        keys = sorted(barres.keys())
        for fret in keys:
            for string in barres[fret]:
                f = int(fret)
                if str(tab[Neck.TUNING[string]][f]) == "?":
                    tab[Neck.TUNING[string]][f] = str(f - fret_start + 1)
                    finger_found = True
            if finger_found:
                involved_fingers += 1
        if involved_fingers >= 4:
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
                if fret not in ["X", "-", "?", "0"]:
                    if int(fret) > max_finger:
                        max_finger = int(fret)
        return max_finger

    def fingering_is_possible(self, fret_positions: [int]) -> bool:
        m = self.neck.FRET_QUANTITY + 2
        for fret in fret_positions:
            if fret != 0 and fret < m:
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

    def get_highest_used_neck(self, layout: []):
        chord_layout = layout.copy()
        try:
            while "X" in chord_layout: chord_layout.remove("X")
        except Exception:
            pass
        highest_used_neck = max(chord_layout)
        highest_used_neck = max(self.FINGERING_WIDTH + 1, highest_used_neck + 1)  # +1 due to the nut
        return highest_used_neck

    def get_lowest_used_fret(self, layout: []):
        chord_layout = layout.copy()
        try:
            while "X" in chord_layout: chord_layout.remove("X")
        except Exception:
            pass
        try:
            while -1 in chord_layout: chord_layout.remove(-1)
        except Exception:
            pass
        try:
            while "0" in chord_layout: chord_layout.remove("0")
        except Exception:
            pass
        try:
            while 0 in chord_layout: chord_layout.remove(0)
        except Exception:
            pass
        lowest_used_fret = min(chord_layout)
        return lowest_used_fret
