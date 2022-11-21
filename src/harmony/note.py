class Note:
    chromatic_scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    tempered_chromatic_scale = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#",
                                "Fb", "F", "F#", "Gb", "G", "G#"]
    extended_chromatic_scale = ["Abb", "Ab", "A", "A#", "A##", "Bbb", "Bb", "B", "B#", "B##",
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
            index_name = Note.tempered_chromatic_scale.index(self.name)
            if type(other) == Note:
                index_other = Note.tempered_chromatic_scale.index(other.name)
            if type(other) == str:
                index_other = Note.tempered_chromatic_scale.index(other)
            same = (index_name == index_other + 1) \
                    or (index_other == index_name + 1) \
                    or (index_other == len(Note.tempered_chromatic_scale) - 1 and index_name == 0) \
                    or (index_other == 0 and index_name == len(Note.tempered_chromatic_scale) -1)

            return same
