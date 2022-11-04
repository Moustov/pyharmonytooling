from pychord import ChordProgression, Chord


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


def get_compliance_chord_presence(tone: [str], cp: ChordProgression) -> float:
    """
    the distance is binary : if the chord is present => the chord will fully count
    :param tone:
    :param cp:
    :return:
    """
    compliance = {}
    chord_song_list = []
    for chord_song in cp:
        if chord_song not in chord_song_list:
            chord_song_list.append(chord_song)

    for chord_tone in tone:
        for chord_song in cp:
            possible_chord_qualities = get_chord_possible_qualities(chord_tone)
            for chord_color in possible_chord_qualities:
                if chord_color.components() == chord_song.components():
                    compliance[chord_tone] = True
    compliance_level = 0
    for chord_tone in tone:
        if chord_tone in compliance.keys() and compliance[chord_tone]:
            compliance_level += 1
    return compliance_level / len(chord_song_list)


def get_borrowed_chords(tone: [str], song_chord_progression: ChordProgression) -> {}:
    borrowed_chords = {}
    colors = []
    for chord_tone in tone:
        possible_chord_qualities = get_chord_possible_qualities(chord_tone)
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
    see https://www.oolimo.com/guitarchords/find
    :param chord:
    :return:
    """
    c = Chord(chord)
    enriched_with_quality = [(chord + "")]
    if c.quality.quality == "m":
        enriched_with_quality += [
            (chord + "add9"), (chord + "6"), (chord + "6/9"), (chord + "7"), (chord + "9"),
            # (chord + "7/b13"),
        ]
    elif c.quality.quality != "dim":
        enriched_with_quality += [
            (chord + "sus"), (chord + "sus2"), (chord + "7sus4"),
            (chord + "7sus4/9"),
            #   (chord + "7sus4/b9"),
            (chord + "7sus4/13"),
            (chord + "add9"), (chord + "6"), (chord + "6/9"), (chord + "7"), (chord + "9"),
            (chord + "11"), (chord + "13"),
            # (chord + "7/b13"),
            (chord + "maj7"), (chord + "maj9"),
            #   (chord + "maj7/#11"),
            # (chord + "maj7/#5")
        ]
    enriched_with_quality_with_bass = enriched_with_quality.copy()
    chromatic_scale = ["A", "B", "C", "D", "E", "F", "G", "A#", "C#", "D#", "F#", "G#"]
    for c in enriched_with_quality:
        # print(c)
        try:
            ceq = Chord(c)
            for cs in chromatic_scale:
                if str(ceq.chord) != cs and ceq.on == "":
                    # print(str(c.chord) + "/" + cs)
                    try:
                        a = (str(c) + "/" + cs)
                        enriched_with_quality_with_bass.append(a)
                    except Exception as err:
                        print(err, c, cs)
                else:
                    pass    # todo: remove this part - just for break point matters
        except Exception as err:
            print(err)
    return enriched_with_quality_with_bass



def get_chord_possible_qualities(chord: str) -> [str]:
    """
    see https://www.oolimo.com/guitarchords/find
    :param chord:
    :return:
    """
    res = []
    possible_chords = get_chord_names_possible_qualities(chord)
    for c in possible_chords:
        try:
            res.append(Chord(c))
        except Exception as err:
            print(c, "cannot be turned into a Chord", err)
    return res


def digest_song(song: str) -> ChordProgression:
    cp = None
    possible_chords = []
    lines = song.split("\n")
    for l in lines:
        words = l.split(" ")
        for w in words:
            if w != "":
                # print(f"'{w}'")
                try:
                    c = Chord(w)
                    possible_chords.append(w)
                except:
                    pass
    cp = ChordProgression(possible_chords)

    # for c in cp.chords:
    #     print(c.components())

    # c = Chord("Fdim")
    # print("----", c.components())
    return cp


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


def guess_tone_from_circle_of_fifths(cp: ChordProgression, cof: {}) -> []:
    """

    :param cp:
    :param cof:
    :return:
    """
    compliance_level_max = [0, "?"]
    compliances = {}
    for tone in cof:
        compliance_level = get_compliance_chord_presence(cof[tone], cp)
        print(tone, "(major)", compliance_level * 100, "%")
        compliances[tone] = compliance_level
        if compliance_level > compliance_level_max[0]:
            compliance_level_max = [compliance_level, tone]
        borrowed_chords = get_borrowed_chords(tone, cp)
        print("   Borrowed chords:", borrowed_chords.keys())
    return compliance_level_max


def guess_tone_and_mode(cp: ChordProgression) -> []:
    guess = guess_tone_from_circle_of_fifths(cp, circle_of_fifths_natural_majors)
    return guess
