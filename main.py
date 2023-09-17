import turtle as t
import paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = t.Screen()
scoreboard = ScoreBoard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# creating right paddle
r_paddle = paddle.Paddle()
r_paddle.setPosition(x=370, y=0)

# move the right paddle
screen.onkeypress(r_paddle.goUp, "Up")
screen.onkeypress(r_paddle.goDown, "Down")


# create first paddle
l_paddle = paddle.Paddle()
l_paddle.setPosition(x=-370, y=0)

# move the second paddle
screen.onkeypress(l_paddle.goUp, "w")
screen.onkeypress(l_paddle.goDown, "s")

# creating the ball
ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.animationSpeed)
    screen.update()
    ball.move()

    # detecting collision w/ top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision w/paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -340
    ):
        ball.rebounce()

    # detect when right paddle misses
    if ball.xcor() > 390:
        ball.resetBall()
        scoreboard.score_for_left()

    # detect when the left paddle misses
    if ball.xcor() < -390:
        ball.resetBall()
        scoreboard.score_for_right()


screen.exitonclick()
