from src.harmony.circle_of_5th import CircleOf5thNaturalMajor
from src.song.ultimate_guitar_search import UltimateGuitarSearch

ugs = UltimateGuitarSearch()
cadence = "ii7-V7-Imaj7"
# the mode should rather be guessed from the cadence
cof_maj = CircleOf5thNaturalMajor.guess_tone_and_mode_from_cadence(cadence)

songs = ugs.search_songs_from_cadence(cadence, cof_maj, 5, matches_exactly=True, try_avoiding_blocked_searches=True)
print(songs)
