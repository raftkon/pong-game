from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates: tuple) -> None:
        super().__init__('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(coordinates)
        self.move_speed = 20

    def up(self):
        new_y = self.ycor()+self.move_speed
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor()-self.move_speed
        self.goto(x=self.xcor(), y=new_y)

    def increase_speed(self):
        self.move_speed *= 1.1

    def reset_speed(self):
        self.move_speed = 20
