from array import array

from pychord import Chord

from src.displays.console import _HarmonyLogger
from src.harmony.note import Note


class CofChord(Chord):
    def __init__(self, chord_name: str):
        super().__init__(chord_name)

    @staticmethod
    def is_same_chord_from_components(a, b):
        """
        returns True if all components are the same
        :param a:
        :param b:
        :return:
        """
        if not isinstance(a, Chord) or not isinstance(b, Chord):
            raise TypeError(f"Cannot compare non CofChord objects")
        c1 = sorted(a.components())
        c2 = sorted(b.components())
        if len(c1) != len (c2):
            return False
        return CofChord.is_chord_included_from_components(a, b)

    @staticmethod
    def is_chord_included_from_components(a, b):
        """
        return True is the components from a are included in b
        :param a:
        :param b:
        :return:
        """
        if not isinstance(a, Chord) or not isinstance(b, Chord):
            raise TypeError(f"Cannot compare non CofChord objects")
        c1 = sorted(a.components())
        return CofChord.are_components_included_in_chord(c1, b)

    @staticmethod
    def are_components_included_in_chord(components: [Note], chord):
        """
        return True is the components from a are included in b
        :param chord: a Chord()
        :param components:
        :return:
        """
        if not isinstance(chord, Chord):
            raise TypeError(f"Cannot compare non CofChord objects")
        c2 = sorted(chord.components())
        for e1 in components:
            found = False
            for e2 in c2:
                if e1 == Note(e2):
                    found = True
                    break
            if not found:
                return False
        return True

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
                               "M7", "M7/9", "M7/#11",
                               "M7+5", "M7/13", "M7/9/13", "7", "7/b9", "7/9",
                               "7/#9", "7/#11", "7/b5", "7/#5", "7/b13", "7/13",
                               "7/9/13", "7/b9/b13", "7/13/b9", "6", "6/9"
                               ]
        else:
            chord_qualities = ["", "m", "5", "add9", "aug", "dim7",
                               "sus4", "sus2", "7sus4", "7sus4/9", "7sus4/b9", "7sus4/13",
                               "madd9", "m6", "m6/9", "m7", "m7/9", "m7/11",
                               "m7/13", "m7/b13", "M7", "M7/9", "M7/#11",
                               "M7+5", "M7/13", "M7/9/13", "7", "7/b9", "7/9",
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
            for cs in Note.CHROMATIC_SCALE_SHARP_BASED:
                if cs != base_chord.root:
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
            if CofChord.is_same_chord_from_components(chord, pc):
                similar_chords.append(pc)
                _HarmonyLogger.print_detail(_HarmonyLogger.LOD_CHORD, f"{pc} == {chord}")
                _HarmonyLogger.print_detail(_HarmonyLogger.LOD_NOTE, f"{pc.components()} vs {chord.components()}")
        return similar_chords

    @staticmethod
    def all_existing_chords_from_note(note: Note) -> [Chord]:
        """
        return the list of all possible chords
        :return:
        """
        possible_chords_from_note = []
        possible_chords_from_note += CofChord.get_chord_names_possible_qualities(str(note))
        possible_chords_from_note += CofChord.get_chord_names_possible_qualities(str(note) + "m")
        _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE,
                                    f"Number of existing chords: {len(possible_chords_from_note)}")
        return possible_chords_from_note

    @staticmethod
    def all_existing_chords() -> [Chord]:
        """
        return the list of all possible chords
        the list includes sharp/flat equivalents
        todo : provide a cache for this
        :return:
        """
        possible_chords = []
        for note in Note.CHROMATIC_SCALE_SHARP_BASED:
            for eqv_note in Note.equivalents(note):
                possible_chords += CofChord.get_chord_names_possible_qualities(eqv_note)
                possible_chords += CofChord.get_chord_names_possible_qualities(eqv_note + "m")
        _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"Number of existing chords: {len(possible_chords)}")
        res = []
        checked_chords = []
        for c in possible_chords:
            if str(c) not in checked_chords:
                res.append(c)
                checked_chords.append(str(c))
        return res

    @staticmethod
    def find_similar_chords() -> []:
        """
        find similar chords among all possible chords
        WARNING a lot of combinations are generated
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

    @staticmethod
    def guess_chord_name(chord_notes: [Note], is_strictly_compliant: bool = True, simplest_chord_only: bool = True) -> [Chord]:
        """
        todo return <Chord("C")> from [<Note("C">), <Note("G">), <Note("E">)]
        :param simplest_chord_only: "simple" means shortest chord name (with no bass if possible)
        :param is_strictly_compliant: try not to
        :param chord_notes:
        :return:
        """
        compatible_chords = []
        possible_chords = CofChord.all_existing_chords()
        for c in possible_chords:
            if CofChord.are_components_included_in_chord(chord_notes, c):
                if is_strictly_compliant and len(chord_notes) == len(c.components()):
                    compatible_chords.append(c)
                elif not is_strictly_compliant:
                    compatible_chords.append(c)
        if simplest_chord_only and len(chord_notes) == 1:
            return [Chord(str(chord_notes[0]))]
        elif simplest_chord_only:
            # loooong dummy name to ensure finding the shortest chord name
            simplest_chord_name = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            simplest_chord = None
            for c in compatible_chords:
                if len(str(c)) < len(str(simplest_chord_name)):
                    simplest_chord_name = c
                    simplest_chord = c
            compatible_chords = [simplest_chord]
        return compatible_chords
