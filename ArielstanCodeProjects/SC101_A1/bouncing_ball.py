"""
File: 
Name: Ariel Shao
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count = 3

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(_):
    global count
    vy = GRAVITY
    if count > 0:
        while ball.x <= window.width:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y >= window.height:
                vy = -vy
                vy *= REDUCE
                while vy > 0:
                    vy -= GRAVITY
            pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)
    count -= 1


if __name__ == "__main__":
    main()
