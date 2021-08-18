from turtle import Turtle


class GameBody(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-275, 275)
        self.pendown()
        self.create_game()

    def create_game(self):
        self.pencolor("white")
        self.pensize(3)
        for i in range(4):
            if i % 2 == 0:
                self.forward(550)
            else:
                self.forward(550)
            self.right(90)
