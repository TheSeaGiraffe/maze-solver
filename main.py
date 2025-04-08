from maze import Maze
from window import Window


def main():
    win = Window(800, 800)

    # Init a maze with a seed for testing purposes
    seed = 42
    maze = Maze(50, 50, 10, 10, 20, 20, win, seed)

    win.wait_for_close()


if __name__ == "__main__":
    main()
