from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.squares[0].distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()

    for square in snake.squares:
        if square.xcor() >= 300 or square.xcor() <= -300 or square.ycor() >= 300 or square.ycor() <= -300:
            scoreboard.reset()
            snake.reset()
            time.sleep(0.2)

    for square in snake.squares[1:]:
        if snake.squares[0].distance(square) < 10:
            scoreboard.reset()
            snake.reset()
            time.sleep(0.2)

screen.exitonclick()
