from cell import Cell
from window import Window


def main():
    win = Window(800, 800)

    # Draw squares or cells using the new Cell class
    sq_small = Cell(200, 200, 300, 300, win)
    sq_small.draw()

    sq_long_horz = Cell(300, 500, 500, 300, win)
    # sq_long_horz.has_left_wall = False
    sq_long_horz.has_top_wall = False
    sq_long_horz.has_bottom_wall = False
    sq_long_horz.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
