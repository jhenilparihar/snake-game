from turtle import Turtle, Screen
screen = Screen()
screen.tracer(0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
position = [(0, 0), (-10, 0), (-20, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in position:
            self.add_segment(i)

    def add_segment(self, i):
        segment = Turtle(shape="square")
        segment.shapesize(0.5)
        segment.color("Blue")
        segment.penup()
        segment.goto(i)
        self.snake.append(segment)

    def reset(self):
        for i in self.snake:
            i.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].xcor(), self.snake[segment - 1].ycor())
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
