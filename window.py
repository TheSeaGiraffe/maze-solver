from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width: int, height: int):
        self._root: Tk = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas: Canvas = Canvas()
        self._canvas.pack(fill=BOTH, expand=True)

        self._is_running: bool = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self):
        self._is_running = False
