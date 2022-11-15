from src.guitar_neck.fingering import Fingering
from src.guitar_neck.neck import Neck


class GuitarNeck:
    def __init__(self):
        self.GRID_WIDTH = 5
        self.GRID_FRETS = 4
        self.GRID_STRING_LEN = 0
        self.horizontal_grid = self.set_blank_grid()

    def string_name_to_display_position(self, string: str) -> int:
        if string == "E":
            return 5
        if string == "A":
            return 4
        if string == "D":
            return 3
        if string == "G":
            return 2
        if string == "B":
            return 1
        if string == "e":
            return 0

    def set_finger(self, string: str, fret: int, finger: chr = Fingering.TAB_MUTE) -> str:
        """
        returns a guitar grid with finger number
        :param string: E / A / D / G / B / e
        :param fret:
        :param finger: X: mute / 0: open / T: thumb / 1: index / 2: major / 3:ring finger / 4: pinky
        :return:
        """
        string_pos = self.string_name_to_display_position(string)
        if fret == 0:
            vertical_index = string_pos * self.GRID_STRING_LEN
            self.horizontal_grid = self.horizontal_grid[0:vertical_index+1] + "0" + self.horizontal_grid[vertical_index+2:]
        elif 0 < fret <= self.GRID_FRETS:
            vertical_index = string_pos * self.GRID_STRING_LEN + fret * (self.GRID_WIDTH+1)
            self.horizontal_grid = self.horizontal_grid[0:vertical_index-1] + finger + self.horizontal_grid[vertical_index:]
        else:
            fret = fret - self.GRID_WIDTH - 1
            self.horizontal_grid = self.remove_nut()
            vertical_index = string_pos * self.GRID_STRING_LEN + fret * (self.GRID_WIDTH+1)
            self.horizontal_grid = self.horizontal_grid[0:vertical_index-1] + finger + self.horizontal_grid[vertical_index:]
        return self.horizontal_grid

    def set_blank_grid(self) -> str:
        """
        :return:
        e |-----+-----+-----+-----+
        B |-----+-----+-----+-----+
        G |-----+-----+-----+-----+
        D |-----+-----+-----+-----+
        A |-----+-----+-----+-----+
        E |-----+-----+-----+-----+
        """
        neck = Neck()
        fret = "-" * self.GRID_WIDTH
        fret = fret + "+"
        string = fret * self.GRID_FRETS
        self.horizontal_grid = neck.TUNING[5] + " |" + string + "\n"
        self.GRID_STRING_LEN = len(self.horizontal_grid)
        self.horizontal_grid += neck.TUNING[4] + " |" + string + "\n"
        self.horizontal_grid += neck.TUNING[3] + " |" + string + "\n"
        self.horizontal_grid += neck.TUNING[2] + " |" + string + "\n"
        self.horizontal_grid += neck.TUNING[1] + " |" + string + "\n"
        self.horizontal_grid += neck.TUNING[0] + " |" + string + "\n"
        return self.horizontal_grid

    def draw_fingering(self, fingering: [int], display_full_neck: bool = False) -> str:
        """
        return something like
       e |-----+--1--+-----+-----+--
       B |-----+-----+--3--+-----+--
       G |-----+-----+--3--+-----+--
       D |-----+-----+--3--+-----+--
       A |-----+--1--+-----+-----+--
       E |-----+--1--+-----+-----+--
        :param fingering:
        :param display_full_neck:
        :return:
        """
        self.horizontal_grid = self.set_blank_grid()
        self.set_finger("E", fingering[0])
        self.set_finger("A", fingering[1])
        self.set_finger("D", fingering[2])
        self.set_finger("G", fingering[3])
        self.set_finger("B", fingering[4])
        self.set_finger("e", fingering[5])
        if display_full_neck:
            return self.horizontal_grid
        else:
            return self.get_useful_neck_part()

    def remove_nut(self) -> str:
        """
        can be used to show the useful part of the neck
        :return:
        """
        return self.horizontal_grid.replace("|", "+")

    def get_useful_neck_part(self) -> str:
        """
        returns a string limited to the useful part of the neck with the fret number at the top
        :return:
        """
        return self.horizontal_grid
