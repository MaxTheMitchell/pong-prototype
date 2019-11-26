from paddle import Paddle
from ball import Ball
from score import Score
from translationToGame import GameDisplay
import time

def make_new_display(width,height):
    return [False]*height*width

def ball_hit_paddle(paddle,ball):
    return (ball.right() == paddle.left() or ball.left() == paddle.right())and \
        ((ball.top() >= paddle.top() and ball.top() <= paddle.bottom()) or
        ((ball.bottom() >= paddle.top() and ball.bottom() <= paddle.bottom())))

def set_pygame_keys(game_disp,paddle_l,paddle_r):
    game_disp.add_key('w',paddle_l.move_set_up,paddle_l.move_set_still)
    game_disp.add_key('s',paddle_l.move_set_down,paddle_l.move_set_still)
    game_disp.add_key('UP',paddle_r.move_set_up,paddle_r.move_set_still)
    game_disp.add_key('DOWN',paddle_r.move_set_down,paddle_r.move_set_still)
    return game_disp

# 
# main
# 
WIDTH = 128
HEIGHT = 64

score = Score(WIDTH,HEIGHT)
ball = Ball(WIDTH,HEIGHT,score)
paddle_r = Paddle(WIDTH,HEIGHT)
paddle_l = Paddle(WIDTH,HEIGHT,True)
game_disp = set_pygame_keys(GameDisplay(WIDTH,HEIGHT),paddle_l,paddle_r)

# 
# main loop
# 
while 1:
    time.sleep(.05)
    if ball_hit_paddle(paddle_l,ball) or ball_hit_paddle(paddle_r,ball):
        ball.x_bounce()
    ball.move()
    paddle_l.move()
    paddle_r.move()
    game_disp.check_keys()
    game_disp.translate_to_pygame(score.display(ball.display(
        paddle_l.display(paddle_r.display(make_new_display(WIDTH,HEIGHT))))))

    