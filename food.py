from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()    # inherited from turtle module, so we can call its method directly below
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.food_move_new_position()

    def food_move_new_position(self):
        random_x = randint(-280, 200)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)