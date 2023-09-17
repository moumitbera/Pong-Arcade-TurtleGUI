import turtle as t

FONT = ("Courier", "44", "normal")


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.r_score = 0
        self.l_score = 0
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def score_for_left(self):
        self.l_score += 1
        self.writeScore()

    def score_for_right(self):
        self.r_score += 1
        self.writeScore()
