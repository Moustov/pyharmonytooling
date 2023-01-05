class Note:
    CHROMATIC_SCALE_SHARP_BASED = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    CHROMATIC_SCALE_FLAT_BASED = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    # https://youtu.be/ZjKyQ7cUlO8?t=730
    CHROMATIC_SCALE_ENHARMONIC_NOTES = ["Bdd", "Bb", "Cb", "B#", "Db", "Ebb", "Eb", "Fb", "E#", "Gb", "Abb", "Ab"]
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Note: {self.name}>"

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other) -> bool:
        """
        returns True if same well tempered note (eg: A# == Bb is True
        :param other:
        :return:
        """
        if not isinstance(other, Note) and not isinstance(other, str):
            raise TypeError(f"Cannot compare Note object with {type(other)} object")
        if type(other) == str and self.name == other:
            return True
        elif type(other) == Note and self.name == other.name:
            return True
        distance = self.get_interval_in_half_tones(other)
        return distance == 0

    def get_interval_in_half_tones(self, other) -> int:
        """
        return the number of half tones between self & other
        :param other:
        :return:
        """
        if not isinstance(other, Note) and not isinstance(other, str):
            raise TypeError(f"Cannot compare Note object with {type(other)} object")
        s_self = str(self)
        index_self = Note.get_index(s_self)
        s_other = str(other)
        index_other = Note.get_index(s_other)
        return index_other - index_self

    @staticmethod
    def get_index(note_name):
        """
        returns the internal position of the note_name
        :param note_name:
        :return:
        """
        if not isinstance(note_name, Note) and not isinstance(note_name, str):
            raise TypeError(f"Cannot compare Note object with {type(note_name)} object")
        index_note = -1
        if "#" in note_name:
            try:
                index_note = Note.CHROMATIC_SCALE_SHARP_BASED.index(note_name)
            except:
                index_note = Note.CHROMATIC_SCALE_ENHARMONIC_NOTES.index(note_name)
        else:
            try:
                index_note = Note.CHROMATIC_SCALE_FLAT_BASED.index(note_name)
            except:
                try:
                    index_note = Note.CHROMATIC_SCALE_ENHARMONIC_NOTES.index(note_name)
                except:
                    pass
        if index_note == -1:
            raise ValueError(f"{note_name} is not a known note...")
        return index_note

    @staticmethod
    def equivalents(note: str) -> []:
        """
        if the note is flat => the sharp will also be part of the returned list
        ex  equivalents("Ab") => ["Ab", "G#"]
            equivalents("A") => ["A"]
        :param note:
        :return:
        """
        if "b" in note:
            return [note, Note.CHROMATIC_SCALE_SHARP_BASED[Note.CHROMATIC_SCALE_FLAT_BASED.index(note)]]
        elif "#" in note:
            return [note, Note.CHROMATIC_SCALE_FLAT_BASED[Note.CHROMATIC_SCALE_SHARP_BASED.index(note)]]
        else:
            return [note]

