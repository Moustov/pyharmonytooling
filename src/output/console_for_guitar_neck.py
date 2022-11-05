from src.guitar_neck.neck import TUNNING


class GuitarNeck:
    def __init__(self):
        self.GRID_WIDTH = 5
        self.GRID_FRETS = 4
        self.GRID_STRING_LEN = 0

    def string_name_to_position(self, string: str) -> int:
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

    def set_finger(self, horizontal_grid: str, string: str, fret: int) -> str:
        string_pos = self.string_name_to_position(string)
        if fret == 0:
            pass    # todo
        elif 0 < fret < self.GRID_FRETS:
            index = string_pos * self.GRID_STRING_LEN + fret * (self.GRID_WIDTH+1)
            horizontal_grid = horizontal_grid[0:index-1] + "X" + horizontal_grid[index:]
        else:
            pass # todo
        return horizontal_grid

    def blank_grid(self) -> str:
        """
        e |-----+-----+-----+-----+
        B |-----+-----+-----+-----+
        G |-----+-----+-----+-----+
        D |-----+-----+-----+-----+
        A |-----+-----+-----+-----+
        E |-----+-----+-----+-----+

        :param frets:
        :param width:
        :return:
        """
        fret = "-" * self.GRID_WIDTH
        fret = fret + "+"
        string = fret * self.GRID_FRETS
        horizontal_grid = "e |" + string + "\n"
        self.GRID_STRING_LEN = len(horizontal_grid)
        horizontal_grid += "B |" + string + "\n"
        horizontal_grid += "G |" + string + "\n"
        horizontal_grid += "D |" + string + "\n"
        horizontal_grid += "A |" + string + "\n"
        horizontal_grid += "E |" + string + "\n"
        return horizontal_grid

    def draw_fingering(self, fingering: [int]):
        horizontal_grid = """
       e |-----+--X--+-----+-----+--
       B |-----+-----+--X--+-----+--
       G |-----+-----+---X-+-----+--
       D |-----+-----+---X-+-----+--
       A |-----+--X--+-----+-----+--
       E |-----+--X--+-----+-----+--
        """
        horizontal_grid = self.set_finger(self.blank_grid(), "E", fingering[0])
        horizontal_grid = self.set_finger(horizontal_grid, "A", fingering[1])
        horizontal_grid = self.set_finger(horizontal_grid, "D", fingering[2])
        horizontal_grid = self.set_finger(horizontal_grid, "G", fingering[3])
        horizontal_grid = self.set_finger(horizontal_grid, "B", fingering[4])
        horizontal_grid = self.set_finger(horizontal_grid, "e", fingering[5])
