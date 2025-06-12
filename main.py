from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

keys = {"Up": False, "Down": False, "w": False, "s": False}

def press(key): keys[key] = True
def release(key): keys[key] = False

for key in keys:
    screen.onkeypress(lambda k=key: press(k), key)
    screen.onkeyrelease(lambda k=key: release(k), key)

def move():
    if keys["Up"]: r_paddle.go_up()
    if keys["Down"]: r_paddle.go_down()
    if keys["w"]: l_paddle.go_up()
    if keys["s"]: l_paddle.go_down()
    screen.ontimer(move, 30)

screen.listen()

move()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.right_score()
        ball.reset_position()
    if ball.xcor() < -380:
        score.left_score()
        ball.reset_position()

screen.exitonclick()
