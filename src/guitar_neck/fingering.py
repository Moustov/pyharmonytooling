from pychord import Chord

from src.guitar_neck.neck_exception import NeckException
from src.guitar_neck.neck import Neck


class Fingering:
    FINGERING_WIDTH = 3
    FINGERING_AVAILABLE_FINGERS = 4
    possible_fingers = ["X", "0", "T", "1", "2", "3", "4"]

    def __init__(self, a_neck: Neck = Neck()):
        self.neck = a_neck

    @staticmethod
    def is_barre_included(chord_layout: [int]) -> bool:
        """
        return True if a barre is int this chord layout
        :param chord_layout:
        :return:
        """
        list_of_cells = []
        for cell in chord_layout:
            if cell not in list_of_cells:
                list_of_cells.append(cell)
            else:
                return True
        return False

    @staticmethod
    def same_fret_same_finger(tab: {}, chord_array: [],
                              string_number_1: int, string_name_1: str,
                              string_number_2: int, string_name_2: str) -> bool:
        """
        is_finger_to_put and same_fret_value and finger_already_set
        :param tab:
        :param chord_array:
        :param string_number_1:
        :param string_name_1:
        :param string_number_2:
        :param string_name_2:
        :return:
        """
        is_finger_to_put = chord_array[string_number_1] not in ["0", "X"]
        fret1 = int(chord_array[string_number_1])
        fret2 = int(chord_array[string_number_2])
        same_fret_value = str(tab[string_name_1][fret1]) == str(tab[string_name_2][fret2])
        finger_already_set = str(tab[string_name_1][int(chord_array[string_number_1])]) != "?"
        return is_finger_to_put and same_fret_value and finger_already_set

    def same_finger_same_fret_with_lower_fingers_between(self, tab: dict, chord_array: []):
        """
        return True if a barre-like fingering appears to be impossible since there are
        strings with lower frets than the barre
        :param chord_array:
        :param tab: the tab to test
        :return:
        """
        for string1 in self.neck.TUNING:
            string_number_1 = self.neck.get_string_position_in_tunning(string1)
            for string2 in self.neck.TUNING:
                if string1 != string2:
                    string_number_2 = self.neck.get_string_position_in_tunning(string2)
                    if chord_array[string_number_1] == chord_array[string_number_2] \
                            and chord_array[string_number_1] not in ["0", "X"]:
                        if self.same_fret_same_finger(tab, chord_array,
                                                      string_number_1, string1,
                                                      string_number_2, string2):
                            # handle strings between the 2 strings with a finger at the same fret
                            string_range = range(self.neck.get_string_position_in_tunning(string1) + 1,
                                                 # skip 1st string
                                                 self.neck.get_string_position_in_tunning(
                                                     string2) + 1)  # include last string
                            for string_between in string_range:
                                if str(chord_array[string_between]) not in ["0", "X"] \
                                        and int(chord_array[string_between]) < int(chord_array[string_number_1]):
                                    return True
        return False

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
            if chord_array[self.neck.get_string_position_in_tunning(string)] in ["1", "2", "3", "4"]:
                tab[string][int(chord_array[self.neck.get_string_position_in_tunning(string)])] = "?"
            elif chord_array[self.neck.get_string_position_in_tunning(string)] == "0":
                tab[string][0] = "0"
            elif chord_array[self.neck.get_string_position_in_tunning(string)] == "X":
                tab[string][0] = "X"
            else:
                raise Exception(f"incorrect Fret {chord_array[self.neck.get_string_position_in_tunning(string)]}")
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
            string_index = self.neck.get_string_position_in_tunning(string)
            if tab[string][0] in ["0", "X"]:
                res[string_index] = tab[string][0]
            else:
                for fret in range(1, len(tab[string]) + 1):
                    if tab[string][fret] != "-":
                        res[string_index] = f"{fret}"
                        break
        return res

    def shift_fingering(self, tab: {}) -> {}:
        chord_array = self.get_array_from_tab(tab)
        for string1 in self.neck.TUNING:
            string_index1 = self.neck.get_string_position_in_tunning(string1)
            for string2 in self.neck.TUNING:
                if string1 != string2:
                    string_index2 = self.neck.get_string_position_in_tunning(string2)
                    if self.same_fingered_fret(chord_array, string_index1, string_index2):
                        if self.same_finger_and_fret_across_strings(tab, chord_array,
                                                                    string1, string_index1,
                                                                    string2, string_index2):
                            s1 = self.neck.get_string_position_in_tunning(string1)
                            s2 = self.neck.get_string_position_in_tunning(string2)
                            for string_index_between in range(min(s1, s2) + 1,
                                                              max(s1, s2)):
                                if self.is_string_index_between_fingered_before_fret(tab, chord_array,
                                                                                     string_index_between,
                                                                                     string_index2):
                                    # set the next finger
                                    the_fret1 = int(chord_array[string_index1])
                                    the_fret2 = int(chord_array[string_index2])
                                    tab[string2][the_fret2] = str(int(tab[string2][the_fret1]) + 1)
                    if chord_array[string_index2] not in ["0", "X", "?"] \
                            and tab[string2][int(chord_array[string_index2])] != "-":
                        # shift fingers
                        new_finger = int(tab[string2][int(chord_array[string_index2])]) + 1
                        if new_finger <= self.FINGERING_AVAILABLE_FINGERS:
                            tab[string2][int(chord_array[string_index2])] = str(new_finger)
                        else:
                            raise NeckException("too many fingers required for this tab")
        return tab

    def find_finger_layout(self, chord_layout: [int]) -> [chr]:
        """
        finds an appropriate finger layout from a chord
        :param chord_layout:
        :return: X: mute / 0: open / T: thumb / 1: index / 2: major / 3:ring finger / 4: pinky
        """
        tab = {}
        neck_length = max(chord_layout)
        neck_length = max(self.FINGERING_WIDTH + 1, neck_length + 1)  # +1 due to the nut
        for string in self.neck.TUNING:
            tab[string] = []
            for fret in range(1, neck_length + 1):
                tab[string].append("-")
        i = 0
        for cell in chord_layout:
            if cell == -1:
                tab[self.neck.TUNING[i]][0] = "X"
            elif cell == 0:
                tab[self.neck.TUNING[i]][0] = "0"
            else:
                tab[self.neck.TUNING[i]][cell] = "?"
            i += 1

        finger = 1
        for fret in range(1, neck_length):
            finger_found = False
            for string in self.neck.TUNING:
                if str(tab[string][fret]) == "?":
                    tab[string][fret] = str(finger)
                    finger_found = True
            if finger_found:
                finger += 1
            if self.same_finger_same_fret_with_lower_fingers_between(tab, chord_layout):
                tab = self.shift_fingering(tab)
                finger = self.get_max_finger(tab) + 1
        if finger >= 6:
            raise NeckException(f"Too many fingers required for the tab {chord_layout}")
        return tab

    @staticmethod
    def same_fingered_fret(chord_array: [int], string_index1: int, string_index2: int):
        """

        :param chord_array:
        :param string_index1:
        :param string_index2:
        :return:
        """
        return chord_array[string_index1] == chord_array[string_index2] and chord_array[string_index1] not in ["0", "X"]

    @staticmethod
    def same_finger_and_fret_across_strings(tab: {}, chord_array: [], string1: str, string_index1: int,
                                            string2: str, string_index2: int):
        """

        :param tab:
        :param chord_array:
        :param string1:
        :param string_index1:
        :param string2:
        :param string_index2:
        :return:
        """
        return tab[string1][int(chord_array[string_index1])] == tab[string2][int(chord_array[string_index2])]

    @staticmethod
    def is_string_index_between_fingered_before_fret(tab: {}, chord_array: [int],
                                                     string_between_index: int,
                                                     reference_string_index: int):
        """

        :param tab:
        :param chord_array:
        :param string_between_index:
        :param reference_string_index:
        :return:
        """
        is_string_fingered = chord_array[string_between_index] not in ["0", "X", "?"]
        is_finger_before = chord_array[string_between_index] < chord_array[reference_string_index]
        cell_is_not_a_dash = tab[Neck.TUNING[string_between_index]][int(chord_array[string_between_index])] != "-"
        return is_string_fingered and is_finger_before and cell_is_not_a_dash

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
                                if self.fingering_is_possible(self.neck.FRET_QUANTITY, fingering_combination):
                                    possible_fingerings.append(fingering_combination)
        return possible_fingerings
