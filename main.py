from tkinter import messagebox
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
from body import GameBody

body = GameBody()
body.create_game()

screen = Screen()
screen.setup(width=605, height=650)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    score.update_scoreboard()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 5:
        score.score_increment()
        food.refresh()
        snake.extend()
        snake.extend()
        score.score_increment()

    # Detect collision   with wall.
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 270 or x < -270 or y > 270 or y < -270:
        if not messagebox.askyesno("Game Over!", "Do you want to play again?"):
            game_is_on = False
            score.game_over()
        else:
            score.reset_()
            snake.reset()

    # Detect collision with tail.
    for i in snake.snake[1:]:
        if snake.head.distance(i) < 5:
            if not messagebox.askyesno("Game Over!", "Do you want to play again?"):
                game_is_on = False
                score.game_over()
            else:
                score.reset_()
                snake.reset()

screen.exitonclick()
