from unittest import TestCase

from deepdiff import DeepDiff
from pychord import Chord
from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.song.text_song import TextSongWithLineForChords


class TestTextSong(TestCase):
    ut_report = UnitTestReport()
    song_happy_birthday = """
                        A           E
                Happy Birthday to you
                      E           A
                Happy Birthday to you
                      A7            D
                Happy Birthday dear (name)
                      A        E    A
                Happy Birthday to you
            """
    song_sometimes = """
            [Verse]
            A          G
            Tough, you think you've got the stuff
                   F#m            D
            You're telling me and anyone
                   A
            You're hard enough
                A
            You don't have to put up a fight
                G
            You don't have to always be right
            F#m                     D
            Let me take some of the punches
                A
            For you tonight

            [Verse]
            [F -> C -> Dm]
            I know that we don't talk
            [F -> C -> Am]
            I'm sick of it all
            [F -> C -> Dm]         A
            Can you hear me when I Sing,
                   F#m
            you're the reason I sing
            D                 E       A
            You're the reason why the opera is in me

            [Pre Chorus]
                  D
            Yeah, hey now
                                 A
            Still got to let you know
                                         F#m
            A house still doesn't make a home
                                 D
            Don't leave me here alone

            [Chorus]
                     F#m                       E
            And it's you when I look in the mirror
                     D                             D
            And it's you that makes it hard to let go
            F#m                 E               D
            Sometimes you can't make it on your own
            F#m                 E
            Sometimes you can't make it
                         D
            The best you can do is to fake it
            F#m                 E        D
            Sometimes you can't make it on your own
            """
    song_evenou = """
           Dm
    Hevenu Sha- lom halerem
           Gm
    Hevenu Sha- lom halerem
           A7       Gm
    Hevenu Sha- lom ha- lerem
           A7        A7        A7           Dm
    Hevenu Sha- lom, Sha- lom, Sha- lom halerem

    [Verse 1]
                 Dm
    Nous vous a- nnoncons la paix,
                 Gm
    Nous vous a- nnonçons la paix,
                 A7            Dm
    Nous vous a- nnon- çons la paix
                        A7       A7       A7           Dm
    Nous vous annonçons la paix, la paix, la paix en Jésus

    [Verse 2]
                 Dm
    Nous vous a- nnoncons la joie,
                 Gm
    Nous vous a- nnonçons la joie,
                 A7            Dm
    Nous vous a- nnon- çons la joie
                        A7       A7       A7           Dm
    Nous vous annonçons la joie, la joie, la joie en Jésus-Christ

    [Verse 3]
                 Dm
    Nous vous a- nnoncons l'amour,
                 Gm
    Nous vous a- nnonçons l'amour,
                 A7           Dm
    Nous vous a- nnon- çons l'amour
                          A7       A7       A7       Dm
    Nous vous annonçons l'amour, l'amour, l'amour en Jésus

    [Verse 4]
                 Dm
    Nous vous a- nnoncons la paix,
                 Gm
    Nous vous a- nnonçons la joie,
                 A7           Dm
    Nous vous a- nnon- çons l'amour
                        A7       A7         A7       Dm
    Nous vous annonçons la paix, la joie, l'amour en Jésus        """
    song_saravah = """[Intro]
D6/F#  Em7/B  A7  D6/F#  D6/F#  Em7/B  A7  D6/F#
 
[Verse]
D6/F#         Em7/B    A7    D6/F#
Etre heureux, c'est plus ou moins ce qu'on cherche
            Em7/B    A7    D6/F#
J'aime rire, chanter et je n'empêche
        Em7/B    A7    D6/F#     Db6/F  A7
Pas les gens qui sont bien d'être joyeux
D6/F#             Em7/B    A7    D6/F#
Pourtant s'il est une samba sans tristesse
               Em7/B  A7   D6/F#
C'est un vin qui ne donne pas l'ivresse
               Em7/B  A7   D6/F#
Un vin qui ne donne pas l'ivresse
              Em7/B    A7    D6/F#     Db6/F  A7
Non, ce n'est pas la samba que je veux
 
[Instrumental]
D6/F#   Em7/B    A7
[Parlando]
 
"Faire une samba sans tristesse,
 
C'est aimer une femme qui ne serait que belle."
 
Ce sont les propres paroles de Vinicius de Moraes,
 
Poète et diplomate auteur de cette chanson,
 
Et comme il le dit lui-même, le blanc le plus noir du Brésil.
 
Moi qui suis peut-être le Français le plus brésilien de France,
 
J'aimerais vous parler de mon amour de la samba,
 
Comme un amoureux qui n'osant pas parler à celle qu'il aime,
 
En parlerait à tous ceux qu'il rencontre
 
[Verse]
D6/F#         Em7/B    A7    D6/F#
J'en connais que la chanson incommode
            Em7/B    A7    D6/F#
D'autres pour qui ce n'est rien qu'une mode
        Em7/B    A7    D6/F#     Db6/F  A7
D'autres qui en profitent sans l'aimer
D6/F#             Em7/B    A7    D6/F#
Moi je l'aime et j'ai parcouru le monde
               Em7/B  A7   D6/F#
En cherchant ses racines vagabondes
               Em7/B  A7   D6/F#
Aujourd'hui pour trouver les plus profondes
              Em7/B    A7    D6/F#     Db6/F  A7
C'est la samba chanson qu'il faut chanter
 
 
[Instrumental]
D6/F#   Em7/B    A7
 
[Parlando]
João Gilberto, Carlos Lyra, Dorival Caymmi,
 
Antonio Carlos Jobim, Vinicius de Moraes.
 
Baden Powell qui a fait la musique de cette chanson
 
Et de tant d'autres, vous avez mon salut
 
Ce soir je voudrais boire jusqu'à l'ivresse
 
Pour mieux délirer sur tous ceux que grâce à vous j'ai découvert
 
Et qui ont fait de la samba ce qu'elle est, saravah
 
Pixinginha, Noel Rosa, Dolores Duran, Cyro Monteiro et tant d'autres
 
Et tout ceux qui viennent, Edu Lobo, et mes amis qui sont avec moi ce soir,
 
Baden bien sûr, Ico, Oswaldo, Luigi, Oscar, Nicolino, Milton. Saravah
 
Tous ceux-là qui font qu'il est un mot que plus jamais
 
je ne pourrai prononcer sans frissonner.
 
Un mot qui secoue tout un peuple en le faisant chanter,
 
Les mains levées au ciel
 
[Verse]
D6/F#       Em7/B  A7    D6/F#
On m'a dit qu'elle venait de Bahia
                  Em7/B  A7  D6/F#
Qu'elle doit s'enrhumer, sa poésie a
              Em7/B    A7    D6/F#     Db6/F  A7
Des siècles de danse et de douleurs
  D6/F#       Em7/B  A7    D6/F#
Mais quel que soit le sentiment qu'elle exprime
               Em7/B  A7    D6/F#
Elle est blanche de formes et de rimes
               Em7/B  A7    D6/F#
Blanche de formes et de rimes
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur
 
[Outro]
  D6/F#       Em7/B  A7    D6/F#
Mais quel que soit le sentiment qu'elle exprime
               Em7/B  A7    D6/F#
Elle est blanche de formes et de rimes
               Em7/B  A7    D6/F#
Blanche de formes et de rimes
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur
  D6/F#       Em7/B  A7    D6/F#
Mais quel que soit le sentiment qu'elle exprime
               Em7/B  A7    D6/F#
Elle est blanche de formes et de rimes
               Em7/B  A7    D6/F#
Blanche de formes et de rimes
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur
 D6/F#  Em7/B  A7    D6/F#  Db6/F  A7
Elle est nègre, bien nègre dans son cœur"""

    def test_digest(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_happy_birthday)
        print(the_song.chords_sequence)
        self.ut_report.assertTrue(the_song.chords_sequence == [Chord("A"), Chord("E"), Chord("E"), Chord("A"),
                                                               Chord("A7"), Chord("D"), Chord("A"), Chord("E"),
                                                               Chord("A")])

    def test_compliance(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_happy_birthday)
        compliance_level_max = the_song.get_tone_and_mode()
        print("Compliance:", compliance_level_max)
        self.ut_report.assertTrue(compliance_level_max["compliance_rate"] == 1.0)
        self.ut_report.assertTrue(compliance_level_max["tone"] == "A")
        self.ut_report.assertTrue(compliance_level_max["cof_name"] == "Natural Major")
        print(the_song.chords_sequence)
        borrowed_chords = the_song.get_borrowed_chords()
        print("Borrowed chords:", borrowed_chords)
        self.ut_report.assertTrue(borrowed_chords == [])

    def test_degrees_happy_birthday(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_happy_birthday)
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['I', 'V', 'V', 'I', 'I7', 'IV', 'I', 'V', 'I'])

    def test_degrees_evenou(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_evenou)
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['i', 'iv', 'V7', 'iv', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'V7',
                                                        'i', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'V7', 'i', 'V7', 'V7',
                                                        'V7', 'i', 'i', 'iv', 'V7', 'i', 'V7', 'V7', 'V7', 'i', 'i',
                                                        'iv', 'V7', 'i', 'V7', 'V7', 'V7', 'i'])

    def test_degrees_sometimes(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_sometimes)
        the_song.generate_degrees_from_chord_progression()
        self.ut_report.assertTrue(the_song.degrees == ['I', 'VI#', 'vii', 'IV', 'I', 'I', 'VI#', 'vii', 'IV', 'I',
                                                       'VII', 'VII', 'VII', 'I', 'vii', 'IV', 'V', 'I', 'IV', 'I',
                                                       'vii', 'I', 'IV', 'vii', 'V', 'IV', 'IV', 'vii', 'V', 'IV',
                                                       'vii', 'V', 'IV', 'vii', 'V', 'IV'])

    def test_remarquable_cadences_happy_birthday(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_happy_birthday)
        the_song.generate_degrees_from_chord_progression()
        res = the_song.get_remarquable_cadences()
        expected = {'REMARQUABLE_CADENCES_NATURAL_MAJOR:AUTHENTIC CADENCE': [4]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.ut_report.assertTrue(diff == {})

    def test_remarquable_cadences_happy_birthday(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_evenou)
        the_song.generate_degrees_from_chord_progression()
        res = the_song.get_remarquable_cadences()
        expected = {}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.ut_report.assertTrue(diff == {})

    def test_remarquable_cadences_sometimes(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_sometimes)
        the_song.generate_degrees_from_chord_progression()
        res = the_song.get_remarquable_cadences()
        expected = {'REMARQUABLE_CADENCES_NATURAL_MAJOR:AUTHENTIC CADENCE': [11, 26],
                    'REMARQUABLE_CADENCES_NATURAL_MAJOR:PLAGAL CADENCE': [10, 25]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.ut_report.assertTrue(diff == {})

    def test_remarquable_cadences_saravah(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_saravah)
        the_song.generate_degrees_from_chord_progression()
        res = the_song.get_remarquable_cadences()
        expected = {'REMARQUABLE_CADENCES_NATURAL_MAJOR:SAMBA SARAVAH': [0, 13, 26, 36, 46, 67, 77, 87, 97, 118, 128, 138]}
        diff = DeepDiff(res, expected, ignore_order=True)
        self.ut_report.assertTrue(diff == {})

    def test_transpose_happy_birthday(self):
        the_song = TextSongWithLineForChords()
        the_song.digest(self.song_happy_birthday)
        the_song.generate_degrees_from_chord_progression()
        res = the_song.transpose(number_half_tone=-5)
        expected = ['E', 'B', 'B', 'E', 'E7', 'A', 'E', 'B', 'E']
        self.ut_report.assertTrue(res == expected)

        res = the_song.transpose(number_half_tone=0)
        expected = ['A', 'E', 'E', 'A', 'A7', 'D', 'A', 'E', 'A']
        self.ut_report.assertTrue(res == expected)

        res = the_song.transpose(number_half_tone=10)
        expected = ['G', 'D', 'D', 'G', 'G7', 'C', 'G', 'D', 'G']
        self.ut_report.assertTrue(res == expected)

        res = the_song.transpose(number_half_tone=12)
        expected = ['A', 'E', 'E', 'A', 'A7', 'D', 'A', 'E', 'A']
        self.ut_report.assertTrue(res == expected)

        res = the_song.transpose(number_half_tone=12-5)
        expected = ['E', 'B', 'B', 'E', 'E7', 'A', 'E', 'B', 'E']
        self.ut_report.assertTrue(res == expected)
