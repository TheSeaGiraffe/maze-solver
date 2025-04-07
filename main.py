from cell import Cell
from window import Window


def main():
    win = Window(800, 800)

    # Draw squares or cells using the new Cell class
    src_cell = Cell(200, 300, 300, 400, win)
    src_cell.draw()
    target_cell = Cell(500, 300, 600, 400, win)
    target_cell.draw()

    # Draw line between center of src and target cells
    src_cell.draw_move(target_cell)

    win.wait_for_close()


if __name__ == "__main__":
    main()
