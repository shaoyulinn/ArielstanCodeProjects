"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_height-paddle_offset)

        # Center a filled ball in the graphical window
        ball_width = ball_radius*2
        ball_height = ball_radius*2
        self.ball = GOval(width=ball_width, height=ball_height)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_width)/2, y=(window_height-ball_height)/2)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_direction)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.num_bricks = brick_cols * brick_rows
        brick_y = brick_offset
        for i in range(brick_rows):
            brick_x = 0
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if i <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 1 < i <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 3 < i <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 5 < i <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x += (brick_width+brick_spacing)
            brick_y += (brick_height+brick_spacing)

        self.switch = False

    def paddle_move(self, mouse):
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > (self.window.width - self.paddle.width/2):
            self.paddle.x = (self.window.width - self.paddle.width)
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def ball_direction(self, _):
        if not self.switch:
            self.switch = True

        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(1, MAX_X_SPEED)

        if self.__dx == 0:
            self.__dx = random.randrange(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def change_x_direction(self):
        self.__dx = -self.__dx

    def change_y_direction(self):
        self.__dy = -self.__dy

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)
        self.__dy = 0
        self.__dx = 0

    # Getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy












