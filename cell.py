from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, win: Window):
        # Window
        self._win: Window = win

        # Coords
        self._x1: int = 0
        self._y1: int = 0
        self._x2: int = 0
        self._y2: int = 0

        # Wall check
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        # Set coords
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # Create all necessary points
        pt_lower_left = Point(self._x1, self._y1)
        pt_lower_right = Point(self._x2, self._y1)
        pt_upper_left = Point(self._x1, self._y2)
        pt_upper_right = Point(self._x2, self._y2)

        # Draw lines
        # Wonder if I can do all of this in a loop. Will think about it later
        if self.has_left_wall:
            line_left = Line(pt_lower_left, pt_upper_left)
            self._win.draw_line(line_left, "black")
        if self.has_right_wall:
            line_right = Line(pt_lower_right, pt_upper_right)
            self._win.draw_line(line_right, "black")
        if self.has_top_wall:
            line_top = Line(pt_upper_left, pt_upper_right)
            self._win.draw_line(line_top, "black")
        if self.has_bottom_wall:
            line_bottom = Line(pt_lower_left, pt_lower_right)
            self._win.draw_line(line_bottom, "black")

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        # Get center of both cells
        # src cell
        center_x1 = self._x1 + ((self._x2 - self._x1) // 2)
        center_y1 = self._y1 + ((self._y2 - self._y1) // 2)
        src_center = Point(center_x1, center_y1)

        # target cell
        center_x2 = to_cell._x1 + ((to_cell._x2 - to_cell._x1) // 2)
        center_y2 = to_cell._y1 + ((to_cell._y2 - to_cell._y1) // 2)
        target_center = Point(center_x2, center_y2)

        # Draw line
        center_line = Line(src_center, target_center)
        fill_color = "gray" if undo else "red"
        self._win.draw_line(center_line, fill_color)
