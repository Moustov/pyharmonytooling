from src.song.ultimate_guitar_song import UltimateGuitarSong
from src.song.ultimate_guitar_search import UltimateGuitarSearch

ug_engine = UltimateGuitarSearch()
query = "C Cm G"
urls = ug_engine.search(query, 3, matches_exactly=True, try_avoiding_blocked_searches=True)
song = UltimateGuitarSong()
for link in urls:
    print("===================================")
    print("===================================")
    print("===================================")
    song.extract_song_from_url(link)
    print(song)
