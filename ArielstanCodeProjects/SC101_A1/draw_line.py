"""
File: 
Name: Ariel Shao
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
count = 0
circle_x = 0
circle_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global count, circle_x, circle_y
    count += 1
    if count % 2 == 1:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(circle)
        circle_x = circle.x
        circle_y = circle.y
    else:
        line = GLine(x0=circle_x + SIZE / 2, y0=circle_y + SIZE / 2,  x1=mouse.x - SIZE / 2, y1=mouse.y - SIZE / 2)
        circle = window.get_object_at(circle_x + SIZE / 2, circle_y + SIZE / 2)
        window.remove(circle)
        window.add(line)


if __name__ == "__main__":
    main()
