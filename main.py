from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Leo's snake game")
screen.tracer(0)

# Define class
snake = Snake()
food = Food()

# Call class method
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # manipulate the speed of snake, shorter faster
    snake.move()

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.food_move_new_position()


screen.exitonclick()