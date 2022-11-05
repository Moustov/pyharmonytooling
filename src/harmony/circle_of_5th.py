from pychord import ChordProgression, Chord

from src.output.console import LOD_TONE, LOD_CHORD, LOD_NOTE, print_detail

chromatic_scale = ["A", "B", "C", "D", "E", "F", "G", "A#", "C#", "D#", "F#", "G#"]
circle_of_fifths_natural_majors = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "Fm", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "Abm", "Bb", "C#", "D#m", "Fdim"],
    "Db": ["Db", "Ebm", "F#m", "G#", "Ab", "Bbm", "C#dim"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
}
circle_of_fifths_church_modes = circle_of_fifths_natural_majors
circle_of_fifths_major_modes = circle_of_fifths_natural_majors
circle_of_fifths_harmonic_minors = {  # todo
    "C": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "G": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "D": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "A": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "E": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "B": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "F#": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "Db": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "Ab": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "Eb": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "Bb": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
    "F": ["Cm", "Dm7b5", "Ebmaj7-#5", "Fm7", "G7", "Abmaj7", "Bdim7"],
}
circle_of_fifths_melodic_minors = {  # todo
    "C": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "G": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "D": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "E": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "A": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "B": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "F#": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "Dd": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "Ab": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "Eb": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "Bb": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
    "F": ["Cm", "Dm7", "Ebmaj7-#5", "F7", "G7", "Abm7b5", "Bm7b5"],
}


def get_compliance_note_presence(tone: [str], cp: ChordProgression) -> float:
    """
    distance with notes
    if the note is present => the chord will fully count
    :param tone:
    :param cp:
    :return:
    """
    return 0.0


def get_compliance_chord_frequency(tone: [str], cp: ChordProgression) -> float:
    """
    distance with tone is based on the amount of chord presence:
    if the chord is present => the chord will count regarding its use in the cp
    :param tone:
    :param cp:
    :return:
    """
    return 0.0

def all_existing_chords() -> [Chord]:
    possible_chords_from_note = []
    for note in chromatic_scale:
        possible_chords_from_note += get_chord_names_possible_qualities(note)
        possible_chords_from_note += get_chord_names_possible_qualities(note+"m")
    print_detail(LOD_TONE, f"Number of existing chords: {len(possible_chords_from_note)}")
    return possible_chords_from_note


def find_substitutes(chord: Chord) -> [Chord]:
    similar_chords = []
    possible_chords = all_existing_chords()
    for pc in possible_chords:
        if pc != chord and pc.components() == chord.components():
            similar_chords.append(pc)
            print_detail(LOD_CHORD, f"{pc} == {chord}")
            print_detail(LOD_NOTE, f"{pc.components()} vs {chord.components()}")
    return similar_chords


def find_similar_chords() -> []:
    similar_chords = []
    possible_chords_from_note = all_existing_chords()
    for chord1 in possible_chords_from_note:
        for chord2 in possible_chords_from_note:
            if chord1 != chord2 and chord1.components() == chord2.components():
                similar_chords.append([chord1, chord2])
                print_detail(LOD_CHORD, f"{chord1} == {chord2}")
                print_detail(LOD_NOTE, f"{chord1.components()} vs {chord2.components()}")
    return similar_chords


