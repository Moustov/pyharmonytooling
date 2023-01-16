from pyharmonytools.harmony.cadence import Cadence
from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor_4notes, CircleOf5thNaturalMajor_triads, \
    CircleOf5th
from pyharmonytools.song.ultimate_guitar_search import UltimateGuitarSearch

ug_engine = UltimateGuitarSearch()
# query = "A C D Dm"
# urls = ug_engine.search(query, 3, matches_exactly=True)
# song = UltimateGuitarSong()
# for link in urls:
#     print("===================================")
#     print("===================================")
#     print("===================================")
#     song.extract_song_from_url(link)
#     print(song)

ugs = UltimateGuitarSearch()
cadence = "V-IV-#ii7-VII-vii7-I-V"

cadence_and_tone = Cadence.guess_tone_and_mode_from_cadence(cadence)
MAX_SONG_PER_SEARCH = 5

cof = CircleOf5th.cof_factory(cadence_and_tone["cof_name"])
songs = ugs.search_songs_from_cadence(cadence, cof, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                      try_avoiding_blocked_searches=True)
print(songs)
