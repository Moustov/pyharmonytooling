from src.harmony.harmony_tools import digest_song, guess_tone_and_mode

song = """
      A           E
Happy Birthday to you
      E           A
Happy Birthday to you
      A7            D
Happy Birthday dear (name)
      A        E    A
Happy Birthday to you
"""
cp = digest_song(song)
compliance_level_max = guess_tone_and_mode(cp)
print(compliance_level_max)

