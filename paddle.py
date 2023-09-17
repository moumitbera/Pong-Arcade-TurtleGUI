import turtle as t


class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.speed("fastest")

    def goUp(self):
        self.fd(20)

    def goDown(self):
        self.back(20)

    def setPosition(self, x, y):
        self.goto(x, y)
