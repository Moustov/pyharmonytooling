from src.guitar_neck.neck_exception import NeckException
from src.guitar_neck.neck import Neck


class Fingering:
    possible_fingers = ["X", "0", "T", "1", "2", "3", "4"]

    def __init__(self):
        self.neck = Neck()

    def is_barre_included(self, chord_layout: [int]) -> bool:
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
        return True if a barre-like fingering appears to be impossible since there are strings with lower frets than the barre
        :param chord_array:
        :param tab: the tab to test
        :return:
        """
        for string1 in self.neck.TUNNING:
            string_number_1 = self.neck.get_string_position_in_tunning(string1)
            for string2 in self.neck.TUNNING:
                if string1 != string2:
                    string_number_2 = self.neck.get_string_position_in_tunning(string2)
                    if chord_array[string_number_1] == chord_array[string_number_2] \
                            and chord_array[string_number_1] not in ["0", "X"]:
                        if self.same_fret_same_finger(tab, chord_array,
                                                      string_number_1, string1,
                                                      string_number_2, string2):
                            string_range = range(self.neck.get_string_position_in_tunning(string1) + 1,  # skip 1st string
                                                 self.neck.get_string_position_in_tunning(
                                                     string2) + 1)  # include last string
                            for string_between in string_range:
                                if str(chord_array[string_between]) == "X" \
                                        or int(chord_array[string_between]) < int(chord_array[string_number_1]):
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
        for string in self.neck.TUNNING:
            tab[string] = []
            for fret in range(1, self.neck.FINGERING_WIDTH + 2):
                tab[string].append("-")

        for string in self.neck.TUNNING:
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
        res = []
        for string in self.neck.TUNNING:
            for fret in range(0, len(tab[string])):
                if tab[string][fret] != "-":
                    res.append(tab[string][fret])
        return res

    def shift_fingering(self, fret: int, tab: {}):
        chord_array = self.get_array_from_tab(tab)
        for string1 in self.neck.TUNNING:
            index1 = self.neck.get_string_position_in_tunning(string1)
            for string2 in self.neck.TUNNING:
                if string1 != string2:
                    index2 = self.neck.get_string_position_in_tunning(string2)
                    if chord_array[index1] == chord_array[index2] and chord_array[index1] not in ["0", "X"]:
                        if tab[string1][int(chord_array[index1])] == tab[string2][int(chord_array[index2])]:
                            for string_between in range(self.neck.get_string_position_in_tunning(string1) + 1,
                                                        self.neck.get_string_position_in_tunning(string2)):
                                if chord_array[string_between] == "X" \
                                        or chord_array[string_between] < chord_array[index1]:
                                    # set the next finger
                                    tab[string2][index2] = tab[string2][index1] + 1
                    if chord_array[index2] not in ["0", "X", "?"]:
                        # shift fingers
                        new_finger = int(tab[string2][index2]) + 1
                        if new_finger > 4:  # todo set as constant
                            tab[string2][index2] = str(new_finger)
                        else:
                            raise NeckException("too many fingers required for this tab")

    def find_finger_layout(self, chord_layout: [int]) -> [chr]:
        """
        finds an appropriate finger layout from a chord
        :param chord_layout:
        :return: X: mute / 0: open / T: thumb / 1: index / 2: major / 3:ring finger / 4: pinky
        """
        tab = {}
        neck_length = max(chord_layout)
        neck_length = max(self.neck.FINGERING_WIDTH + 1, neck_length + 1)  # +1 due to the nut
        for string in self.neck.TUNNING:
            tab[string] = []
            for fret in range(1, neck_length + 1):
                tab[string].append("-")
        i = 0
        for cell in chord_layout:
            if cell == -1:
                tab[self.neck.TUNNING[i]][0] = "X"
            elif cell == 0:
                tab[self.neck.TUNNING[i]][0] = "0"
            else:
                tab[self.neck.TUNNING[i]][cell] = "?"
            i += 1

        finger = 1
        for fret in range(1, neck_length):
            for string in self.neck.TUNNING:
                if str(tab[string][fret]) == "?":
                    tab[string][fret] = str(finger)
                    finger += 1
            if self.same_finger_same_fret_with_lower_fingers_between(tab, chord_layout):
                tab = self.shift_fingering(fret, tab)
        if finger >= 6:
            raise NeckException(f"Too many fingers required for the tab {chord_layout}")
        return tab
