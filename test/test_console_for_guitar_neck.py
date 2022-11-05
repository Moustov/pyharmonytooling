from unittest import TestCase

from src.output.console_for_guitar_neck import GuitarNeck


class Test(TestCase):
    def test_set_single_finger(self):
        expected_grid = """e |-----+-----+-----+-----+
B |-----+-----+-----+-----+
G |-----+-----+-----+-----+
D |-----+-----+-----+-----+
A |-----+-----+-----+-----+
E |--X--+-----+-----+-----+
"""
        a_grid = GuitarNeck()
        grid = a_grid.blank_grid()
        grid = a_grid.set_finger(grid, "E", 1)
        assert (grid == expected_grid)

        expected_grid = """e |-----+-----+--X--+-----+
B |-----+-----+-----+-----+
G |-----+-----+-----+-----+
D |-----+-----+-----+-----+
A |-----+-----+-----+-----+
E |-----+-----+-----+-----+
"""
        grid = a_grid.blank_grid()
        grid = a_grid.set_finger(grid, "e", 3)
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
        grid = a_grid.blank_grid()
        grid = a_grid.set_finger(grid, "E", 1)
        grid = a_grid.set_finger(grid, "B", 4)
        assert (grid == expected_grid)
