from maze import Maze
from window import Window


def main():
    win = Window(800, 800)

    # Init and solve a maze
    maze = Maze(100, 100, 12, 12, 50, 50, win)

    if maze.solve():
        print("Solution found")
    else:
        print("No solution")

    win.wait_for_close()


if __name__ == "__main__":
    main()
