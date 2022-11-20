from src.harmony.circle_of_5th import CircleOf5thNaturalMajor
from src.song.ultimate_guitar_search import UltimateGuitarSearch

ugs = UltimateGuitarSearch()
cof_maj = CircleOf5thNaturalMajor()
songs = ugs.search_songs_from_cadence("ii7-V7-Imaj7", cof_maj, 5)
print(songs)