from pychord import Chord

from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.degree import Degree
from pyharmonytools.harmony.note import Note


class Song:
    def __init__(self):
        self.remarquable_cadences = {}
        self.artist = ""
        self.song_title = ""
        self.cof = CircleOf5th()
        self.lyrics = []
        self.line_of_chords = []
        self.chords_sequence = []
        self.degrees = []

    def __str__(self):
        """
        returns a string synthesis of a song
        :return:
        """
        res = f"Title: {self.song_title}\n"
        res += f"Artist: {self.artist}\n"
        return res

    def get_recognized_chords(self) -> [Chord]:
        """
        return a list of valid Chords
        :return:
        """
        res = []
        for cs in self.chords_sequence:
            if type(cs) is Chord:
                res.append(f" {cs} ")
        return res

    def get_tone_and_mode(self) -> dict:
        """
        return the max tone compliance from this song
        see:
        * https://stackoverflow.com/questions/45399081/determine-the-key-of-a-song-by-its-chords
        :return: {"compliance_rate": 0, "tone": "?", "cof_name": "?", "scale": [], "harmonic suite": []}
        """
        song = " ".join(self.get_recognized_chords())
        cp = self.cof.digest_song(song)
        compliance_level_max = self.cof.digest_possible_tones_and_modes(cp)
        return compliance_level_max

    def get_borrowed_chords(self) -> [str]:
        """
        returns the list of borrowed chords from the max tone compliance perspecive
        :return:
        """
        chords_string = " ".join(self.get_recognized_chords())
        cp = self.cof.digest_song(chords_string)
        suspected_key = {}
        if len(self.cof.cof_tone_compliances.keys()) <= 1:
            suspected_key = self.cof.digest_possible_tones_and_modes(cp)
        else:
            suspected_key = self.get_most_compliant_tone_and_mode()
        borrowed_chords = self.cof.get_borrowed_chords(cp, suspected_key["cof_name"], suspected_key["tone"])
        return borrowed_chords

    def digest(self, content: str):
        """
        subclasses must implement the digest()
        :param content:
        :return:
        """
        raise Exception("You should use a subclass and implement this method inside")

    def get_most_compliant_tone_and_mode(self) -> dict:
        """
        returns the most probable tone and mode
        :return:
        """
        best_compliance = {"compliance_rate": 0, "tone": "?", "cof_name": "?", "scale": [], "harmonic suite": []}
        for mode in self.cof.cof_tone_compliances.keys():
            for tone in self.cof.cof_tone_compliances[mode].keys():
                if self.cof.cof_tone_compliances[mode][tone]["compliance_rate"] > best_compliance["compliance_rate"]:
                    best_compliance = self.cof.cof_tone_compliances[mode][tone]
        return best_compliance

    def generate_degrees_from_chord_progression(self):
        """
        set song degrees from the song suspected key into self.degrees
        :return:
        """
        self.degrees = []
        chords_string = " ".join(self.get_recognized_chords())
        cp = self.cof.digest_song(chords_string)
        suspected_key = {}
        if len(self.cof.cof_tone_compliances.keys()) <= 1:
            suspected_key = self.cof.digest_possible_tones_and_modes(cp)
        else:
            suspected_key = self.get_most_compliant_tone_and_mode()
        for cs in self.chords_sequence:
            deg = self.get_degree(suspected_key, cs)
            self.degrees.append(deg)

    def get_remarquable_cadences(self) -> dict:
        """
        show remarkable cadences in tabs
        :return: The returned dictionary provides for each cadence the chord position the progression starts
        """
        if not self.degrees:
            self.generate_degrees_from_chord_progression()

        self.remarquable_cadences = {}
        song_degrees = "-".join(self.degrees)
        for c in Cadence.REMARQUABLE_CADENCES_NATURAL_MAJOR:
            key = f"REMARQUABLE_CADENCES_NATURAL_MAJOR:{c}"
            for deg in range(0, len(self.degrees)):
                if song_degrees[deg:].startswith(Cadence.REMARQUABLE_CADENCES_NATURAL_MAJOR[c]):
                    if key not in self.remarquable_cadences.keys():
                        self.remarquable_cadences[key] = []
                    self.remarquable_cadences[key].append(deg)
        for c in Cadence.REMARQUABLE_CADENCES_NATURAL_MINOR:
            key = f"REMARQUABLE_CADENCES_NATURAL_MINOR:{c}"
            for deg in range(0, len(self.degrees)):
                if song_degrees[deg:].startswith(Cadence.REMARQUABLE_CADENCES_NATURAL_MINOR[c]):
                    if key not in self.remarquable_cadences.keys():
                        self.remarquable_cadences[key] = []
                    self.remarquable_cadences[key].append(deg)
        for c in Cadence.REMARQUABLE_CADENCES_HYBRID:
            key = f"REMARQUABLE_CADENCES_HYBRID:{c}"
            for deg in range(0, len(self.degrees)):
                if song_degrees[deg:].startswith(Cadence.REMARQUABLE_CADENCES_HYBRID[c]):
                    if key not in self.remarquable_cadences.keys():
                        self.remarquable_cadences[key] = []
                    self.remarquable_cadences[key].append(deg)
        return self.remarquable_cadences

    def get_degree(self, tonality: dict, c: Chord) -> str:
        """
        return degree of c within a tonality
        :param tonality:
        :param c:
        :return:
        """
        deg = 0
        root_found = False
        interval = 0
        for d in tonality["harmonic suite"]:
            deg += 1
            d_chord = Chord(d)
            if d_chord.root == c.root:
                root_found = True
                break
        if not root_found:
            deg = 0
            for d in tonality["harmonic suite"]:
                deg += 1
                d_chord = Chord(d)
                if ord(d_chord.root[0]) == ord(c.root[0]):
                    root_found = True
                    interval = Note(d_chord.root).get_interval_in_half_tones(Note(c.root))
                    break

        sharp = ""
        if interval != 0:
            sharp = "#"

        if deg == 1:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"i{sharp}{c.quality.quality[1:]}"
            else:
                return f"I{sharp}{c.quality.quality}"
        elif deg == 2:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"ii{sharp}{c.quality.quality[1:]}"
            else:
                return f"II{sharp}{c.quality.quality}"
        elif deg == 3:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"iii{sharp}{c.quality.quality[1:]}"
            else:
                return f"III{sharp}{c.quality.quality}"
        elif deg == 4:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"iv{sharp}{c.quality.quality[1:]}"
            else:
                return f"IV{sharp}{c.quality.quality}"
        elif deg == 5:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"v{sharp}{c.quality.quality[1:]}"
            else:
                return f"V{sharp}{c.quality.quality}"
        elif deg == 6:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"vi{sharp}{c.quality.quality[1:]}"
            else:
                return f"VI{sharp}{c.quality.quality}"
        elif deg == 7:
            if c.quality.quality.startswith("m") and not c.quality.quality.startswith("maj7"):
                return f"vii{sharp}{c.quality.quality[1:]}"
            else:
                return f"VII{sharp}{c.quality.quality}"
        else:
            raise ValueError(f"Degree calculation error with {str(c)} in {str(tonality)}")

    def transpose(self, number_half_tone: int) -> []:
        """
        updates self.chords_sequence with a chord sequence transposed to number_half_tone
        :param number_half_tone: number of 1/2 tones from the CoF root note
        :return:
        """
        res = []
        chords_string = " ".join(self.get_recognized_chords())
        cp = self.cof.digest_song(chords_string)
        if len(self.cof.cof_tone_compliances.keys()) <= 1:
            suspected_key = self.cof.digest_possible_tones_and_modes(cp)
        else:
            suspected_key = self.get_most_compliant_tone_and_mode()
        root_note = Note(suspected_key["tone"])
        root_note.transpose(number_half_tone)
        cof = CircleOf5th.cof_factory(suspected_key["cof_name"])
        for d in self.degrees:
            deg = Degree()
            c = deg.get_chord_from_degree(d, str(root_note), cof)
            res.append(c)
        self.chords_sequence = res
        return res
