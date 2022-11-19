from unittest import TestCase

from src.displays.console_for_guitar_neck import GuitarNeck


class Test(TestCase):
    def test_set_single_finger_E(self):
        expected_grid = """e |-----+-----+-----+-----+
B |-----+-----+-----+-----+
G |-----+-----+-----+-----+
D |-----+-----+-----+-----+
A |-----+-----+-----+-----+
E |--X--+-----+-----+-----+
"""
        a_grid = GuitarNeck()
        grid = a_grid.set_finger("E", 1)
        assert (grid == expected_grid)

    def test_set_single_finger_e(self):
        expected_grid = """e |-----+-----+--X--+-----+
B |-----+-----+-----+-----+
G |-----+-----+-----+-----+
D |-----+-----+-----+-----+
A |-----+-----+-----+-----+
E |-----+-----+-----+-----+
"""
        a_grid = GuitarNeck()
        grid = a_grid.set_finger("e", 3)
        assert (grid == expected_grid)

    def test_set_multiple_fingers(self):
        expected_grid = """e |-----+-----+-----+-----+
B |-----+-----+-----+--X--+
G |-----+-----+-----+-----+
D |-----+-----+-----+-----+
A |-----+-----+-----+-----+
E |--X--+-----+-----+-----+
"""
        a_grid = GuitarNeck()
        a_grid.set_finger("E", 1)
        grid = a_grid.set_finger("B", 4)
        assert (grid == expected_grid)
