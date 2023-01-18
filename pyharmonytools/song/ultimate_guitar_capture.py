from lxml import html
import requests

from pyharmonytools.song.ultimate_guitar_song import UltimateGuitarSong

for page in range(1, 50):
    print(f"------ page {page} -------")
    if page == 1:
        the_page = ""
    else:
        the_page = f"page={page}&"

    url = f"https://www.ultimate-guitar.com/explore?order=date_desc&{the_page}type[]=Chords"

    print(f"Trying to retrieve {url}...")
    page = requests.get(url)
    data_content = str(page.content).split('<div class="js-store" data-content')[1].split('"></div>')[0]
    parts = data_content.split(";:&quot;")
    for p in parts:
        if p.startswith("https://tabs"):
            url_song = p.split("&quot;")[0]
            print(url_song)
            song = UltimateGuitarSong()
            try:
                song.extract_song_from_url(url_song)
                song.store_song("c:/chords")
            except Exception as e:
                print(str(e))
