from pychord import ChordProgression, Chord

from src.output.console import LOD_TONE, LOD_CHORD, LOD_NOTE, print_detail, HarmonyLogger


class CircleOf5th:
    chromatic_scale = ["A", "B", "C", "D", "E", "F", "G", "A#", "C#", "D#", "F#", "G#"]
    cof_name = "circle name"
    intervals = []
    qualities = []
    cof_scales = None
    cycle_sequence = ["C", "G", "D", "E", "A", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
    # circle_of_fifths_natural_majors = {
    #     "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    #     "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    #     "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    #     "A": ["A", "Bm", "C#m", "D", "E", "Fm", "G#dim"],
    #     "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    #     "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    #     "F#": ["F#", "G#m", "Abm", "Bb", "C#", "D#m", "Fdim"],
    #     "Db": ["Db", "Ebm", "F#m", "G#", "Ab", "Bbm", "C#dim"],
    #     "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
    #     "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
    #     "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
    #     "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
    # }
    # circle_of_fifths_church_modes = circle_of_fifths_natural_majors
    # circle_of_fifths_major_modes = circle_of_fifths_natural_majors
    # circle_of_fifths_harmonic_minors = {  # todo
    #     "C": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "G": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "D": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "A": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "E": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "B": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "F#": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "Db": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "Ab": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "Eb": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "Bb": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    #     "F": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    # }
    # circle_of_fifths_melodic_minors = {  # todo
    #     "C": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "G": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "D": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "E": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "A": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "B": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "F#": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "Dd": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "Ab": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "Eb": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "Bb": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    #     "F": ["Cm", "Dm7", "EbM7#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    # }

    def get_compliance_note_presence(self, tone: [str], cp: ChordProgression) -> float:
        """
        todo
        distance with notes
        if the note is present => the chord will fully count
        :param tone:
        :param cp:
        :return:
        """
        return 0.0

    def get_compliance_chord_frequency(self, tone: [str], cp: ChordProgression) -> float:
        """
        todo
        distance with tone is based on the amount of chord presence:
        if the chord is present => the chord will count regarding its use in the cp
        :param tone:
        :param cp:
        :return:
        """
        return 0.0

    def all_existing_chords(self) -> [Chord]:
        """
        return the list of all possible chords
        :return:
        """
        possible_chords_from_note = []
        for note in self.chromatic_scale:
            possible_chords_from_note += self.get_chord_names_possible_qualities(note)
            possible_chords_from_note += self.get_chord_names_possible_qualities(note + "m")
        HarmonyLogger.print_detail(HarmonyLogger.LOD_TONE, f"Number of existing chords: {len(possible_chords_from_note)}")
        return possible_chords_from_note

    def find_substitutes(self, chord: Chord) -> [Chord]:
        """
        return the list of equivalent chords from a chord
        :param chord:
        :return:
        """
        similar_chords = []
        possible_chords = self.all_existing_chords()
        for pc in possible_chords:
            if pc != chord and pc.components() == chord.components():
                similar_chords.append(pc)
                HarmonyLogger.print_detail(HarmonyLogger.LOD_CHORD, f"{pc} == {chord}")
                HarmonyLogger.print_detail(HarmonyLogger.LOD_NOTE, f"{pc.components()} vs {chord.components()}")
        return similar_chords

    def find_similar_chords(self) -> []:
        """
        find similar chords among all possible chords
        :return:
        """
        similar_chords = []
        possible_chords_from_note = self.all_existing_chords()
        for chord1 in possible_chords_from_note:
            for chord2 in possible_chords_from_note:
                if chord1 != chord2 and chord1.components() == chord2.components():
                    similar_chords.append([chord1, chord2])
                    HarmonyLogger.print_detail(HarmonyLogger.LOD_CHORD, f"{chord1} == {chord2}")
                    HarmonyLogger.print_detail(HarmonyLogger.LOD_NOTE, f"{chord1.components()} vs {chord2.components()}")
        return similar_chords

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
            HarmonyLogger.print_detail(HarmonyLogger.LOD_CHORD, f"  Check {chord_tone}")
            tone_compliance[chord_tone] = False
            possible_chord_qualities = self.get_chord_names_possible_qualities(chord_tone)
            for chord_song in chord_song_list:
                if chord_song in possible_chord_qualities:
                    tone_compliance[chord_tone] = True
                    compliant_chords.append(chord_song)
                    HarmonyLogger.print_detail(HarmonyLogger.LOD_CHORD, f"    {chord_song} found in song")

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
            possible_chord_qualities = self.get_chord_names_possible_qualities(chord_tone)
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

    def get_chord_names_possible_qualities(self, chord: str) -> [Chord]:
        """
        returns the list of Chord with possible qualities a chord may have
        see
            https://www.oolimo.com/guitarchords/find
            https://www.musicnotes.com/now/tips/a-complete-guide-to-chord-symbols-in-music/
        :param chord:
        :return:
        """
        try:
            base_chord = Chord(chord)
        except:
            pass
        chord_qualities = []
        if base_chord.quality.quality == "m":
            chord_qualities = ["m", "5", "add9", "aug", "dim7",
                               "sus4", "sus2", "7sus4", "7sus4/9", "7sus4/b9", "7sus4/13",
                               "madd9", "m6", "m6/9", "m7", "m7/9", "m7/11",
                               "m7/13", "m7/b13", "m/maj7",
                               "m7b5",
                               "m7/11/b5", "dim/b13"
                               ]
        elif base_chord.quality.quality == "dim":
            chord_qualities = ["dim", "dim7", "dim/b13"]
        elif base_chord.quality.quality == "":
            chord_qualities = ["", "5", "add9", "aug",
                               "sus4", "sus2", "7sus4", "7sus4/9", "7sus4/b9", "7sus4/13",
                               "maj7", "maj7/9", "maj7/#11",
                               "M7+5", "maj7/13", "maj7/9/13", "7", "7/b9", "7/9",
                               "7/#9", "7/#11", "7/b5", "7/#5", "7/b13", "7/13",
                               "7/9/13", "7/b9/b13", "7/13/b9", "6", "6/9"
                               ]
        else:
            chord_qualities = ["", "m", "5", "add9", "aug", "dim7",
                               "sus4", "sus2", "7sus4", "7sus4/9", "7sus4/b9", "7sus4/13",
                               "madd9", "m6", "m6/9", "m7", "m7/9", "m7/11",
                               "m7/13", "m7/b13", "m/maj7", "maj7", "maj7/9", "maj7/#11",
                               "M7+5", "maj7/13", "maj7/9/13", "7", "7/b9", "7/9",
                               "7/#9", "7/#11", "7/b5", "7/#5", "7/b13", "7/13",
                               "7/9/13", "7/b9/b13", "7/13/b9", "6", "6/9", "m7b5",
                               "m7/11/b5", "dim7/b13"
                               ]
        enriched_with_quality = []
        for c in chord_qualities:
            try:
                valid_chord = Chord(base_chord.root + c)
                enriched_with_quality.append(valid_chord)
            except ValueError as err:
                # print("Chord", chord+c, "is invalid", err)
                pass
        enriched_with_quality_with_bass = enriched_with_quality.copy()
        for c in enriched_with_quality:
            for cs in self.chromatic_scale:
                try:
                    a = (str(c) + "/" + cs)
                    valid_chord = Chord(a)
                    enriched_with_quality_with_bass.append(valid_chord)
                except ValueError as err:
                    # print("Chord", a, "is invalid", err)
                    pass
        # print("All possible chords:", len(enriched_with_quality_with_bass))
        return enriched_with_quality_with_bass

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

    def generate_circle_of_fifths_natural_majors(self) -> {}:
        """
        generates the circle_of_fifths_natural_majors
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        intervals = [2, 2, 1, 2, 2, 2]
        qualities = ["", "m", "m", "", "", "m", "dim"]
        return self.generate_circle_of_fifths(intervals, qualities)

    def generate_circle_of_fifths_harmonic_minors(self) -> {}:
        """
        generates the circle_of_fifths_natural_majors
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        intervals = [2, 1, 2, 2, 1, 3]
        qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]
        return self.generate_circle_of_fifths(intervals, qualities)

    def generate_circle_of_fifths_natural_minors(self) -> {}:
        """
        generates the circle_of_fifths_natural_majors
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        intervals = [2, 1, 2, 2, 1, 2]
        qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]
        return self.generate_circle_of_fifths(intervals, qualities)

    def generate_circle_of_fifths(self, intervals, qualities) -> dict:
        """
        generates a circle of fifths from intervals, qualities
        :param intervals:
        :param qualities:
        :param cycle_sequence:
        :return:
        """
        intervals.append(0)
        res = {}
        for seq in self.cycle_sequence:
            res[seq] = []
            current_note = seq
            for interval, quality in zip(intervals, qualities):
                res[seq].append(f"{current_note}{quality}")
                current_note = self.get_next_note(current_note, interval)
        return res

    def guess_tone_from_circle_of_fifths(self, cp: ChordProgression) -> []:
        """

        :param cp:
        :return: [probability, note, circle name, scale]
        """
        compliance_level_max = [0, "?", "?",[]]
        compliances = {}
        compliance_level = 0
        for tone in self.cof_scales:
            HarmonyLogger.print_detail(HarmonyLogger.LOD_TONE, f"Check tone {str(tone)} in {self.cof_name}")
            compliance_level = self.get_compliance_chord_presence(self.cof_scales[tone], cp)
            HarmonyLogger.print_detail(HarmonyLogger.LOD_TONE, f"{tone}, {compliance_level * 100}%")
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

    def generate_circle_of_fifths(self) -> {}:
        """
        generates the circle_of_fifths_natural_majors
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        return super().generate_circle_of_fifths(self.intervals, self.qualities)


class CircleOf5thNaturalMinor(CircleOf5th):
    cof_name = "Natural Minor"
    intervals = [2, 1, 2, 2, 1, 2]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()

    def generate_circle_of_fifths(self) -> {}:
        """
        generates the circle_of_fifths_natural_minors
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        return super().generate_circle_of_fifths(self.intervals, self.qualities)


class CircleOf5thMelodicMinor(CircleOf5th):
    cof_name = "Melodic Minor"
    intervals = [2, 1, 2, 2, 2, 2]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()

    def generate_circle_of_fifths(self) -> {}:
        """
        generates the circle_of_fifths_melodic minor
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        return super().generate_circle_of_fifths(self.intervals, self.qualities)


class CircleOf5thHarmonicMinor(CircleOf5th):
    cof_name = "Harmonic Minor"
    intervals = [2, 1, 2, 2, 1, 3]
    qualities = ["m", "m7b5", "M7+5", "m7", "7", "maj7", "dim7"]

    def __init__(self):
        self.cof_scales = self.generate_circle_of_fifths()

    def generate_circle_of_fifths(self) -> {}:
        """
        generates the circle_of_fifths_melodic minor
        https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
        :return:
        """
        return super().generate_circle_of_fifths(self.intervals, self.qualities)

