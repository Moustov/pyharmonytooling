from pychord import Chord

from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.harmony.note import Note


class CofChord(Chord):
    possible_chords = []

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
    def is_chord_included_from_components(a: Chord, b: Chord):
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
    def are_components_included_in_chord(expected_notes: [Note], chord: Chord):
        """
        return True is the components from a are included in b
        :param chord: a Chord()
        :param expected_notes:
        :return:
        """
        if not isinstance(chord, Chord):
            raise TypeError(f"Cannot compare non CofChord objects")
        proposed_chord_components = chord.components()
        for exp_note in expected_notes:
            found = False
            for proposed_note in proposed_chord_components:
                if exp_note == Note(proposed_note):
                    found = True
                    break
            if not found:
                return False
        return True

    @staticmethod
    def get_chord_names_possible_qualities(chord: str) -> [Chord]:
        """
        returns the list of Chord with possible qualities a chord may have

        NOTE: let's try to extract possible qualities from
                https://github.com/yuma-m/pychord/blob/main/pychord/constants/qualities.py
                or QualityManager (https://github.com/yuma-m/pychord/blob/main/pychord/quality.py)
                considering minor qualities from the presence of "3" in the chord notes
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
        :return:
        """
        if CofChord.possible_chords:
            return CofChord.possible_chords

        for note in Note.CHROMATIC_SCALE_SHARP_BASED:
            # let's handle notes like Ab/G#
            for eqv_note in Note.equivalents(note):
                CofChord.possible_chords += CofChord.get_chord_names_possible_qualities(eqv_note)
                CofChord.possible_chords += CofChord.get_chord_names_possible_qualities(eqv_note + "m")
        _HarmonyLogger.print_detail(_HarmonyLogger.LOD_TONE, f"Number of existing chords: {len(CofChord.possible_chords)}")
        res = []
        checked_chords = []
        for c in CofChord.possible_chords:
            if str(c) not in checked_chords:
                res.append(c)
                checked_chords.append(str(c))
        CofChord.possible_chords = res
        return res

    @staticmethod
    def find_similar_chords() -> []:
        """
        find similar chords among all possible chords
        **WARNING** a lot of combinations are generated
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
        return <Chord("C")> from [<Note("C">), <Note("G">), <Note("E">)]

        * NOTE: the chord name is influenced with the bass
        * **WARNING** : simplest_chord_only => is_strictly_compliant
        * todo BUG: simplest_chord_only does not seem to work properly:

                notes = [Note("B"), Note("E"), Note("D"), Note("A")]
                res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=False)
                print(res)
                --> []
            while
                notes = [Note("B"), Note("E"), Note("D"), Note("A")]
                res = CofChord.guess_chord_name(notes, is_strictly_compliant=True, simplest_chord_only=True)
                print(res)
                --> [<Chord: E7sus4>]

        * NOTE: could be optimized from https://github.com/yuma-m/pychord/blob/59e3bf52d39c3355c6b5709f6adf6d44b7eaec6a/pychord/analyzer.py#L8
            However, this method does not fully work properly : https://github.com/yuma-m/pychord/issues/73
        :param simplest_chord_only: "simple" means shortest chord name (with no bass if possible)
        :param is_strictly_compliant:   True: finds only chords with the same notes
                                        False: chords that includes required notes
        :param chord_notes:
        :return:
        """
        exaecos = []  # chords with same best complexity
        compatible_chords = []
        possible_chords = CofChord.all_existing_chords()
        for c in possible_chords:
            if CofChord.are_components_included_in_chord(chord_notes, c):
                if is_strictly_compliant:
                    if len(chord_notes) == len(c.components()):
                        compatible_chords.append(c)
                else:
                    compatible_chords.append(c)
        if simplest_chord_only and len(chord_notes) == 1:
            return [Chord(str(chord_notes[0]))]
        elif simplest_chord_only:
            res = []
            # loooong dummy name to ensure finding the shortest chord name
            simplest_chord_name = "A#7sus4/13/C#"   # the longest known/valid chord name (see PyChord)
            simplest_chord = None
            for c in compatible_chords:
                diff = CofChord.compare_simplicity(c, simplest_chord_name)
                if diff == -1:
                    simplest_chord_name = str(c)
                    simplest_chord = c
                    exaecos = [c]
                elif diff == 0:
                    exaecos.append(c)
        return exaecos

    @staticmethod
    def compare_simplicity(chord: Chord, simplest_chord_name: str) -> int:
        """
        return True if chord (name) is simpler than the provided simplest_chord_name
        todo : add other criteria that would provide simpler chords such as CoF compliance or b/# to improve readability
        Note: CoF compliance could be handled at Song level
        Note: on a guitar, the less fingers, the better
        Note: on a guitar, the closest, the better
        :param simplest_chord_name: criterion #1 because it improves readability
        :param chord:
        :return: -1 : chord is simpler / 0: same / 1 simplest_chord_name is simpler
        """
        if len(chord.components()) < len(Chord(simplest_chord_name).components()):
            # the less note, the less strings, the simplier
            return -1
        if len(str(chord)) < len(simplest_chord_name):
            # the shorter the name, the more readable, the simplier
            return -1
        elif len(str(chord)) == len(simplest_chord_name) and (len(chord.components()) == len(simplest_chord_name)):
            # same name length + same amount of notes
            return 0
        elif len(str(chord)) > len(simplest_chord_name):
            # the longer the name, the more complex
            return 1
        return 0

    @staticmethod
    def is_chord_in_array(chord: Chord, array: [Chord]) -> bool:
        """
        True if the chord can be found in the array
        :param chord:
        :param array:
        :return:
        """
        found = False
        for c in array:
            if str(chord) == str(c):
                found = True
                break
        return found

    @staticmethod
    def same_array_of_chords(chords_1: [Chord], chords_2: [Chord]):
        """
        True if the 2 arrays of chords contains the same Chords
        :param chords_2:
        :return:
        """
        expectation_met = True
        for r in chords_1:
            c_found = False
            for e in chords_2:
                if str(r) == str(e):
                    c_found = True
                    break
            if not c_found:
                return False
            expectation_met = expectation_met and c_found
        return expectation_met

    @staticmethod
    def are_chord_equals(chord1: Chord, chord2:Chord) -> bool:
        if not chord1 or not chord2:
            return False
        c1 = sorted(chord1.components())
        cmp1 = CofChord.are_components_included_in_chord(c1, chord2)
        c2 = sorted(chord1.components())
        cmp2 = CofChord.are_components_included_in_chord(c2, chord1)
        return cmp1 and cmp2