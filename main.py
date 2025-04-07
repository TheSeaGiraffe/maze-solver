from maze import Maze
from window import Window


def main():
    win = Window(800, 800)

    # Init a maze
    maze = Maze(100, 100, 15, 15, 20, 20, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
