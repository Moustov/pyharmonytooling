from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.note import Note


class Degree:
    def __init__(self):
        pass

    @staticmethod
    def get_chord_from_degree(degree, root_note, mode: CircleOf5th) -> str:
        """
        return a chord name from a degree + root note
        :param mode: the CircleOf5th will provide intervals
        :param degree:
        :param root_note:
        :return:
        """
        if degree.startswith("iii"):
            note = Degree.get_note_degree(root_note, 3, mode)
            return f"{note}m{degree[3:]}"
        if degree.startswith("ii"):
            note = Degree.get_note_degree(root_note, 2, mode)
            return f"{note}m{degree[2:]}"
        if degree.startswith("iv"):
            note = Degree.get_note_degree(root_note, 4, mode)
            return f"{note}m{degree[2:]}"
        if degree.startswith("i"):
            note = Degree.get_note_degree(root_note, 1, mode)
            return f"{note}m{degree[1:]}"
        if degree.startswith("vii"):
            note = Degree.get_note_degree(root_note, 7, mode)
            return f"{note}m{degree[3:]}"
        if degree.startswith("vi"):
            note = Degree.get_note_degree(root_note, 6, mode)
            return f"{note}m{degree[2:]}"
        if degree.startswith("v"):
            note = Degree.get_note_degree(root_note, 5, mode)
            return f"{note}m{degree[1:]}"

        if degree.startswith("III"):
            note = Degree.get_note_degree(root_note, 3, mode)
            return note + degree[3:]
        if degree.startswith("II"):
            note = Degree.get_note_degree(root_note, 2, mode)
            return note + degree[2:]
        if degree.startswith("IV"):
            note = Degree.get_note_degree(root_note, 4, mode)
            return note + degree[2:]
        if degree.startswith("I"):
            note = Degree.get_note_degree(root_note, 1, mode)
            return note + degree[1:]
        if degree.startswith("VII"):
            note = Degree.get_note_degree(root_note, 7, mode)
            return note + degree[3:]
        if degree.startswith("VI"):
            note = Degree.get_note_degree(root_note, 6, mode)
            return note + degree[2:]
        if degree.startswith("V"):
            note = Degree.get_note_degree(root_note, 5, mode)
            return note + degree[1:]

    @staticmethod
    def get_note_degree(root_note: str, degree: int, mode: CircleOf5th) -> int:
        """

        :param mode: the CircleOf5th will provide intervals
        :param root_note: from CircleOf5th.chromatic_scale
        :param degree: 1 to 7
        :return:
        """
        nb_half_tones = 0
        for i in range(0, degree - 1):
            nb_half_tones += mode.intervals[i]
        if root_note in Note.CHROMATIC_SCALE_SHARP_BASED:
            index = (Note.CHROMATIC_SCALE_SHARP_BASED.index(root_note) + nb_half_tones) % len(Note.CHROMATIC_SCALE_SHARP_BASED)
            return Note.CHROMATIC_SCALE_SHARP_BASED[index]
        if root_note in Note.CHROMATIC_SCALE_FLAT_BASED:
            index = (Note.CHROMATIC_SCALE_FLAT_BASED.index(root_note) + nb_half_tones) % len(Note.CHROMATIC_SCALE_FLAT_BASED)
            return Note.CHROMATIC_SCALE_FLAT_BASED[index]
        if root_note in Note.CHROMATIC_SCALE_ENHARMONIC_NOTES:
            index = (Note.CHROMATIC_SCALE_ENHARMONIC_NOTES.index(root_note) + nb_half_tones) % len(Note.CHROMATIC_SCALE_ENHARMONIC_NOTES)
            return Note.CHROMATIC_SCALE_ENHARMONIC_NOTES[index]
        if root_note in Note.EXTENDED_CHROMATIC_SCALE:
            index = (Note.EXTENDED_CHROMATIC_SCALE.index(root_note) + nb_half_tones) % len(Note.EXTENDED_CHROMATIC_SCALE)
            return Note.EXTENDED_CHROMATIC_SCALE[index]
        raise ValueError(f"The note '{root_note}' could be found in any scale")
