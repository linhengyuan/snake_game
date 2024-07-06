from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.write("Score: ", False, "Left", ('Arial', 8, 'normal'))
