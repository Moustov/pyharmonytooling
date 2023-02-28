from pychord import Chord

from pyharmonytools.harmony.note import Note


class Neck:
    TUNING = ["E", "A", "D", "G", "B", "e"]
    FRET_QUANTITY_STANDARD = 12
    FRET_QUANTITY_CLASSIC = 18
    FRET_QUANTITY_ELECTRIC = 24
    FRET_QUANTITY = FRET_QUANTITY_STANDARD
    # https://imgur.com/gallery/82gqBVW
    OCTAVES_ON_NECK = """0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18
e	4	4	4	4	4	4	4	4	4	4	4	4	5	5	5	5	5	5	5
B	3	4	4	4	4	4	4	4	4	4	4	4	4	5	5	5	5	5	5
G	3	3	3	3	3	4	4	4	4	4	4	4	4	4	4	4	4	4	4
D	3	3	3	3	3	3	3	3	3	3	4	4	4	4	4	4	4	4	4
A	2	2	2	3	3	3	3	3	3	3	3	3	3	3	4	4	4	4	4
E	2	2	2	2	2	2	2	2	3	3	3	3	3	3	3	3	3	3	3
"""

    def __init__(self):
        self.octave = {}
        lines = self.OCTAVES_ON_NECK.split("\n")
        for s in self.TUNING:
            self.octave[s] = {}
            frets = lines[len(self.TUNING) - self.TUNING.index(s)].split()
            for fret in range(0, len(frets)-1):
                self.octave[s][fret] = int(frets[fret+1])

    @staticmethod
    def find_note_from_position(string: str, fret: int) -> str:
        """
        https://www.musicnotes.com/now/tips/how-to-read-guitar-tabs/
        # todo involve self.TUNING to alter the note
        :param fret:
        :param string:
        :return:
        """
        if fret == 0:
            return string.upper()
        else:
            res = Chord(string.upper())
            res.transpose(fret)
        return str(res)

    def find_positions_on_string_from_note(self, string: str, note: str, octave: int = -1) -> [str, int]:
        """
        return all frets on a string that matches the note
        :param octave:
        :param string:
        :param note:
        :return:
        """
        res = []
        for fret in range(0, self.FRET_QUANTITY + 2):  # +1 for the nut / +1 to reach the last fret => +2
            neck_note = Neck.find_note_from_position(string, fret)
            if Note(neck_note) == Note(note):
                if octave == -1:
                    res.append([string, fret])
                elif octave == self.octave[string][fret]:
                    res.append([string, fret])

        return res

    def find_positions_from_note(self, note: str, octave: int = -1) -> [[str, int]]:
        """
        provide a list of frets on the neck which match a note
        :param octave:
        :param note:
        :return:
        """
        res = []
        for string in self.TUNING:
            positions = self.find_positions_on_string_from_note(string, note, octave)
            for p in positions:
                res.append(p)
        return res
