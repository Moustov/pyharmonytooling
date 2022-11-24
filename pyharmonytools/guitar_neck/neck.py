from pychord import Chord


class Neck:
    TUNING = ["E", "A", "D", "G", "B", "e"]
    FRET_QUANTITY_STANDARD = 12
    FRET_QUANTITY_CLASSIC = 18
    FRET_QUANTITY_ELECTRIC = 24
    FRET_QUANTITY = FRET_QUANTITY_STANDARD

    def __init__(self):
        pass

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
            return string
        else:
            res = Chord(string.upper())
            res.transpose(fret)
        return str(res)

    def find_positions_on_string_from_note(self, string: str, note: str) -> [str, int]:
        """
        return all frets on a string that matches the note
        :param string:
        :param note:
        :return:
        """
        res = []
        for fret in range(0, self.FRET_QUANTITY + 2):  # +1 for the nut / +1 to reach the last fret => +2
            if Neck.find_note_from_position(string, fret).upper() == note.upper():
                res.append([string, fret])
        return res

    def find_positions_from_note(self, note: str) -> [[str, int]]:
        """
        provide a list of frets on the neck which match a note
        :param note:
        :return:
        """
        res = []
        for string in self.TUNING:
            positions = self.find_positions_on_string_from_note(string, note)
            for p in positions:
                res.append(p)
        return res
