from src.displays.console import _HarmonyLogger
from src.song.text_song import TextSongWithLineForChords

song = """
Am Em Am Em G Gmaj7 Em         """
_HarmonyLogger.outcome_level_of_detail = _HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
