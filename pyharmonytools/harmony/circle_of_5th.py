from pychord import ChordProgression, Chord

from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.harmony.note import Note


def chord_note_included_in_chord_list(chord_song: Chord, chord_list: [Chord]) -> bool:
    """
    handle tempered equivalence with Note.__eq__()
    :param chord_song:
    :param chord_list:
    :return:
    """
    for c in chord_list:
        # if CofChord.is_chord_included_from_components(chord_song, c):
        if CofChord.is_same_chord_from_components(chord_song, c):
            return True
    return False


class CircleOf5th:

    def __init__(self):
        self.cof_name = "circle name"
        self.intervals = []
        self.qualities = []
        self.cof_scales = None
        self.cycle_sequence = ["C", "G", "D", "E", "A", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
        self.cof_tone_compliances = {self.cof_name: {}}
        self.compliance_level = 0
        self.borrowed_chords_level = 0
        self.compliant_chords_qty = 0
        self.borrowed_chords_qty = 0

    @staticmethod
    def cof_factory(cof_name: str) -> object:
        if cof_name == "Natural Major - 4 notes":
            return CircleOf5thNaturalMajor_4notes()
        if cof_name == "Natural Major - triads":
            return CircleOf5thNaturalMajor_triads()
        if cof_name == "Harmonic Major - 4 notes":
            return CircleOf5thHarmonicMajor_4notes()
        if cof_name == "Harmonic Major - triads":
            return CircleOf5thHarmonicMajor_triads()
        if cof_name == "Harmonic Minor - 4 notes":
            return CircleOf5thHarmonicMinor_4notes()
        if cof_name == "Harmonic Minor - triads":
            return CircleOf5thHarmonicMinor_triads()
        if cof_name == "Melodic Minor - 4 notes":
            return CircleOf5thMelodicMinor_4notes()
        if cof_name == "Melodic Minor - triads":
            return CircleOf5thMelodicMinor_triads()
        if cof_name == "Natural Minor - 4 notes":
            return CircleOf5thNaturalMinor_4notes()
        if cof_name == "Natural Minor - triads":
            return CircleOf5thNaturalMinor_triads()

    def get_compliance_note_presence(self, tone: [str], cp: ChordProgression) -> float:
        """
        todo distance with notes
        if the note is present => the chord will fully count
        :param tone:
        :param cp:
        :return:
        """
        return 0.0

    def get_compliance_chord_frequency(self, tone: [str], cp: ChordProgression) -> float:
        """
        todo distance with tone is based on the amount of chord presence:
        if the chord is present => the chord will count regarding its use in the cp
        :param tone:
        :param cp:
        :return:
        """
        return 0.0

    def get_compliance_chord_presence(self, harmonic_suite_chords: [str], chords: ChordProgression,
                                      cof_name: str, tonality: str) -> float:
        """
        the distance is binary : if the chord is present => the chord will fully count
        :param harmonic_suite_chords:
        :param chords:
        :return: 0.0 --> 1.0 (100% compliant)
        """
        # init - synthesis of used chords in cp for quicker analysis
        tone_compliance = {}
        compliant_chords = []
        chord_song_list = {}
        chord_list = []
        for cs in chords:
            if not CofChord.is_chord_in_array(cs, chord_list):
                chord_song_list[str(cs)] = 1
                chord_list.append(cs)
            else:
                chord_song_list[str(cs)] += 1

        # check each chord in the tone and see if colored versions of the chord is used in chord_song_list
        self.cof_tone_compliances[cof_name][tonality] = {}
        self.compliance_level = 0
        self.borrowed_chords_level = 0
        self.compliant_chords_qty = 0
        self.borrowed_chords_qty = 0
        for chord_song in chord_song_list:
            chord_tone_found = False
            for chord_tonality in harmonic_suite_chords:
                ct = Chord(chord_tonality)
                cs = Chord(chord_song)
                if self.is_chord_in_tonality(ct, cs):
                    self.cof_tone_compliances[cof_name][tonality][chord_song] = chord_song_list[chord_song]
                    self.compliance_level += chord_song_list[chord_song]
                    self.compliant_chords_qty += 1
                    chord_tone_found = True
                    break
            if not chord_tone_found:
                self.cof_tone_compliances[cof_name][tonality][chord_song] = -chord_song_list[chord_song]
                self.borrowed_chords_qty += 1
                self.borrowed_chords_level += abs(chord_song_list[chord_song])

        if self.compliance_level == 0 or self.compliant_chords_qty == 0:
            # nothing in common
            return 0.0
        elif len(self.cof_tone_compliances[cof_name][tonality]) >= len(chord_song_list) == self.compliant_chords_qty:
            # all song chords are used and belong to the tonality
            return 1.0
        # elif len(chord_song_list) <= len(self.cof_tone_compliances[cof_name][tone]) and borrowed_chords_qty == 0:
        #     # the whole song is in the tone
        #     return 100.0
        else:
            return (self.compliance_level - self.borrowed_chords_level) / len(chords)

    def is_chord_in_tonality(self, chord_tonality: Chord, chord_song: Chord) -> bool:
        """
        useful when trying to see if a chord song is in a tonality
        :param chord_tonality:
        :param chord_song:
        :return:
        """
        # handles flat & sharp equivalents
        eqv = Note(chord_tonality.root).equivalents(chord_song.root)
        same_root = False
        for n in eqv:
            if str(n) == chord_tonality.root:
                same_root = True
                break

        if same_root:
            if chord_tonality.quality.quality == chord_song.quality.quality:
                return True
            if chord_tonality.quality.quality.startswith("dim") and chord_song.quality.quality.startswith("dim"):
                return True
            elif chord_tonality.quality.quality.startswith("maj7") and chord_song.quality.quality.startswith("maj7"):
                return True
            else:
                if chord_tonality.quality.quality.startswith("m") \
                        and chord_song.quality.quality.startswith("m") \
                        and not chord_tonality.quality.quality.startswith("maj7") \
                        and not chord_song.quality.quality.startswith("maj7"):
                    return True
                elif not chord_tonality.quality.quality.startswith("m") \
                        and not chord_song.quality.quality.startswith("m"):
                    if not chord_tonality.quality.quality.startswith("dim") \
                        and not chord_song.quality.quality.startswith("dim"):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
        # alternative technical solution:
        # possible_chord_qualities = CofChord.get_chord_names_possible_qualities(chord_tone)
        # return chord_note_included_in_chord_list(Chord(chord_song), possible_chord_qualities)

    def get_borrowed_chords(self, song_chord_progression: ChordProgression, cof_name: str, tonality: str) -> [str]:
        """
        returns borrowed chords the song_chord_progression involves from a given CoF + tonality
        :param cof_name:
        :param tonality:
        :param song_chord_progression:
        :return:
        """
        borrowed_chords = []
        if self.cof_tone_compliances[cof_name] == {}:
            self.digest_possible_tones_and_modes(song_chord_progression)
        for chord_name in self.cof_tone_compliances[cof_name][tonality]["chords"].keys():
            if self.cof_tone_compliances[cof_name][tonality]["chords"][chord_name] < 0:
                borrowed_chords.append(chord_name)
        return borrowed_chords

    def digest_song(self, song: str) -> ChordProgression:
        """
        return a ChordProgression object from a song
        todo make sure the captured chords are chords, not words (eg. "am", "a", ...)
        :param song:
        :return:
        """
        cp = None
        possible_chords = []
        lines = song.split("\n")
        for line in lines:
            words = line.split(" ")
            for w in words:
                if w != "":
                    try:
                        chord = CofChord.get_chord_from_harmonic_and_enharmonic(w)
                        c = Chord(chord)
                        possible_chords.append(chord)
                    except:  # todo handle exception differently because it should not happen
                        print(f"Issue to digest chord {chord} with PyChord")
        cp = ChordProgression(possible_chords)
        return cp

    def generate_circle_of_fifths(self) -> dict:
        """
        generates a circle of fifths from intervals, qualities
        :return:
        """
        intervals = self.intervals.copy()
        intervals.append(0)
        res = {}
        for seq in self.cycle_sequence:
            res[seq] = []
            current_note = seq
            for interval, quality in zip(intervals, self.qualities):
                res[seq].append(f"{current_note}{quality}")
                current_note = self.get_next_note(current_note, interval)
        return res

    def reset_digested_compliance_levels(self):
        """
        reset the self.cof_tone_compliances
        :return:
        """
        self.cof_tone_compliances = {}

    def digest_tone_compliancy_with_circle_of_fifth(self, cp: ChordProgression) -> []:
        """
        returns the compliance level max.
        all compliance levels are stored in self.cof_tone_compliances
        :param cp:
        :return: [probability, note, circle name, scale]
        """
        compliance_level_max = {"compliance_rate": -9999, "tone": "?", "cof_name": "?", "scale": [], "harmonic suite": [], "intervals": []}
        compliance_rate = 0
        for tone in self.cof_scales:
            _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"Check tone {str(tone)} in {self.cof_name}")
            compliance_rate = self.get_compliance_chord_presence(self.cof_scales[tone], cp, self.cof_name, tone)
            _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"   -> {tone}, {compliance_rate * 100}%")
            self.cof_tone_compliances[self.cof_name][tone] = {"compliance_rate": compliance_rate,
                                                              "tone": tone, "cof_name": self.cof_name,
                                                              "scale": self.get_scale(tone),
                                                              "harmonic suite": self.cof_scales[tone],
                                                              "chords": self.cof_tone_compliances[self.cof_name][tone],
                                                              "compliance_level": self.compliance_level,
                                                              "borrowed_chords_level": self.borrowed_chords_level,
                                                              "compliant_chords_qty": self.compliant_chords_qty,
                                                              "borrowed_chords_qty": self.borrowed_chords_qty,
                                                              "intervals": []
                                                              }
            if compliance_rate > compliance_level_max["compliance_rate"]:
                compliance_level_max = self.cof_tone_compliances[self.cof_name][tone]
        return compliance_level_max

    def digest_possible_tones_and_modes(self, cp: ChordProgression) -> dict:
        """
        return the most probable tone of a ChordProgression across possible circle of 5th.
        all compatibility values are stored in self.cof_tone_compliances, the best possible guess is returned.
        :param cp:
        :return: {"compliance_rate": 0, "tone": "?", "cof_name": "?", "scale": [], "harmonic suite": [], "intervals": []}
        """
        best_tone = {"compliance_rate": 0, "tone": "?", "cof_name": "?", "scale": [], "harmonic suite": [], "intervals": []}

        cof_nat_maj = CircleOf5thNaturalMajor_4notes()
        guess = cof_nat_maj.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_nat_maj.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_nat_maj = CircleOf5thNaturalMajor_triads()
        guess = cof_nat_maj.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_nat_maj.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_har_major = CircleOf5thHarmonicMajor_4notes()
        guess = cof_har_major.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_har_major.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_har_major = CircleOf5thHarmonicMajor_triads()
        guess = cof_har_major.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_har_major.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_mel_minor = CircleOf5thMelodicMinor_4notes()
        guess = cof_mel_minor.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_mel_minor.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_mel_minor = CircleOf5thMelodicMinor_triads()
        guess = cof_mel_minor.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_mel_minor.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_nat_min = CircleOf5thNaturalMinor_4notes()
        guess = cof_nat_min.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_nat_min.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_nat_min = CircleOf5thNaturalMinor_triads()
        guess = cof_nat_min.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_nat_min.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_harm_minor = CircleOf5thHarmonicMinor_4notes()
        guess = cof_harm_minor.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_harm_minor.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess

        cof_harm_minor = CircleOf5thHarmonicMinor_triads()
        guess = cof_harm_minor.digest_tone_compliancy_with_circle_of_fifth(cp)
        self.cof_tone_compliances = {**self.cof_tone_compliances, **cof_harm_minor.cof_tone_compliances}
        if guess["compliance_rate"] > best_tone["compliance_rate"]:
            best_tone = guess
        # print(self.cof_tone_compliances)
        return best_tone

    def get_next_note(self, current_note: str, interval: int) -> str:
        """
        return the current note name + interval
        :param current_note:
        :param interval: number of semitones
        :return:
        """
        current_chord = Chord(current_note)
        current_chord.transpose(interval)
        return str(current_chord)

    def get_scale(self, tone: str) -> [str]:
        """
        returns the scale of this circle of 5th from the tone
        :param tone:
        :return:
        """
        scale = [tone]
        current_note = tone
        for i in self.intervals:
            next_note = self.get_next_note(current_note, i)
            scale.append(next_note)
            current_note = next_note
        return scale


