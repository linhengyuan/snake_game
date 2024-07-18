from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Leo's snake game")
screen.tracer(0)

# Define class
snake = Snake()
food = Food()
scoreboard = Score()

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
        scoreboard.score_update_add()
        snake.extend()

    # Detect collision with wall
    if snake.snake_body[0].xcor() > 290 or snake.snake_body[0].xcor() < (-290) \
            or snake.snake_body[0].ycor() > 290 or snake.snake_body[0].ycor() < -290:
        scoreboard.reset_game()
        snake.reset()

    # Detect collision with Tail
    for seg in snake.snake_body[1:]:
        if snake.snake_body[0].distance(seg) < 15:
            scoreboard.reset_game()
            snake.reset()


screen.exitonclick()