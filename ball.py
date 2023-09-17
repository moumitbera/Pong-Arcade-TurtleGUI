import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moveX = 10
        self.moveY = 10
        self.animationSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.moveX
        newY = self.ycor() + self.moveY
        self.goto(newX, newY)

    def bounce(self):
        self.moveY *= -1

    def rebounce(self):
        self.moveX *= -1
        self.animationSpeed *= 0.9

    def resetBall(self):
        self.goto(0, 0)
        self.animationSpeed = 0.1
        self.moveX *= -1
