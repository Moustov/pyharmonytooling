from pychord import Chord

from pyharmonytools.song.song import Song


class TextSongWithLineForChords(Song):
    def __init__(self):
        super().__init__()

    def digest(self, content: str):
        self.chords_sequence = []
        self.lyrics = []
        self.artist = "Unknown"
        self.song_title = "Unknown"

        lines = content.split("\n")
        chord_found = False
        a_line = ""
        for line in lines:
            words = line.split()
            chord_found = False
            a_line = ""
            for w in words:
                try:
                    chord = Chord(w)
                    self.chords_sequence.append(chord)
                    chord_found = True
                except:
                    if not chord_found:
                        a_line += " " + w
            if not chord_found and a_line.strip() != "":
                self.lyrics.append(a_line.strip())

