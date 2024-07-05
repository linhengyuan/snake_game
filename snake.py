from turtle import Turtle

# snake body position, x-y axis, store in snake_body_position list

SNAKE_BODY_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in SNAKE_BODY_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_body.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)