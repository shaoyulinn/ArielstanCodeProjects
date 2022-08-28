"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# constant
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!

    while True:
        if graphics.num_bricks > 0:
            if lives > 0:
                # Update
                vx = graphics.get_dx()
                vy = graphics.get_dy()
                graphics.ball.move(vx, vy)
                # Check
                if graphics.ball.x <= 0 or (graphics.ball.x+graphics.ball.width) > graphics.window.width:
                    graphics.change_x_direction()
                if graphics.ball.y <= 0:
                    graphics.change_y_direction()
                if graphics.ball.y > graphics.window.height:
                    lives -= 1
                    graphics.reset_ball()

                maybe_object1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                maybe_object2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                maybe_object3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                maybe_object4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)

                if maybe_object1 is not None:
                    if maybe_object1 == graphics.paddle:
                        graphics.change_y_direction()
                    else:
                        graphics.change_y_direction()
                        graphics.window.remove(maybe_object1)
                        graphics.num_bricks -= 1

                elif maybe_object2 is not None:
                    if maybe_object2 == graphics.paddle:
                        graphics.change_y_direction()
                    else:
                        graphics.change_y_direction()
                        graphics.window.remove(maybe_object2)
                        graphics.num_bricks -= 1

                elif maybe_object3 is not None:
                    if maybe_object3 == graphics.paddle:
                        graphics.change_y_direction()
                    else:
                        graphics.change_y_direction()
                        graphics.window.remove(maybe_object3)
                        graphics.num_bricks -= 1

                elif maybe_object4 is not None:
                    if maybe_object4 == graphics.paddle:
                        graphics.change_y_direction()
                    else:
                        graphics.change_y_direction()
                        graphics.window.remove(maybe_object4)
                        graphics.num_bricks -= 1

                else:
                    pass

                # Pause
                pause(FRAME_RATE)
            else:
                break
        else:
            break
    graphics.reset_ball()


if __name__ == '__main__':
    main()
