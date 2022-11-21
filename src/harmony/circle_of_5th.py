from pychord import ChordProgression, Chord

from src.displays.console import _HarmonyLogger
from src.harmony.cof_chord import CofChord
from src.harmony.note import Note


class CircleOf5th:
    cof_name = "circle name"
    intervals = []
    qualities = []
    cof_scales = None
    cycle_sequence = ["C", "G", "D", "E", "A", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]

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

    @staticmethod
    def guess_tone_and_mode_from_cadence(cadence: str):
        """
        return the most compatible circle of 5th with the cadence
        :param cadence: eg. "ii7-V7-Imaj7" would return a CircleOf5thNaturalMajor()
        :return:
        """
        return CircleOf5thNaturalMajor()

    def get_compliance_chord_presence(self, tone: [str], cp: ChordProgression) -> float:
        """
        the distance is binary : if the chord is present => the chord will fully count
        :param tone:
        :param cp:
        :return: 0.0 --> 1.0 (100% compliant)
        """
        # init - synthesis of used chords in cp for quicker analysis
        tone_compliance = {}
        compliant_chords = []
        chord_song_list = []
        for chord_song in cp:
            if chord_song not in chord_song_list:
                chord_song_list.append(chord_song)

        # check each chord in the tone and see if colored versions of the chord is used in chord_song_list
        for chord_tone in tone:
            _HarmonyLogger.print_detail(_HarmonyLogger.LOD_CHORD, f"  Check {chord_tone}")
            tone_compliance[chord_tone] = False
            possible_chord_qualities = CofChord.get_chord_names_possible_qualities(chord_tone)
            for chord_song in chord_song_list:
                if chord_song in possible_chord_qualities:
                    # todo handle tempered equivalence with Note.__eq__()
                    tone_compliance[chord_tone] = True
                    compliant_chords.append(chord_song)
                    _HarmonyLogger.print_detail(_HarmonyLogger.LOD_CHORD, f"    {chord_song} found in song")

        # set compliance level
        compliance_level = 0
        borrowed_chords_qty = 0
        if len(compliant_chords) > 0:
            for chord_song in chord_song_list:
                if chord_song in compliant_chords:
                    compliance_level += 1
                else:
                    borrowed_chords_qty += 1

        if compliance_level == 0 or len(compliant_chords) == 0:
            return 0.0
        elif len(chord_song_list) > len(tone_compliance) and compliance_level == len(tone_compliance):
            return 1.0
        elif len(chord_song_list) <= len(tone_compliance) and borrowed_chords_qty == 0:
            return 1.0
        else:
            return compliance_level / len(tone_compliance)

    def get_borrowed_chords(self, tone: [str], song_chord_progression: ChordProgression) -> {}:
        """
        returns borrowed chords the song_chord_progression involves from a given tone
        :param tone: array of chord names
        :param song_chord_progression:
        :return:
        """
        borrowed_chords = {}
        colors = []
        for chord_tone in tone:
            possible_chord_qualities = CofChord.get_chord_names_possible_qualities(chord_tone)
            for chord_tone_color in possible_chord_qualities:
                colors.append(chord_tone_color)

        for chord_song in song_chord_progression:
            found = False
            for chord_tone_color in colors:
                if chord_tone_color.components() == chord_song.components():
                    found = True
            if not found:
                for chord_tone in tone:
                    c = Chord(chord_tone)
                    if c.components() != chord_song.components():
                        borrowed_chords[str(chord_song)] = True
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
                        c = Chord(w)
                        possible_chords.append(w)
                    except:
                        pass
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

    def guess_tone_from_circle_of_fifths(self, cp: ChordProgression) -> []:
        """

        :param cp:
        :return: [probability, note, circle name, scale]
        """
        compliance_level_max = [0, "?", "?", []]
        compliances = {}
        compliance_level = 0
        for tone in self.cof_scales:
            _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"Check tone {str(tone)} in {self.cof_name}")
            compliance_level = self.get_compliance_chord_presence(self.cof_scales[tone], cp)
            _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"{tone}, {compliance_level * 100}%")
            compliances[tone] = compliance_level
            if compliance_level > compliance_level_max[0]:
                compliance_level_max = [compliance_level, tone, self.cof_name, self.get_scale(tone)]
        return compliance_level_max

    def guess_tone_and_mode(self, cp: ChordProgression) -> []:
        """
        return the most probable tone of a ChordProgression across possible circle of 5th
        :param cp:
        :return: [probability, note, circle name, scale]
        """
        best_tone = [0, "-", "?", []]
        cof_nat_maj = CircleOf5thNaturalMajor()
        guess = cof_nat_maj.guess_tone_from_circle_of_fifths(cp)
        if guess[0] > best_tone[0]:
            best_tone = guess
        cof_mel_minor = CircleOf5thMelodicMinor()
        guess = cof_mel_minor.guess_tone_from_circle_of_fifths(cp)
        if guess[0] > best_tone[0]:
            best_tone = guess
        cof_nat_min = CircleOf5thNaturalMinor()
        guess = cof_nat_min.guess_tone_from_circle_of_fifths(cp)
        if guess[0] > best_tone[0]:
            best_tone = guess
        cof_harm_minor = CircleOf5thHarmonicMinor()
        guess = cof_harm_minor.guess_tone_from_circle_of_fifths(cp)
        if guess[0] > best_tone[0]:
            best_tone = guess
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


class CircleOf5thNaturalMajor(CircleOf5th):
    cof_name = "Natural Major"
    intervals = [2, 2, 1, 2, 2, 2]
    qualities = ["", "m", "m", "", "", "m", "dim"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()


class CircleOf5thNaturalMinor(CircleOf5th):
    cof_name = "Natural Minor"
    intervals = [2, 1, 2, 2, 1, 2]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()


class CircleOf5thMelodicMinor(CircleOf5th):
    cof_name = "Melodic Minor"
    intervals = [2, 1, 2, 2, 2, 2]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()


class CircleOf5thHarmonicMinor(CircleOf5th):
    cof_name = "Harmonic Minor"
    intervals = [2, 1, 2, 2, 1, 3]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()