def get_compliance_chord_presence(tone: [str], cp: ChordProgression) -> float:
    """
    the distance is binary : if the chord is present => the chord will fully count
    :param tone:
    :param cp:
    :return:
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
        print_detail(LOD_CHORD, f"  Check {chord_tone}")
        tone_compliance[chord_tone] = False
        possible_chord_qualities = get_chord_names_possible_qualities(chord_tone)
        for chord_song in chord_song_list:
            if chord_song in possible_chord_qualities:
                tone_compliance[chord_tone] = True
                compliant_chords.append(chord_song)
                print_detail(LOD_CHORD, f"    {chord_song} found in song")

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


def get_borrowed_chords(tone: [str], song_chord_progression: ChordProgression) -> {}:
    """
    returns borrowed chords the song_chord_progression involves from a given tone
    :param tone: array of chord names
    :param song_chord_progression:
    :return:
    """
    borrowed_chords = {}
    colors = []
    for chord_tone in tone:
        possible_chord_qualities = get_chord_names_possible_qualities(chord_tone)
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


def get_chord_names_possible_qualities(chord: str) -> [str]:
    """
    returns the list of strings with possible qualities a chord may have
    see
        https://www.oolimo.com/guitarchords/find
        https://www.musicnotes.com/now/tips/a-complete-guide-to-chord-symbols-in-music/
    :param chord:
    :return:
    """
    base_chord = Chord(chord)
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
                           "maj7/#5", "maj7/13", "maj7/9/13", "7", "7/b9", "7/9",
                           "7/#9", "7/#11", "7/b5", "7/#5", "7/b13", "7/13",
                           "7/9/13", "7/b9/b13", "7/13/b9", "6", "6/9"
                           ]
    else:
        chord_qualities = ["", "m", "5", "add9", "aug", "dim7",
                           "sus4", "sus2", "7sus4", "7sus4/9", "7sus4/b9", "7sus4/13",
                           "madd9", "m6", "m6/9", "m7", "m7/9", "m7/11",
                           "m7/13", "m7/b13", "m/maj7", "maj7", "maj7/9", "maj7/#11",
                           "maj7/#5", "maj7/13", "maj7/9/13", "7", "7/b9", "7/9",
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
        for cs in chromatic_scale:
            try:
                a = (str(c) + "/" + cs)
                valid_chord = Chord(a)
                enriched_with_quality_with_bass.append(valid_chord)
            except ValueError as err:
                # print("Chord", a, "is invalid", err)
                pass
    # print("All possible chords:", len(enriched_with_quality_with_bass))
    return enriched_with_quality_with_bass


def digest_song(song: str) -> ChordProgression:
    """
    return a ChordProgression object from a song
    todo make sure the captured chords are chords, not words (eg. "am", "a", ...)
    :param song:
    :return:
    """
    cp = None
    possible_chords = []
    lines = song.split("\n")
    for l in lines:
        words = l.split(" ")
        for w in words:
            if w != "":
                try:
                    c = Chord(w)
                    possible_chords.append(w)
                except:
                    pass
    cp = ChordProgression(possible_chords)
    return cp


def generate_circle_of_fifths_natural_majors() -> {}:
    """
    generates the circle_of_fifths_natural_majors
    https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
    :return:
    """
    intervals = ["W", "W", "H", "W", "W", "W"]
    qualities = ["", "m", "m", "", "", "m", "dim"]
    return generate_circle_of_fifths(intervals, qualities)


def generate_circle_of_fifths_harmonic_minors() -> {}:
    """
    generates the circle_of_fifths_natural_majors
    https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
    :return:
    """
    intervals = ["W", "H", "W", "W", "H", "W+H"]
    qualities = ["m", "m7b5", "maj7/#5", "m7", "7", "maj7", "dim7"]
    return generate_circle_of_fifths(intervals, qualities)


def generate_circle_of_fifths_natural_minors() -> {}:
    """
    generates the circle_of_fifths_natural_majors
    https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
    :return:
    """
    intervals = ["W", "H", "W", "W", "H", "W"]
    qualities = ["m", "m7b5", "maj7/#5", "m7", "7", "maj7", "dim7"]
    return generate_circle_of_fifths(intervals, qualities)


def generate_circle_of_fifths_melodic_minors() -> {}:
    """
    generates the circle_of_fifths_natural_majors
    https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
    :return:
    """
    intervals = ["W", "H", "W", "W", "W", "W"]
    qualities = ["m", "m7b5", "maj7/#5", "m7", "7", "maj7", "dim7"]
    return generate_circle_of_fifths(intervals, qualities)


def generate_circle_of_fifths(intervals, qualities, cycle_sequence):
    """
    todo
    generates a circle of fifths from intervals, qualities
    :param intervals:
    :param qualities:
    :param cycle_sequence:
    :return:
    """
    cycle_sequence = ["C", "G", "D", "E", "A", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
    return {}


def guess_tone_from_circle_of_fifths(cp: ChordProgression, cof: {}, cof_name: str) -> []:
    """

    :param outcome_level_of_detail:
    :param cof_name:
    :param cp:
    :param cof:
    :return:
    """
    compliance_level_max = [0, "?"]
    compliances = {}
    for tone in cof:
        print_detail(LOD_TONE, f"Check tone {str(tone)} in {cof_name}")
        compliance_level = get_compliance_chord_presence(cof[tone], cp)
        print_detail(LOD_TONE, f"{tone}, {compliance_level * 100}%")
        compliances[tone] = compliance_level
        if compliance_level > compliance_level_max[0]:
            compliance_level_max = [compliance_level, tone]
    return compliance_level_max


def guess_tone_and_mode(cp: ChordProgression) -> []:
    guess = guess_tone_from_circle_of_fifths(cp, circle_of_fifths_natural_majors, "Natural Major")
    return guess
