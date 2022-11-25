from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class Cadence:
    REMARQUABLE_CADENCES = {
        "ANATOLE": "ii7-V7-Imaj7",  # https://en.wikipedia.org/wiki/Ii%E2%80%93V%E2%80%93I_progression
        "PHRYGIAN_HALF_CADENCE": "v–iv6–V",   # https://en.wikipedia.org/wiki/Cadence#Phrygian_half_cadence
        "MINOR_PLAGAL_CADENCE": "IV-iv-I",  # Minor Plagal Cadence found in "My Way" https://en.wikipedia.org/wiki/Cadence#Minor_plagal_cadence
        "VIIb_V7_I": "bVII–V7-I", # https://en.wikipedia.org/wiki/%E2%99%ADVII%E2%80%93V7_cadence
        "III_VI_II_V": "III–VI–II–V",     # https://en.wikipedia.org/wiki/Ii%E2%80%93V%E2%80%93I_progression
        "I_V_vi_IV": "I–V–vi–IV", # https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression
        "I_IV_bVII_IV": "I–IV–bVII–IV",   # https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression#I%E2%80%93V%E2%80%93%E2%99%ADVII%E2%80%93IV
        "PACHELBEL'S CANON": "I–V–vi–iii–IV–I–IV–V",   # https://en.wikipedia.org/wiki/Pachelbel%27s_Canon
        "RAGTIME":  "III7–VI7–II7–V7",   # https://en.wikipedia.org/wiki/Ragtime_progression
        "I−vi−ii−V": "I−vi−ii−V",   # https://en.wikipedia.org/wiki/I%E2%88%92vi%E2%88%92ii%E2%88%92V
        "bVI-bVII-I": "bVI-bVII-I"  # https://www.studybass.com/lessons/harmony/the-flat-vi-flat-vii-i-cadence/

    }

    def __init__(self):
        self.ugs = UltimateGuitarSearch

    def get_song_samples(self, cadence: str, cof: CircleOf5th, max_songs: int) -> dict:
        """
        returns songs from a cadence
        todo the mode should rather be guessed from the cadence
        :param cadence:
        :param cof:
        :param max_songs:
        :return:
        """
        songs = self.ugs.search_songs_from_cadence(cadence, cof, max_songs, matches_exactly=True,
                                                   try_avoiding_blocked_searches=True)
        return songs
