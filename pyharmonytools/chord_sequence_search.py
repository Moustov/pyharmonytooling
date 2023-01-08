from pyharmonytools.harmony.circle_of_5th import CircleOf5thNaturalMajor
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
cadence = "I-V-vi-iii-IV-I-IV-V"

cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)
MAX_SONG_PER_SEARCH = 5

songs = ugs.search_songs_from_cadence(cadence, cof_maj, MAX_SONG_PER_SEARCH, matches_exactly=True,
                                      try_avoiding_blocked_searches=True)
print(songs)
