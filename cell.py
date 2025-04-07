from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window):
        # Window
        self._win: Window = win

        # Coords
        self._x1: int = x1
        self._y1: int = y1
        self._x2: int = x2
        self._y2: int = y2

        # Wall check
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True

    def draw(self):
        # Create all necessary points
        pt_lower_left = Point(self._x1, self._y1)
        pt_lower_right = Point(self._x2, self._y1)
        pt_upper_left = Point(self._x1, self._y2)
        pt_upper_right = Point(self._x2, self._y2)

        # Draw lines
        # Wonder if I can do all of this in a loop. Will think about it later
        if self.has_left_wall:
            line_left = Line(pt_lower_left, pt_upper_left)
            self._win.draw_line(line_left, "red")
        if self.has_right_wall:
            line_right = Line(pt_lower_right, pt_upper_right)
            self._win.draw_line(line_right, "red")
        if self.has_top_wall:
            line_top = Line(pt_upper_left, pt_upper_right)
            self._win.draw_line(line_top, "red")
        if self.has_bottom_wall:
            line_bottom = Line(pt_lower_left, pt_lower_right)
            self._win.draw_line(line_bottom, "red")
