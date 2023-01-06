from pychord import Chord

from pyharmonytools.harmony.circle_of_5th import CircleOf5th


class Song:
    def __init__(self):
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

    def get_degree(self, tonality: dict, c: Chord) -> str:
        """
        return degree of c within a tonality
        :param tonality:
        :param c:
        :return:
        """
        deg = 0
        for d in tonality["harmonic suite"]:
            deg += 1
            d_chord = Chord(d)
            if d_chord.root == c.root:
                break
        if deg == 1:
            return f"I{c.quality.quality}"
        if deg == 2:
            return f"II{c.quality.quality}"
        if deg == 3:
            return f"III{c.quality.quality}"
        if deg == 4:
            return f"IV{c.quality.quality}"
        if deg == 5:
            return f"V{c.quality.quality}"
        if deg == 6:
            return f"VI{c.quality.quality}"
        if deg == 7:
            return f"VII{c.quality.quality}"
