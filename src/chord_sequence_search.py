from src.song.song import UltimateGuitarSong
from src.song.ultimate_guitar_search import UltimateGuitarSearch

ug_engine = UltimateGuitarSearch()
query = "D Dm A"
urls = ug_engine.search(query, 20)
song = UltimateGuitarSong()
for link in urls:
    print("===================================")
    print("===================================")
    print("===================================")
    song.extract_song_from_url(link)
    print(song.get_string())
