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
        if self.cof.cof_tone_compliances == {}:
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
