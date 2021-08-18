from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-260, 260)
        y_cor = random.randint(-260, 260)

        x_round = x_cor % 10
        y_round = y_cor % 10
        if 10 - x_round <= 5:
            x_cor = x_cor + (10 - x_round)
        else:
            x_cor = x_cor - (10 - (10 - x_round))

        if 10 - y_round <= 5:
            y_cor = y_cor + (10 - y_round)
        else:
            y_cor = y_cor - (10 - (10 - y_round))

        self.goto(x_cor, y_cor)
