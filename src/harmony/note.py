class Note:
    CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    TEMPERED_CHROMATIC_SCALE = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#",
                                "Fb", "F", "F#", "Gb", "G", "G#"]
    EXTENDED_CHROMATIC_SCALE = ["Abb", "Ab", "A", "A#", "A##", "Bbb", "Bb", "B", "B#", "B##",
                                "Cbb", "Cb", "C", "C#", "C##", "Dbb", "Db", "D", "D#", "D##",
                                "Ebb", "Eb", "E", "E#", "E##", "Fbb", "Fb", "F", "F#", "F##",
                                "Gbb", "Gb", "G", "G#", "G##"]

    def __init__(self, name):
        self.name = name

    def __eq__(self, other) -> bool:
        """
        returns True if same well tempered note (eg: A# == Bb is True
        :param other:
        :return:
        """
        if type(other) == str and self.name == other:
            return True
        if type(other) == Note and self.name == other.name:
            return True
        if "#" or "b" in self.name:
            index_other = -1
            index_name = Note.TEMPERED_CHROMATIC_SCALE.index(self.name)
            if type(other) == Note:
                index_other = Note.TEMPERED_CHROMATIC_SCALE.index(other.name)
            if type(other) == str:
                index_other = Note.TEMPERED_CHROMATIC_SCALE.index(other)
            same = (index_name == index_other + 1) \
                    or (index_other == index_name + 1) \
                    or (index_other == len(Note.TEMPERED_CHROMATIC_SCALE) - 1 and index_name == 0) \
                    or (index_other == 0 and index_name == len(Note.TEMPERED_CHROMATIC_SCALE) - 1)

            return same
