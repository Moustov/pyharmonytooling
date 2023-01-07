from pyharmonytools.harmony.circle_of_5th import CircleOf5th
from pyharmonytools.harmony.degree import Degree
from pyharmonytools.harmony.note import Note
# from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch


class Cadence:
    REMARQUABLE_CADENCES_NATURAL_MAJOR = {
        "AUTHENTIC CADENCE": "V-I",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "PLAGAL CADENCE": "IV-I",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "ANATOLE": "ii7-V7-Imaj7",  # https://en.wikipedia.org/wiki/Ii%E2%80%93V%E2%80%93I_progression
        "VIIb_V7_I": "VIIb-V7-I",  # https://en.wikipedia.org/wiki/%E2%99%ADVII%E2%80%93V7_cadence
        "I_V_vi_IV": "I-V-vi-IV",  # https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression
                                    # https://www.youtube.com/watch?v=AbW3sES2zCw
        "SAD BUT UPLIFTING": "vi-V-IV-V",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "SECONDARY DOMINANTS": "IV-V-V6/vi-vi",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "I_IV_bVII_IV": "I-IV-VIIb-IV",
        # https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression#I%E2%80%93V%E2%80%93%E2%99%ADVII%E2%80%93IV
        "PACHELBEL'S CANON": "I-V-vi-iii-IV-I-IV-V",  # https://en.wikipedia.org/wiki/Pachelbel%27s_Canon
        "RAGTIME": "III7-VI7-II7-V7",  # https://en.wikipedia.org/wiki/Ragtime_progression
        "JAZZ IT UP": "I−vi−ii−V",  # https://en.wikipedia.org/wiki/I%E2%88%92vi%E2%88%92ii%E2%88%92V
                                    # https://www.youtube.com/watch?v=eVteycbJUsw
        "bVI-bVII-I": "VIb-VIIb-I",  # https://www.studybass.com/lessons/harmony/the-flat-vi-flat-vii-i-cadence/
        "HALF CADENCE": "ii-V",  # https://www.schoolofcomposition.com/cadences-in-music/
        "DECEPTIVE CADENCE": "V-ii",  # https://www.schoolofcomposition.com/cadences-in-music/
        "DECEPTIVE CADENCE 2": "V-vi",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 3": "V7-vi",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 4": "Vsus-vi7",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "DECEPTIVE CADENCE 6": "V-IV/3rd",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "MELANCOLIC JOY": "I-IM7-I7",  # eg. Jamie Cullum's "It's Christmas" https://tabs.ultimate-guitar.com/tab/jamie-cullum/its-christmas-chords-4335365
        "CANON": "I-V-vi-iii-IV-I-IV-V", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "FREEDOM": "V-IV-I",  # eg. https://tabs.ultimate-guitar.com/tab/george-michael/freedom-90-chords-8344
        "S. WONDER's 251": "IImaj7-V9sus4-Imaj7",  # https://www.youtube.com/shorts/J8IV_umUdUo
        "3-6-2-5 TURNAROUND": "III-VI-II-V",  # https://www.youtube.com/watch?v=hWCX9-DnMG0
        "STORYTELLER": "I-IV-vi-V",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "I-IV-vi-IV": "I-IV-vi-IV",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "BASS PLAYER": "I-ii7-I6-IV",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "JOURNEY": "IV-I6-V",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "I-V-IV": "I-V-IV",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "I-IV": "I-IV",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "IV-V-I-vi": "IV-V-I-vi",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "I-IV-V": "I-IV-V",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "IV-I-V-vi": "IV-I-V-vi",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "vi-IV-I-V": "vi-IV-I-V",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "BELIEVE": "I-V-ii-IV",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "DOO-WOP CHANGES": "I-vi-IV-V",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "50s PROGRESSION": "I-vi-IV-V",  # https://www.youtube.com/watch?v=AbW3sES2zCw
        "I-IV-V-IV": "I-IV-V-IV", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "I-IV-ii-V": "I-IV-ii-V", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "I-IV-I-V": "I-IV-I-V", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "I-ii-iii-IV-V": "I-ii-iii-IV-V", # https://www.musical-u.com/learn/exploring-common-chord-progressions/

        # {'A F#m7 Bm7 E7 ': [], 'A# Gm7 Cm7 F7 ': [], 'B G#m7 C#m7 F#7 ': [], 'C Am7 Dm7 G7 ': ['https://tabs.ultimate-guitar.com/tab/charles-aznavour/donne-donne-moi-ton-coeur-chords-4448435', 'https://tabs.ultimate-guitar.com/tab/charles-trenet/route-nationale-7-chords-2399405', 'https://tabs.ultimate-guitar.com/tab/4399226', 'https://tabs.ultimate-guitar.com/tab/misc-christmas/have-yourself-a-merry-little-christmas-chords-1007691', 'https://tabs.ultimate-guitar.com/tab/charles-trenet/douce-france-chords-1700887'], 'C# A#m7 D#m7 G#7 ': ['https://tabs.ultimate-guitar.com/tab/charles-aznavour/donne-donne-moi-ton-coeur-chords-4448435', 'https://tabs.ultimate-guitar.com/tab/misc-musicals/something-rotten-right-hand-man-chords-3647228', 'https://tabs.ultimate-guitar.com/tab/jimmie-rodgers/secretly-chords-1407072', 'https://tabs.ultimate-guitar.com/tab/joe-hisaishi/sanpo-a-walk-chords-1237044', 'https://tabs.ultimate-guitar.com/tab/joe-hisaishi/sanpo-a-walk-ukulele-1391150'], 'D Bm7 Em7 A7 ': ['https://tabs.ultimate-guitar.com/tab/charles-aznavour/jaime-paris-au-mois-de-mai-chords-2955164', 'https://tabs.ultimate-guitar.com/tab/lou-berry/blue-sky-chords-2881406', 'https://tabs.ultimate-guitar.com/tab/2959910', 'https://tabs.ultimate-guitar.com/tab/the-beautiful-south/les-yeux-ouverts-ukulele-1470609', 'https://tabs.ultimate-guitar.com/tab/sabrina-carpenter/im-fine-chords-4289981'], 'D# Cm7 Fm7 A#7 ': [], 'E C#m7 F#m7 B7 ': ['https://tabs.ultimate-guitar.com/tab/charles-trenet/le-piano-de-la-plage-chords-4396265', 'https://tabs.ultimate-guitar.com/tab/wings/goodnight-tonight-ukulele-2263035'], 'F Dm7 Gm7 C7 ': ['https://tabs.ultimate-guitar.com/tab/the-beatles/i-will-chords-17421', 'https://tabs.ultimate-guitar.com/tab/james-taylor/carolina-in-my-mind-chords-1970905', 'https://tabs.ultimate-guitar.com/tab/michel-delpech/la-vie-la-vie-chords-4203580', 'https://tabs.ultimate-guitar.com/tab/charles-trenet/le-piano-de-la-plage-chords-4396265', 'https://tabs.ultimate-guitar.com/tab/ben-loncle-soul/mon-amour-chords-1737579'], 'F# D#m7 G#m7 C#7 ': ['https://tabs.ultimate-guitar.com/tab/michel-delpech/la-vie-la-vie-chords-4203580', 'https://tabs.ultimate-guitar.com/tab/enzo-enzo/les-yeux-ouverts-chords-3331703', 'https://tabs.ultimate-guitar.com/tab/jack-van-gelder/summer-holiday-chords-3729350', 'https://tabs.ultimate-guitar.com/tab/jacob-banks/by-design-evel-knievel-chords-4332377'], 'G Em7 Am7 D7 ': ['https://tabs.ultimate-guitar.com/tab/3856097', 'https://tabs.ultimate-guitar.com/tab/3951392', 'https://tabs.ultimate-guitar.com/tab/etta-james/at-last-chords-2786473', 'https://tabs.ultimate-guitar.com/tab/sam-cooke/you-send-me-chords-212936', 'https://tabs.ultimate-guitar.com/tab/adele/all-night-parking-chords-3955127'], 'G# Fm7 A#m7 D#7 ': ['https://tabs.ultimate-guitar.com/tab/eva-weel-skram/tid-med-mjuke-pakkar-chords-4426565']}
        "AT LAST":  "I-vi7-ii7-V7", # Etta James https://tabs.ultimate-guitar.com/tab/etta-james/at-last-chords-1118407
        #"SAMBA DE BENCAO" = "AT LAST"
        "SAMBA SARAVAH":    "I6-ii7-V7",   # Pierre Barouh https://tabs.ultimate-guitar.com/tab/pierre-barouh/samba-saravah-chords-4454282
        # "*":"any chord" /  "]":"a phrase ending on"
        "HALF CADENCE_GENERIC": "*-V]",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
    }

    REMARQUABLE_CADENCES_NATURAL_MINOR = {
        "i-iv-v-i": "i-iv-v-i",  # https://www.study-guitar.com/blog/minor-key-chord-progressions/
        "i-ii°-v-i": "i-iidim-v-i",  # https://www.study-guitar.com/blog/minor-key-chord-progressions/
        "i-VI-III-VII": "i-VI-III-VII",  # https://www.study-guitar.com/blog/minor-key-chord-progressions/
        "i-VII-VI-VII-i": "i-VII-VI-VII-i",  # https://www.study-guitar.com/blog/minor-key-chord-progressions/
        "i-VII-VI-V7": "i-VII-VI-V7",  # https://www.study-guitar.com/blog/minor-key-chord-progressions/
        "i-VI-VII": "i-VI-VII", # https://www.fretjam.com/natural-minor-chord-progressions.html
        "i-III-VII-VI": "i-III-VII-VI",  # https://www.fretjam.com/natural-minor-chord-progressions.html
        "i-VII-iv-VI": "i-VII-iv-VI",  # https://www.fretjam.com/natural-minor-chord-progressions.html
        "i-v-VI-VII": "i-v-VI-VII",  # https://www.fretjam.com/natural-minor-chord-progressions.html
        "i-v-VII-iv": "i-v-VII-iv",  # https://www.fretjam.com/natural-minor-chord-progressions.html
        "i-v-iv-VII": "i-v-iv-VII",  # https://www.fretjam.com/natural-minor-chord-progressions.html
    }

    REMARQUABLE_CADENCES_HYBRID = {
        "SUSPENS RISING": "idim-i#dim-iidim",  # eg. https://tabs.ultimate-guitar.com/tab/the-specials/ghost-town-chords-2572791
        "PHRYGIAN_HALF_CADENCE": "v-iv6-V",  # https://en.wikipedia.org/wiki/Cadence#Phrygian_half_cadence
        "MINOR_PLAGAL_CADENCE": "IV-iv-I", # Minor Plagal Cadence found in "My Way" https://en.wikipedia.org/wiki/Cadence#Minor_plagal_cadence
        "DECEPTIVE CADENCE 5": "V7-VI",  # https://musictheory.pugetsound.edu/mt21c/cadences.html
        "III_VI_II_V": "III-VI-II-V",  # https://en.wikipedia.org/wiki/Ii%E2%80%93V%E2%80%93I_progression
        "EPIC PROGRESSION": "I-bVI-V",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "I-III-IV-iv": "I-III-IV-iv",  # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "i-V-i-iv": "i-V-i-iv", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
        "MINOR CHANGE": "IV-iv-I",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "TRAP CHORDS": "i-VI-i-v",  # https://www.youtube.com/watch?v=eVteycbJUsw
        "ANDALUSIAN CADENCE": "vi-V-IV-III", # https://www.musical-u.com/learn/exploring-common-chord-progressions/
    }

    def __init__(self):
        pass

    def get_chords_sequences(self, cadence: str, cof: CircleOf5th) -> {}:
        """
        return chords sequence in all 12 keys
        :param cof:
        :param cadence: eg. "III-VI-II-V"
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
