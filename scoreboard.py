from turtle import Turtle

ALIGN = "Center"
FONT = ('Arial', 12, 'normal')



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("score_data.txt", mode="r") as score:
            self.high_score = int(score.read())
        self.penup()
        self.goto(x= 0, y = 270)
        self.color("white")
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN , font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "Center", ('Arial', 12, 'normal'))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as score:
                score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def score_update_add(self):
        self.score += 1
        self.update_scoreboard()
