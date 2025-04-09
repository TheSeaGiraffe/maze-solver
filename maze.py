import random
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
        win: Window | None = None,
        seed: int | None = None,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window | None = win
        self._cells: list[list[Cell]] = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
                self._break_entrance_and_exit(row, col)
                self._draw_cell(row, col)

    def _break_entrance_and_exit(self, i: int, j: int):
        if (i == 0) and (j == 0):
            self._cells[i][j].has_top_wall = False
        elif (i == (self._num_rows - 1)) and (j == (self._num_cols - 1)):
            self._cells[i][j].has_bottom_wall = False

    def _draw_cell(self, i: int, j: int):
        # Remember, (x1, y1) is lower left corner and (x2, y2) is upper right
        cell_x2 = self._x1 + ((j + 1) * self._cell_size_x)
        cell_y2 = self._y1 + ((i + 1) * self._cell_size_y)
        cell_x1 = cell_x2 - self._cell_size_x
        cell_y1 = cell_y2 - self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j].visited = True
        while True:
            # Create empty list to keep track of all the coords that we'll need to visit
            cell_coords_to_visit: list[tuple[str, int, int]] = []

            # Check adjacent cells
            adj_coords = [
                ("right", i, j + 1),
                ("bottom", i + 1, j),
                ("left", i, j - 1),
                ("top", i - 1, j),
            ]

            for direction, i_adj, j_adj in adj_coords:
                if (
                    i_adj < 0
                    or j_adj < 0
                    or i_adj > (self._num_rows - 1)
                    or j_adj > (self._num_cols - 1)
                ):
                    continue
                if not self._cells[i_adj][j_adj].visited:
                    cell_coords_to_visit.append((direction, i_adj, j_adj))

            # If all adjacent cells have been visited draw current cell then exit while
            # loop
            if len(cell_coords_to_visit) == 0:
                self._draw_cell(i, j)
                return

            # Pick random direction
            next_cell_direction, next_cell_i, next_cell_j = random.choice(
                cell_coords_to_visit
            )

            # Remove wall between current cell and chosen cell
            match next_cell_direction:
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_cell_i][next_cell_j].has_left_wall = False
                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_cell_i][next_cell_j].has_top_wall = False
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_cell_i][next_cell_j].has_right_wall = False
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_cell_i][next_cell_j].has_bottom_wall = False
                case _:
                    pass

            # Move to cell by calling _break_walls_r
            self._break_walls_r(next_cell_i, next_cell_j)

    def _reset_cells_visited(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._cells[row][col].visited = False

    def _solve_r(self, i: int, j: int) -> bool:
        # Call the animate method
        self._animate()

        # Mark current cell as visited
        self._cells[i][j].visited = True

        # If we're at the end cell then return True
        if i == (self._num_rows - 1) and j == (self._num_cols - 1):
            return True

        # Check each direction and move towards the cell with no wall
        # Check adjacent cells
        adj_coords = [
            ("right", i, j + 1),
            ("bottom", i + 1, j),
            ("left", i, j - 1),
            ("top", i - 1, j),
        ]

        for direction, i_adj, j_adj in adj_coords:
            if (
                i_adj < 0
                or j_adj < 0
                or i_adj > (self._num_rows - 1)
                or j_adj > (self._num_cols - 1)
            ):
                continue

            if self._cells[i_adj][j_adj].visited:
                continue

            move = False
            match direction:
                case "right":
                    if (
                        not self._cells[i][j].has_right_wall
                        and not self._cells[i_adj][j_adj].has_left_wall
                    ):
                        move = True
                case "bottom":
                    if (
                        not self._cells[i][j].has_bottom_wall
                        and not self._cells[i_adj][j_adj].has_top_wall
                    ):
                        move = True
                case "left":
                    if (
                        not self._cells[i][j].has_left_wall
                        and not self._cells[i_adj][j_adj].has_right_wall
                    ):
                        move = True
                case "top":
                    if (
                        not self._cells[i][j].has_top_wall
                        and not self._cells[i_adj][j_adj].has_bottom_wall
                    ):
                        move = True
                case _:
                    pass

            if move:
                self._cells[i][j].draw_move(self._cells[i_adj][j_adj])
                if self._solve_r(i_adj, j_adj):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i_adj][j_adj], True)

        # If none of the directions worked out return False
        return False

    def solve(self) -> bool:
        return self._solve_r(0, 0)
