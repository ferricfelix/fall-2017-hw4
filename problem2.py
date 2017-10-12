from abc import ABC, abstractmethod
import tkinter as tk


CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


def draw_pixel(canvas, x, y, color='#000000'):
    """Draw a pixel at (x,y) on the given canvas"""
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color)


def main(shape):
    """Create a main window with a canvas to draw on"""
    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Render the user-defined shape

    # TODO: Insert your code here!

    # Start the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)
    tk.mainloop()


if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    head = Circle(0, 0, 200)
    left_eye = Circle(-70, 100, 20)
    right_eye = Circle(70, 100, 20)
    mouth = Rectangle(-90, -80, 90, -60)
    happy_face = head - left_eye - right_eye - mouth

    # Draw the happy face
    main(happy_face)
