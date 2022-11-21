from pychord import Chord

from src.displays.console import _HarmonyLogger
from src.harmony.note import Note


class CofChord(Chord):
    def __init__(self, chord_name: str):
        super().Chord(chord_name)

    @staticmethod
    def get_chord_names_possible_qualities(chord: str) -> [Chord]:
        """
        returns the list of Chord with possible qualities a chord may have
        see
            https://www.oolimo.com/guitarchords/find
            https://www.musicnotes.com/now/tips/a-complete-guide-to-chord-symbols-in-music/
        :param chord:
        :return:
        """
        base_chord = None
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
            for cs in Note.CHROMATIC_SCALE:
                try:
                    a = (str(c) + "/" + cs)
                    valid_chord = Chord(a)
                    enriched_with_quality_with_bass.append(valid_chord)
                except ValueError as err:
                    # print("Chord", a, "is invalid", err)
                    pass
        # print("All possible chords:", len(enriched_with_quality_with_bass))
        return enriched_with_quality_with_bass

    @staticmethod
    def find_substitutes(chord: Chord) -> [Chord]:
        """
        return the list of equivalent chords from a chord
        :param chord:
        :return:
        """
        similar_chords = []
        possible_chords = CofChord.all_existing_chords()
        for pc in possible_chords:
            if pc != chord and pc.components() == chord.components():
                similar_chords.append(pc)
                _HarmonyLogger.print_detail(_HarmonyLogger.LOD_CHORD, f"{pc} == {chord}")
                _HarmonyLogger.print_detail(_HarmonyLogger.LOD_NOTE, f"{pc.components()} vs {chord.components()}")
        return similar_chords

    @staticmethod
    def all_existing_chords() -> [Chord]:
        """
        return the list of all possible chords
        :return:
        """
        possible_chords_from_note = []
        for note in Note.CHROMATIC_SCALE:
            possible_chords_from_note += CofChord.get_chord_names_possible_qualities(note)
            possible_chords_from_note += CofChord.get_chord_names_possible_qualities(note + "m")
        _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE,
                                   f"Number of existing chords: {len(possible_chords_from_note)}")
        return possible_chords_from_note

    @staticmethod
    def find_similar_chords() -> []:
        """
        find similar chords among all possible chords
        /! a lot of combinations are generated
        :return:
        """
        similar_chords = []
        possible_chords_from_note = CofChord.all_existing_chords()
        for chord1 in possible_chords_from_note:
            for chord2 in possible_chords_from_note:
                if chord1 != chord2 and chord1.components() == chord2.components():
                    similar_chords.append([chord1, chord2])
                    _HarmonyLogger.print_detail(_HarmonyLogger.LOD_CHORD, f"{chord1} == {chord2}")
                    _HarmonyLogger.print_detail(_HarmonyLogger.LOD_NOTE,
                                               f"{chord1.components()} vs {chord2.components()}")
        return similar_chords
