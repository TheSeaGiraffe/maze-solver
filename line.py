from tkinter import Canvas

from point import Point


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: Canvas, fill_color: str):
        _ = canvas.create_line(
            (self.p1.x, self.p1.y),
            (self.p2.x, self.p2.y),
            fill=fill_color,
            width=2,
        )
