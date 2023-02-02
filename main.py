from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

# Event listeners
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        r_paddle.increase_speed()
        l_paddle.increase_speed()

    # Detect R paddle misses:
    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()
        l_paddle.reset_speed()
        r_paddle.reset_speed()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        scoreboard.l_point()
        ball.reset_position()
        l_paddle.reset_speed()
        r_paddle.reset_speed()

screen.exitonclick()
