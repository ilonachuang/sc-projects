"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This code represents the coder side of a brick game,
including the constructor and mouse events.

Name: Ilona
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# constants
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
FRAME_RATE = 1000 / 120 # 120 frames per second


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.paddle_offset = self.window.height-paddle_offset-paddle_height
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window.width-paddle_width)/2, y=self.paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.init_x = (self.window.width-self.ball.width)/2
        self.init_y = (self.window.height-self.ball.height)/2
        self.window.add(self.ball, x=self.init_x, y=self.init_y)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.set_switch)
        self.switch = False     # Game starts when self.switch is True

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset
        color_group = brick_rows // 5   # divide rows to five even groups to color
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j in range(0, color_group):
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif j in range(color_group, 2*color_group):
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif j in range(2*color_group, 3*color_group):
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif j in range(3*color_group, 4*color_group):
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick,
                                x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))

    def paddle_move(self, event):
        if event.x + self.paddle_width >= self.window.width:    # out of window
            self.window.add(self.paddle, x=self.window.width-self.paddle_width, y=self.paddle_offset)
        elif event.x <= 0:      # out of window
            self.window.add(self.paddle, x=0, y=self.paddle_offset)
        else:       # in the window, follows mouse
            self.window.add(self.paddle, x=event.x, y=self.paddle_offset)

    def set_switch(self, mouse):
        self.switch = True      # turn on switch

    # Getters
    def get_switch(self):
        return self.switch

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

