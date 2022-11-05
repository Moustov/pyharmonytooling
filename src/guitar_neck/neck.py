from pychord import Chord

TUNNING = ["E", "A", "D", "G", "B", "e"]
FRET_QUANTITY_STANDARD = 12
FRET_QUANTITY_CLASSIC = 18
FRET_QUANTITY = FRET_QUANTITY_STANDARD
FINGERING_WIDTH = 3
FINGERING_AVAILABLE_FINGERS = 4


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


def find_positions_on_string_from_note(string: str, note: str) -> [str, int]:
    res = []
    for fret in range(0, FRET_QUANTITY + 1):
        if find_note_from_position(string, fret).upper() == note.upper():
            res.append([string, fret])
    return res


def find_positions_from_note(note: str) -> [[str, int]]:
    """
    provide a list of
    :param note:
    :return:
    """
    res = []
    for string in TUNNING:
        positions = find_positions_on_string_from_note(string, note)
        for p in positions:
            res.append(p)
    return res


def fingering_is_possible(fret_positions: [int]):
    m = min(fret_positions)
    x = max(fret_positions)
    return abs(x - m) <= FINGERING_WIDTH


def get_fingering_from_chord(chord: Chord) -> [[int]]:
    """
    https://www.musicnotes.com/now/tips/how-to-read-guitar-tabs/
    # todo handle muted string with -1
    :param chord:
    :return:
    """
    guitar = {}
    fingerings = []
    chord_positions = {}
    for note in chord.components():
        chord_positions[note] = []
        for string in TUNNING:
            p = find_positions_on_string_from_note(string, note)
            for pos in p:
                chord_positions[note].append(pos)
    for string in TUNNING:
        guitar[string] = []
    for pos in chord_positions.keys():
        for p in chord_positions[pos]:
            guitar[p[0]].append(p[1])
    for string in TUNNING:
        guitar[string].sort()

    for E in guitar["E"]:
        for A in guitar["A"]:
            for D in guitar["D"]:
                for G in guitar["G"]:
                    for B in guitar["B"]:
                        for e in guitar["e"]:
                            fingering = [E, A, D, G, B, e]
                            if fingering_is_possible(fingering):
                                fingerings.append(fingering)
    return fingerings

