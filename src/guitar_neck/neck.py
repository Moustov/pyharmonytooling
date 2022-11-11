from pychord import Chord

class Neck:
    TUNNING = ["E", "A", "D", "G", "B", "e"]
    FRET_QUANTITY_STANDARD = 12
    FRET_QUANTITY_CLASSIC = 18
    FRET_QUANTITY = FRET_QUANTITY_STANDARD
    FINGERING_WIDTH = 3
    FINGERING_AVAILABLE_FINGERS = 4

    def __init__(self):
        pass

    def get_string_position_in_tunning(self, string: str) -> int:
        if string == "E": return 0
        if string == "A": return 1
        if string == "D": return 2
        if string == "G": return 3
        if string == "B": return 4
        if string == "e": return 5

    def find_note_from_position(self, string: str, fret: int) -> str:
        """
        https://www.musicnotes.com/now/tips/how-to-read-guitar-tabs/
        :param fret:
        :param string:
        :return:
        """
        if fret == 0:
            return string
        else:
            res = Chord(string.upper())
            res.transpose(fret)
        return str(res)

    def find_positions_on_string_from_note(self, string: str, note: str) -> [str, int]:
        res = []
        for fret in range(0, self.FRET_QUANTITY + 1):
            if self.find_note_from_position(string, fret).upper() == note.upper():
                res.append([string, fret])
        return res

    def find_positions_from_note(self, note: str) -> [[str, int]]:
        """
        provide a list of
        :param note:
        :return:
        """
        res = []
        for string in self.TUNNING:
            positions = self.find_positions_on_string_from_note(string, note)
            for p in positions:
                res.append(p)
        return res

    def fingering_is_possible(self, fret_positions: [int]):
        m = min(fret_positions)
        x = max(fret_positions)
        return abs(x - m) <= self.FINGERING_WIDTH

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
            for string in self.TUNNING:
                p = self.find_positions_on_string_from_note(string, note)
                for pos in p:
                    chord_positions[note].append(pos)
        for string in self.TUNNING:
            guitar[string] = []
        for pos in chord_positions.keys():
            for p in chord_positions[pos]:
                guitar[p[0]].append(p[1])
        for string in self.TUNNING:
            guitar[string].sort()

        for E in guitar["E"]:
            for A in guitar["A"]:
                for D in guitar["D"]:
                    for G in guitar["G"]:
                        for B in guitar["B"]:
                            for e in guitar["e"]:
                                fingering = [E, A, D, G, B, e]
                                if self.fingering_is_possible(fingering):
                                    possible_fingerings.append(fingering)
        return possible_fingerings

