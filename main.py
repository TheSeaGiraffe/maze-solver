from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 800)

    # Set some points
    pt1 = Point(200, 200)
    pt2 = Point(200, 600)
    pt3 = Point(600, 200)
    pt4 = Point(600, 600)

    # Create some lines
    l1 = Line(pt1, pt2)
    l2 = Line(pt2, pt4)
    l3 = Line(pt4, pt3)
    l4 = Line(pt1, pt3)
    win.draw_line(l1, "red")
    win.draw_line(l2, "red")
    win.draw_line(l3, "red")
    win.draw_line(l4, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
