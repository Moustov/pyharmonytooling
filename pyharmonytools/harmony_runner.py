from pyharmonytools.displays.console import _HarmonyLogger
from pyharmonytools.song.text_song import TextSongWithLineForChords

song = """
D6 Bm7         Em   A7(6)   D6            Bm7      Em      A7(6)    D6
É melhor ser alegre que ser triste, A alegria é melhor coisa que existe
   Bm7          Em    A7/6  D6/9 Em6 D6/9 Em6
É assim como a luz no cora- ção
D6        Bm7    Em    A7/6 D6          Bm7       Em   A7/6  D6
Mas pra fazer um samba com beleza, É preciso um bocado de tristeza
   Bm7       Em   A7/6   D6       Bm7        Em     A7/6  D6 A7 D6 A7
Preciso um bocado de tristeza, Se não não se faz um samba não
D6    Bm7       Em     A7/6  D6             Bm7   Em       A7/6 D6
Fazer samba não é con- tar piada, Quem faz samba assim não é de nada
Bm7 Em A7/6 D6/9 Em6 D6/9 Em6
Um bom samba é uma forma de ora- ção
D6 Bm7 Em A7/6 D6 Bm7 Em A7/6 D6
Porque o samba é a tristeza que balança, E a tristeza tem sempre uma esperança
D6 Bm7 Em A7/6 D6 Bm7 Em A7/6 D6 A7 D6 A7
A tristeza tem sempre uma esperança, De um dia não ser mais triste não
D6 Bm7 Em A7/6 D6 Bm7 Em A7/6 D6
Ponha um pouco de amor, uma cadencia, E vai ver que ninguem no mundo vence
D6 Bm7 Em A7/6 D6/9 Em6 D6/9 Em6
A beleza que tem um samba, não
D6 Bm7 Em A7/6 D6 Bm7 Em A7/6 D6
Porque o samba nasceu lá na Bahia, E se hoje ele é branco na poesia
D6 Bm7 Em A7/6 D6 Bm7 Em A7/6 D6
Se hoje é branco na poesia, Ele é negro e demais no cora- ção         """
_HarmonyLogger.outcome_level_of_detail = _HarmonyLogger.LOD_NONE
the_song = TextSongWithLineForChords()
the_song.digest(song)
compliance_level_max = the_song.get_tone_and_mode()
print("Compliance:", compliance_level_max)
borrowed_chords = the_song.get_borrowed_chords()
print("Borrowed chords:", borrowed_chords)
