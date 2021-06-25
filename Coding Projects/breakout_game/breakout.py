"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program presents a breakout game with 'NUM_LIVES' lives.
The game starts either if the player is out of lives or if the player removes all bricks.

Name: Ilona
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# constants
FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			    # Number of attempts

# global variables
lives = NUM_LIVES
bricks = 0


def main():
    global lives, bricks
    graphics = BreakoutGraphics()      # constructor
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while lives > 0:
        if graphics.get_switch():      # switch is on
            graphics.ball.move(dx, dy)
            if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
                dx *= -1
            if graphics.ball.y <= 0 or check_collision(graphics):
                dy *= -1
            if bricks == graphics.brick_rows * graphics.brick_cols:     # eliminated all bricks
                graphics.window.add(graphics.ball, x=graphics.init_x, y=graphics.init_y)
                graphics.switch = False     # close switch
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.window.add(graphics.ball, x=graphics.init_x, y=graphics.init_y)
                graphics.switch = False     # close switch
        pause(FRAME_RATE)


def check_collision(graphics):
    """
    this function checks if the ball has touched any objects
    :return: bool, if the ball has collided
    """
    global bricks
    for i in range(0, 2*graphics.ball.width, graphics.ball.width):
        for j in range(0, 2*graphics.ball.width, graphics.ball.width):
            # get_object_at (x, y), (x+ball_width, y), (x, y+ball_height), (x+ball_width, y+ball_height)
            maybe_object = graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j)
            if maybe_object is not None and maybe_object is not graphics.paddle:  # bricks
                graphics.window.remove(maybe_object)
                bricks += 1
                return True
            if maybe_object is graphics.paddle:
                graphics.window.add(graphics.ball, graphics.ball.x, graphics.ball.y-10)  # avoid numerous bounces
                return True


if __name__ == '__main__':
    main()
