from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.degree import Degree
from pyharmonytools.harmony.note import Note
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class Cadence:
    REMARQUABLE_CADENCES_NATURAL_MAJOR = {
        "AUTHENTIC CADENCE": "V–I", # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "PLAGAL CADENCE": "IV–I", # https://musictheory.pugetsound.edu/mt21c/cadences.html
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
        "bVI-bVII-I": "bVI-bVII-I",  # https://www.studybass.com/lessons/harmony/the-flat-vi-flat-vii-i-cadence/
        "HALF CADENCE": "ii–V",    # https://www.schoolofcomposition.com/cadences-in-music/
        "DECEPTIVE CADENCE": "V-ii",  # https://www.schoolofcomposition.com/cadences-in-music/
        "DECEPTIVE CADENCE 2": "V–vi",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 3": "V7–vi",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 4": "Vsus–vi7",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 5": "V7–VI",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 6": "V–IV/3rd",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "MELANCOLIC JOY": "I-IM7-I7",   # eg. Jamie Cullum's "It's Christmas" https://tabs.ultimate-guitar.com/tab/jamie-cullum/its-christmas-chords-4335365
        "FREEDOM": "V-IV-I",   # eg. https://tabs.ultimate-guitar.com/tab/george-michael/freedom-90-chords-8344
        "S. WONDER's 251": "IImaj7-V9sus4-Imaj7",   # https://www.youtube.com/shorts/J8IV_umUdUo
        # "*":"any chord" /  "]":"a phrase ending on"
        "HALF CADENCE_GENERIC": "*-V]",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
    }
    REMARQUABLE_CADENCES_MELODIC_MINOR = {
        "SUSPENS RISING": "i°-i#°-ii°",  # eg. https://tabs.ultimate-guitar.com/tab/the-specials/ghost-town-chords-2572791
    }

    def __init__(self):
        pass

    def get_song_samples(self, cadence: str, cof: CircleOf5th, max_songs: int) -> dict:
        """
        returns songs from a cadence
        todo the mode should rather be guessed from the cadence
        :param cadence:
        :param cof:
        :param max_songs:
        :return:
        """
        ugs = UltimateGuitarSearch
        songs = ugs.search_songs_from_cadence(cadence, mode=cof,
                                              limit_per_tone=max_songs,
                                              matches_exactly=True,
                                              try_avoiding_blocked_searches=True)
        return songs

    def get_chords_sequences(self, cadence: str, cof: CircleOf5th) -> {}:
        """
        return chords sequence in all 12 keys
        :param cof:
        :param cadence: eg. "III–VI–II–V"
        :return:
        """
        res = {}
        degrees = cadence.split("-")
        for root_note in Note.CHROMATIC_SCALE_SHARP_BASED:
            search_string = ""
            for degree in degrees:
                chord = Degree.get_chord_from_degree(degree, root_note, cof)
                search_string += chord + " "
            res[root_note] = search_string
        return res

