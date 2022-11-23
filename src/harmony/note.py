class Note:
    CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    TEMPERED_CHROMATIC_SCALE = {"Ab": 1, "A": 1, "A#": 0, "Bb": 1, "B": 0,
                                "Cb": 1, "C": 1, "C#": 0, "Db": 1, "D": 1, "D#": 0,
                                "Eb": 1, "E": 0, "Fb": 1, "F": 1, "F#": 0,
                                "Gb": 1, "G": 1, "G#": 0}
    # see https://en.wikipedia.org/wiki/Comma_(music) to make it generic as much as possible
    EXTENDED_CHROMATIC_SCALE = ["Abb", "Ab", "A", "A#", "A##", "Bbb", "Bb", "B", "B#", "B##",
                                "Cbb", "Cb", "C", "C#", "C##", "Dbb", "Db", "D", "D#", "D##",
                                "Ebb", "Eb", "E", "E#", "E##", "Fbb", "Fb", "F", "F#", "F##",
                                "Gbb", "Gb", "G", "G#", "G##"]

    def __init__(self, name):
        self.name = name
        if name == "B#":
            self.name = "C"
        if name == "E#":
            self.name = "F"

    def __eq__(self, other) -> bool:
        """
        returns True if same well tempered note (eg: A# == Bb is True
        :param other:
        :return:
        """
        if type(other) == str and self.name == other:
            return True
        elif type(other) == Note and self.name == other.name:
            return True
        distance = self.get_interval_in_half_tones(other)
        return distance == 0

    def get_interval_in_half_tones(self, other) -> int:
        """
        return the number of half tones between self & other
        :type note: Note
        :param note:
        :return:
        """
        tempered_scale = list(Note.TEMPERED_CHROMATIC_SCALE.keys())
        index_name = tempered_scale.index(self.name)
        if type(other) == Note:
            index_other = tempered_scale.index(other.name)
        elif type(other) == str:
            index_other = tempered_scale.index(other)
        nb_half_tones = 0
        if index_other < index_name:
            for n in tempered_scale[index_other: index_name]:
                nb_half_tones += Note.TEMPERED_CHROMATIC_SCALE[n]
            nb_half_tones -= 12
        else:
            for n in tempered_scale[index_name:index_other]:
                nb_half_tones += Note.TEMPERED_CHROMATIC_SCALE[n]
        if nb_half_tones >= 0:
            return nb_half_tones % 12
        else:
            return nb_half_tones % -12
