from unittest import TestCase

from deepdiff import DeepDiff
from pychord import Chord

from pyharmonytools.displays.unit_test_report import UnitTestReport
from pyharmonytools.guitar_tab.guitar_tab import GuitarTab
from pyharmonytools.harmony.cof_chord import CofChord
from pyharmonytools.harmony.note import Note


def are_same_digested_tabs(res: dict, expected: dict):
    """
    ensure carets & chords match are the same
    => compares both tab decorations (eg. { "2": xxx, "17": xxxx, ...})
        and ensure each chords match (at component level)
    :param res:
    :param expected:
    :return:
    """
    for chord_res in res.keys():
        if chord_res not in expected.keys():
            return False
        if not CofChord.are_chord_equals(expected[chord_res], res[chord_res]):
            return False
    for chord_expected in expected.keys():
        if chord_expected not in res.keys():
            return False
        if not CofChord.are_chord_equals(expected[chord_expected], res[chord_expected]):
            return False
    return True


def transform_expected_chords(expected_chords: object) -> object:
    """
    todo
    :param expected_chords:
    :return:
    """
    return None


class TestGuitarTab(TestCase):
    ut_report = UnitTestReport()

    def test_get_notes_from_chord_layout(self):
        chord_layout = [-1, -1, -1, 11, 11, 11]
        res = GuitarTab._get_notes_from_chord_layout(chord_layout)
        expected = [None, None, None, Note("Gb"), Note("Bb"), Note("Eb")]
        self.ut_report.assertTrue(res == expected)

    def test_digest_tab_dgbd(self):
        """ test_digest_tab_readme"""
        tab = """
        e|--11-----11-----10-----11----|
        B|--11-----12-----11-----11----|
        G|--11-----13-----10-----11----|
        D|-----------------------------|
        A|-----------------------------|
        E|-----------------------------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {"2": Chord("Gb6"), "9": Chord("B6"), "16": Chord("Bb"), "23": Chord("Gb6")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_tab_gb6(self):
        tab = """
        e|--11---------------|
        B|------11-----------|
        G|-----------11------|
        D|-------------------|
        A|-------------------|
        E|-------------------|
        """
        expected = {"2": Chord("Bbsus/Gb")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(expected, res))

    def test_digest_tab_gb6_d(self):
        tab = """
        e|--11------------2---|
        B|------11--------3---|
        G|-----------11---2---|
        D|--------------------|
        A|--------------------|
        E|--------------------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {"2": Chord("Ebm"), "16": Chord("D")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_tab_eb(self):
        tab = """
        e|--11---|
        B|-------|
        G|-------|
        D|-------|
        A|-------|
        E|-------|
        """
        expected = {"2": Chord("Eb")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_tab_full_bach(self):
        # todo work on expected chord + digesting full tab
        #  (multiple bars & lines with tab signs such as hammering/pull off/...)
        # see https://tabs.ultimate-guitar.com/tab/johann-sebastian-bach/cello-suite-no-1-prelude-tabs-799617
        tab_full = """
            Cello Suite No. 1 - Prelude
            Johann Sebastian Bach
            4/4
            Key: G Major
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----0---0---0-------0---0---0---|-----1-0-1---1-------1-0-1---1---|
            G|-------2---------------2---------|---------------------------------|
            D|---0-------0---0---0-------0---0-|---2-------2---2---2-------2---2-|
            A|---------------------------------|---------------------------------|
            E|-3---------------3---------------|-3---------------3---------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|-----0---0---0-------0---0---0---|
            G|-----5-4-5---5-------5-4-5---5---|---0---2---0---0---0---2---0-----|
            D|---4-------4---4---4-------4---4-|-------------------------------4-|
            A|---------------------------------|---------------------------------|
            E|-3---------------3---------------|-3---------------3---------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----0---0-----------------------|---------------------------------|
            G|-------2---0---0---0---0---------|---0-2-0-2-0-2-0---0-2-0-2-0-2-0-|
            D|---2---------4---2---4-----0-----|---------------------------------|
            A|-------------------------2---4-2-|-4---------------4---------------|
            E|-3-------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----3-2-3-----------------------|---------------------------------|
            G|---2-------2-0-2---2-0-2---------|-----0---0---0-------0---0---0---|
            D|-4---------------4-------0-4-2-0-|-------4---------------4---------|
            A|---------------------------------|---2-------2---2---2-------2---2-|
            E|---------------------------------|-0---------------0---------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----------------------3-2-0-----|-------3---3---------------------|
            G|-----------------0-----------2-0-|---------2-----2-------2-0-------|
            D|-----0-2-0---------4-2-----------|-4-2-0-------4---0-2-4-----4-2-0-|
            A|---4-------4-2-0-----------------|---------------------------------|
            E|-0-------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|-------0-1-------------0-1-------|
            G|-1-----------1---4-----------1---|-----2-----2---------2-----2-----|
            D|---0-3-2-3-0---0---0-3-2-3-0---0-|---2---------2-0---2---------4-2-|
            A|---------------------------------|-3---------------3---------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|---------------------------------|
            G|---------------------------------|-0-----0---0-2---0---------------|
            D|---4---4-7-4-7-4---4---4-7-4-7-4-|---4-2---4-----4---4-2-0---------|
            A|-6---6-----------6---6-----------|-------------------------3-2-0---|
            E|---------------------------------|-------------------------------3-|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|---------------------------------|
            G|---------------------------------|---------------------------------|
            D|-----0---0---0-------0---0---0---|-----3-2-3---3-------3-2-3---3---|
            A|---3---3---3---3---3---3---3---3-|---2-------2---2---2-------2---2-|
            E|-2---------------2---------------|-3---------------3---------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|-------0---------------0---------|
            G|---------------------------------|-----5---5---5-------5---5---5---|
            D|-----2-0-2---2-------2-0-2---2---|---4-------4---4---4-------4---4-|
            A|---3-------3---3---3-------3---3-|---------------------------------|
            E|-3---------------3---------------|-3---------------3---------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----0---0-----------------------|---------------------------------|
            G|-------2---0---------------------|---------0-----0---------0-----0-|
            D|---0---------4-2-0-------------0-|-----2-4---2-4-------2-4---2-4---|
            A|-------------------3-2-0---------|-4-0-------------3-0-------------|
            E|-3-----------------------3-2-0---|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|-----------2-3-------------------|
            G|---------------------------------|---------2---------------------0-|
            D|-----0-2-4-0-2-4-----0-2-4-0-2-4-|-----0-4-----------------0-2-4---|
            A|-3-0-------------3-0-------------|-3-0---------------0-2-3---------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------0-1---------0-1-3-|-4-3-2-3-3-1-0-1-1---------------|
            G|-2---------0-2-----2---0-2-------|-------------------2-------------|
            D|---4-0-2-4-----------4-----------|---------------------4-2-0-------|
            A|---------------------------------|---------------------------0-2-3-|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----------0-1---0---------------|-------------0---2---------------|
            G|---------2-----2---0-------------|---------0-2---0---3-2-3-3-2-1-2-|
            D|-0---0-4-------------0-----------|-0-----0-------------------------|
            A|---0-------------------3-2---0-2-|-----2---------------------------|
            E|---------------------------3-----|---3-----------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------2-3-2-|-3-------------------------------|
            G|-2-0---0-0-------------0-2-------|---2-------2---------------------|
            D|-----4-----2---------2-----------|-----4-2-4---0-4---0-------------|
            A|-------------4-2-0-4-------------|-----------------0---4-2-0-------|
            E|---------------------------------|---------------------------3-2-0-|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-----1-0-----------1-0-----------|---0-----------------------------|
            G|---------2-0-----------2-0-------|-----2-0-----------2-0-----------|
            D|-0-----------4-2-0---------4-2-0-|---------4-2-0---------4-2-0-----|
            A|---------------------------------|-3-------------3-2-----------3-2-|
            E|---------------------------------|---------------------------------|
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|---------------------------------|---------------------------------|
            G|---0-------2---2---2---2-0-2---2-|---2---2-0-2---2---2---2-0-2---2-|
            D|-----4-2-4---0---2---4-------2---|-4---0-------2---4---0-------2---|
            A|-0-------------------------------|---------------------------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-------------------------0-------|-----0---1-------0---1---3---0---|
            G|---2---2---2---2-0-2-2-2---2---2-|-2-2---2---2---2---2---2---2---2-|
            D|-4---0---2---4---------------0---|-------------0-------------------|
            A|---------------------------------|---------------------------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------------------|
            B|-1---0---1-------0-------0-------|---------------------------------|
            G|---2---2---2-2-2---2-2-2---2-0-2-|-2-2-0-2-2-2---2-0-2---2-0-2---2-|
            D|---------------------------------|-------------4-------4-------2---|
            A|---------------------------------|---------------------------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|---------------------------------|---------------------0---1---2---|
            B|---------------------------------|-0---1---2---3---4---------------|
            G|---2-------------0---1---2---3---|---------------------------------|
            D|-4---0-2-3-0-4-0---0---0---0---0-|---0---0---0---0---0---0---0---0-|
            A|---------------------------------|---------------------------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|-3-------3---3---3-------3---3---|-3-------3---3---3-------3---3---|
            B|---0---0---0---0---0---0---0---0-|---------------------------------|
            G|---------------------------------|---2---2---2---2---2---2---2---2-|
            D|-----0---------------0-----------|-----0---------------0-----------|
            A|---------------------------------|---------------------------------|
            E|---------------------------------|---------------------------------|
             
             
               |       |       |       |         |       |       |       |
            e|-2-------2---2---2-------2---2---|-3-------------------------------|
            B|---1---1---1---1---1---1---1---1-|-0-------------------------------|
            G|---------------------------------|---------------------------------|
            D|-----0---------------0-----------|---------------------------------|
            A|---------------------------------|---------------------------------|
            E|---------------------------------|-3-------------------------------|        
        """
        # not yet reliable
        expected_chords = """
        C     C     Dm  Dm7 G7  G7  C   C
        C7    C7    D7  D7  G   G   C   C
        Am    Am    D7  D7  G   G   Gdim  Edim
        Dm    Dm    Ddim  Fdim  C   C   F   F
        Dm    Dm7   G7  G7  C   C   C7  Fmaj7
        Fmaj7 Fmaj7 F#dim F#dim C#dim Fdim  G7  G7
        C     C     G7  G7  G7  G7  Cm  C
        C     C     G   G   G7  G7  C7  C7
        C     F     C   C   C   C
        """
        chords = expected_chords.split()
        chords_list = []
        for c in chords:
            transposed_chord = Chord(c)
            transposed_chord.transpose(7)
            chords_list.append(transposed_chord)
        expected = transform_expected_chords(expected_chords)
        gt = GuitarTab(tab_full)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_bach_bar_1(self):
        tab = """
  e|---------------------------------|
  B|-----0---0---0-------0---0---0---|
  G|-------2---------------2---------|
  D|---0-------0---0---0-------0---0-|
  A|---------------------------------|
  E|-3---------------3---------------|
  """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'1': Chord("Gadd9")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_tab_simplest_progressive_chords_in_a_bar_ebm(self):
        tab = """
        e|--11---------------|
        B|------11-----------|
        G|-----------11------|
        D|-------------------|
        A|-------------------|
        E|-------------------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {"2": Chord("Ebm")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_bach_bar_1_2(self):
        tab = """
            e|-------------------------------------------------------------------|
            B|-----0---0---0-------0---0---0---------1-0-1---1-------1-0-1---1---|
            G|-------2---------------2-------------------------------------------|
            D|---0-------0---0---0-------0---0-----2-------2---2---2-------2---2-|
            A|-------------------------------------------------------------------|
            E|-3---------------3-----------------3---------------3---------------|
"""
        #      1                                 35    4143            5759
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {'1': Chord('Gadd9'), '35': Chord('C/G'), '41': Chord('B'),
                    '43': Chord('C/G'), '57': Chord('B'), '59': Chord('C/E')}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))

    def test_digest_tab_simplest_progressive_chords_in_a_bar_gb6_d(self):
        tab = """
        e|--11------------2---|
        B|------11--------3---|
        G|-----------11---2---|
        D|--------------------|
        A|--------------------|
        E|--------------------|
        """
        # checked with https://www.oolimo.com/guitarchords/analyze
        expected = {"2": Chord("Gb6"), "16": Chord("D")}
        gt = GuitarTab(tab)
        res = gt.digest_tab_simplest_progressive_chords_in_a_bar()
        self.ut_report.assertTrue(are_same_digested_tabs(res, expected))