class CircleOf5thNaturalMajor_4notes(CircleOf5th):
    def __init__(self):
        super().__init__()
        self.cof_name = "Natural Major - 4 notes"
        self.intervals = [2, 2, 1, 2, 2, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["maj7", "m7", "m7", "maj7", "7", "m7", "m7b5"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thNaturalMajor_triads(CircleOf5th):
    # aka "Church more
    def __init__(self):
        super().__init__()
        self.cof_name = "Natural Major - triads"
        self.intervals = [2, 2, 1, 2, 2, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["", "m", "m", "", "", "m", "dim"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thChurchMode_4notes(CircleOf5thNaturalMajor_4notes):
    def __init__(self):
        super().__init__()
        self.cof_name = "Church mode - 4 notes"


class CircleOf5thChurchMode_triads(CircleOf5thNaturalMajor_triads):
    def __init__(self):
        super().__init__()
        self.cof_name = "Church mode - triads"


class CircleOf5thHarmonicMajor_4notes(CircleOf5th):
    def __init__(self):
        super().__init__()
        self.cof_name = "Harmonic Major - 4 notes"
        self.intervals = [2, 2, 1, 2, 1, 3]
        self.qualities = ["maj7", "m7b5", "m7", "mM7", "7", "M7+5", "dim7"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thHarmonicMajor_triads(CircleOf5th):
    def __init__(self):
        super().__init__()
        self.cof_name = "Harmonic Major - triads"
        self.intervals = [2, 2, 1, 2, 1, 3]
        self.qualities = ["", "dim", "m", "m", "", "5", "dim"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thNaturalMinor_4notes(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    https://www.study-guitar.com/blog/minor-key-chord-progressions/
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Natural Minor - 4 notes"
        self.intervals = [2, 1, 2, 2, 1, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["m", "dim7", "", "m", "m", "", ""]    # todo refine the 4 notes CoF
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thNaturalMinor_triads(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    https://www.study-guitar.com/blog/minor-key-chord-progressions/
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Natural Minor - triads"
        self.intervals = [2, 1, 2, 2, 1, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["m", "dim", "", "m", "m", "", ""]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thMelodicMinor_4notes(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Melodic Minor - 4 notes"
        self.intervals = [2, 1, 2, 2, 2, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["mM7", "m7", "M7+5", "7", "7", "m7b5", "m7b5"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thMelodicMinor_triads(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Melodic Minor - triads"
        self.intervals = [2, 1, 2, 2, 2, 2]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["m", "m", "aug", "", "", "dim", "dim"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thHarmonicMinor_4notes(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Harmonic Minor - 4 notes"
        self.intervals = [2, 1, 2, 2, 1, 3]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["mM7", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}


class CircleOf5thHarmonicMinor_triads(CircleOf5th):
    """
    https://www.youtube.com/watch?v=44t2KJQUh3Y
    """
    def __init__(self):
        super().__init__()
        self.cof_name = "Harmonic Minor - triads"
        self.intervals = [2, 1, 2, 2, 1, 3]  # https://muted.io/scale-formulas-intervals/
        self.qualities = ["m", "dim", "aug", "m", "", "", "dim"]
        self.cof_scales = self.generate_circle_of_fifths()
        self.cof_tone_compliances[self.cof_name] = {}
