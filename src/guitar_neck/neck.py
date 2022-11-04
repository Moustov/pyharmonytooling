from pychord import Chord

TUNNING = ["E", "A", "D", "G", "B", "e"]
FRET_QUANTITY_STANDARD = 12
FRET_QUANTITY_CLASSIC = 18
FRET_QUANTITY = FRET_QUANTITY_STANDARD


def find_note_from_position(string: str, fret: int) -> str:
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


def find_positions_from_note(note: str) -> [str]:
    res = []
    for string in TUNNING:
        for fret in range(0, FRET_QUANTITY+1):
            if find_note_from_position(string, fret).upper() == note.upper():
                res.append([string, fret])
    return res


def get_fingering_from_chord(chord: Chord) -> [[int]]:
    """
    https://www.musicnotes.com/now/tips/how-to-read-guitar-tabs/
    :param chord:
    :return:
    """
    pass
    return [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
