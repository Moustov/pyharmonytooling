from copy import deepcopy

import numpy as np


class Note:
    CONCERT_PITCH = 440
    CHROMATIC_SCALE_SHARP_BASED = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    CHROMATIC_SCALE_FLAT_BASED = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    # https://youtu.be/ZjKyQ7cUlO8?t=730
    CHROMATIC_SCALE_ENHARMONIC_NOTES = ["B#", "Db", "Ebb", "Eb", "Fb", "E#", "Gb", "Abb", "Ab", "Bdd", "Bb", "Cb", ]
    # see https://en.wikipedia.org/wiki/Comma_(music) to make it generic as much as possible
    EXTENDED_CHROMATIC_SCALE = ["Abb", "Ab", "A", "A#", "A##", "Bbb", "Bb", "B", "B#", "B##",
                                "Cbb", "Cb", "C", "C#", "C##", "Dbb", "Db", "D", "D#", "D##",
                                "Ebb", "Eb", "E", "E#", "E##", "Fbb", "Fb", "F", "F#", "F##",
                                "Gbb", "Gb", "G", "G#", "G##"]
    chromatic_frequencies = [0,
                             32.703, 34.648, 36.708, 38.891, 41.203, 43.654, 46.249, 48.999, 51.913, 55.000, 58.270,
                             61.735,
                             65.406, 69.296, 73.416, 77.782, 82.407, 87.307, 92.499, 97.999, 103.830, 110.000, 116.540,
                             123.470,
                             130.810, 138.590, 146.830, 155.560, 164.810, 174.610, 185.000, 196.000, 207.650, 220.000,
                             233.080, 246.940,
                             261.630, 277.180, 293.660, 311.130, 329.630, 349.230, 369.990, 392.000, 415.300, 440.000,
                             466.160, 493.880,
                             523.250, 554.370, 587.330, 622.250, 659.260, 698.460, 739.990, 783.990, 830.610, 880.000,
                             932.330, 987.770,
                             1046.500, 1108.700, 1174.700, 1244.500, 1318.500, 1396.900, 1480.000, 1568.000, 1661.200,
                             1760.000, 1864.700, 1975.500,
                             2093.000, 2217.500, 2349.300, 2489.000, 2637.000, 2793.800, 2960.000, 3136.000, 3322.400,
                             3520.000, 3729.300, 3951.100,
                             4186.000, 4434.900, 4698.600, 4978.000, 5274.000, 5587.700, 5919.900, 6271.900, 6644.900,
                             7040.000, 7458.600, 7902.100,
                             8372.000, 8869.800, 9397.300, 9956.100, 10548.000, 11175.000, 11840.000, 12544.000,
                             13290.000, 14080.000, 14917.000, 15804.000,
                             16744.000, 17740.000, 18795.000, 19912.000, 21096.000, 22351.000, 23680.000, 25088.000,
                             26580.000, 28160.000, 29834.000, 31609.000,
                             9999999999.0]
    notes = {"C": [32.703, 65.406, 130.81, 261.63, 523.25, 1046.5, 2093., 4186., 8372., 16744.],
             "C#": [34.648, 69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5, 4434.9, 8869.8, 17740.],
             "D": [36.708, 73.416, 146.83, 293.66, 587.33, 1174.7, 2349.3, 4698.6, 9397.3, 18795.],
             "D#": [38.891, 77.782, 155.56, 311.13, 622.25, 1244.5, 2489., 4978., 9956.1, 19912.],
             "E": [41.203, 82.407, 164.81, 329.63, 659.26, 1318.5, 2637., 5274., 10548., 21096.],
             "F": [43.654, 87.307, 174.61, 349.23, 698.46, 1396.9, 2793.8, 5587.7, 11175., 22351.],
             "F#": [46.249, 92.499, 185., 369.99, 739.99, 1480., 2960., 5919.9, 11840., 23680.],
             "G": [48.999, 97.999, 196., 392., 783.99, 1568., 3136., 6271.9, 12544., 25088.],
             "G#": [51.913, 103.83, 207.65, 415.3, 830.61, 1661.2, 3322.4, 6644.9, 13290., 26580.],
             "A": [55., 110., 220., 440., 880., 1760., 3520., 7040., 14080., 28160.],
             "A#": [58.27, 116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3, 7458.6, 14917., 29834.],
             "B": [61.735, 123.47, 246.94, 493.88, 987.77, 1975.5, 3951.1, 7902.1, 15804., 31609]
             }
    debug = False
    def __init__(self, name):
        if name[-1].isdigit():
            self.name = name[:-1]
            self.octave = int(name[-1])
        else:
            self.name = name
            self.octave = -1
        if name == "B#":
            self.name = "C"
        elif name == "E#":
            self.name = "F"
        elif name == "Cb":
            self.name = "B"
        elif name == "Fb":
            self.name = "E"
        elif "##" in name:
            index = Note.CHROMATIC_SCALE_SHARP_BASED.index(name[0])
            self.name = Note.CHROMATIC_SCALE_SHARP_BASED[(index + 2) % len(Note.CHROMATIC_SCALE_SHARP_BASED)]
        elif "bb" in name:
            index = Note.CHROMATIC_SCALE_SHARP_BASED.index(name[0])
            self.name = Note.CHROMATIC_SCALE_SHARP_BASED[(index - 2) % len(Note.CHROMATIC_SCALE_SHARP_BASED)]

    def __lt__(self, other):
        interval = self.get_interval_in_half_tones(other)
        if self.octave == -1 and other.octave == -1:
            return interval > 0
        elif self.octave != -1 and other.octave != -1:
            return interval > 0
        else:
            raise ValueError("Cannot compare a raw note with a note with octave")

    def __gt__(self, other):
        interval = self.get_interval_in_half_tones(other)
        return interval < 0

    def __le__(self, other):
        interval = self.get_interval_in_half_tones(other)
        return interval >= 0

    def __ge__(self, other):
        interval = self.get_interval_in_half_tones(other)
        return interval <= 0

    def __str__(self):
        if self.octave == -1:
            return self.name
        else:
            return f"{self.name}{self.octave}"


    def __repr__(self):
        if self.octave == -1:
            return f"<Note: {self.name}>"
        else:
            return f"<Note: {self.name}{self.octave}>"

    def __ne__(self, other):
        if self.octave == -1:
            return not self.__eq__(other)
        else:
            return str(self) != str(other)

    def __eq__(self, other) -> bool:
        """
        returns True if same well tempered note (eg: A# == Bb is True
        :param other:
        :return:
        """
        if not isinstance(other, Note) and not isinstance(other, str):
            raise TypeError(f"Cannot compare Note object with {type(other)} object")
        if isinstance(other, str):
            other = Note(other)
        n1 = self.get_sharp_based_note()
        n2 = other.get_sharp_based_note()
        if n1 == n2 and self.octave == other.octave:
            return True
        else:
            return False

    def get_interval_in_half_tones(self, other) -> int:
        """
        return the number of half tones between self & other
        :param other:
        :return:
        """
        note_other = other
        if not isinstance(other, Note):
            note_other = Note(other)
        index_self = Note.get_index(self.name)
        index_other = Note.get_index(note_other.name)
        if self.octave == -1 and other.octave == -1:
            return index_other - index_self
        elif self.octave != -1 and other.octave != -1:
            return index_other - index_self + (note_other.octave - self.octave) * 12
        else:
            raise ValueError("Cannot get interval from a raw note and a note with octave")

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

    def transpose(self, number_half_tone: int) -> str:
        """
        Transposes the note with number_half_tone
        if note with octave transposed out of [0..9] band => ValueError exception raised
        :param number_half_tone:
        :return:
        """
        if self.debug:
            print(f"Note<{str(self)}>.transpose({number_half_tone})")
        n = self.get_sharp_based_note()
        pos = Note.CHROMATIC_SCALE_SHARP_BASED.index(n)

        if self.octave != -1:
            self.octave += (pos + number_half_tone) // 12
            if self.octave < 0 or self.octave >= 9:
                raise ValueError(f"Could not transpose: note transposition out of octave band "
                                 f"- {self.name}{self.octave} not in [0..9]")
        pos += number_half_tone
        pos = pos % len(Note.CHROMATIC_SCALE_SHARP_BASED)
        self.name = Note.CHROMATIC_SCALE_SHARP_BASED[pos]
        if self.octave == -1:
            return f"{self.name}"
        else:
            return f"{self.name}{self.octave}"

    def get_sharp_based_note(self):
        """
        returns the note name with sharps instead of flats
        :return:
        """
        if 'b' in self.name:
            return Note.CHROMATIC_SCALE_SHARP_BASED[Note.CHROMATIC_SCALE_FLAT_BASED.index(self.name)]
        return self.name

    @staticmethod
    def find_closest_note(pitch) -> (str, float):
        """
        This function finds the closest note for a given pitch
        Parameters:
        pitch (float): pitch given in hertz
        Returns:
        closest_note (str): e.g. A, G#, ..
        closest_pitch (float): pitch of the closest note in hertz
        Copyright (c) 2021 chciken - See https://www.chciken.com/digital/signal/processing/2020/05/13/guitar-tuner.html

        todo Ab and G# are not the same: https://www.youtube.com/watch?v=tGEXJe3px68
        """
        notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        i = int(np.round(np.log2(pitch / Note.CONCERT_PITCH) * 12))
        closest_note_name = notes[i % 12] + str(3 + (i + 9) // 12)
        closest_pitch = Note.CONCERT_PITCH * 2 ** (i / 12)
        return closest_note_name, closest_pitch
