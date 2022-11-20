from src.displays.console import HarmonyLogger
from src.song.text_song import TextSongWithLineForChords

song = """
Am Em Am Em G Gmaj7 Em         """
HarmonyLogger.outcome_level_of_detail = HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
