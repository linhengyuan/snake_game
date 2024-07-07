from turtle import Turtle, Screen

ALIGN = "Center"
FONT = ('Arial', 12, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x= 0, y = 270)
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGN , font=FONT)

    def score_update_add(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "Center", ('Arial', 12, 'normal'))

