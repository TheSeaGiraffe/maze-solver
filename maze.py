import time

from cell import Cell
from window import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window = win
        self._cells: list[list[Cell]] = []

        self._create_cells()

    def _create_cells(self):
        # Populate _cells list
        for _ in range(self._num_rows):
            cell_row: list[Cell] = []
            for _ in range(self._num_cols):
                cell_row.append(Cell(self._win))
            self._cells.append(cell_row)

        # Draw each cell
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, i: int, j: int):
        # Remember, (x1, y1) is lower left corner and (x2, y2) is upper right
        cell_x2 = self._x1 + ((j + 1) * self._cell_size_x)
        cell_y2 = self._y1 + ((i + 1) * self._cell_size_y)
        cell_x1 = cell_x2 - self._cell_size_x
        cell_y1 = cell_y2 - self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
