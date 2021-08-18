from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 19, "normal")

with open("data.txt") as file:
    contents = file.read()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = float(contents)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-270, 280)
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {int(self.score)}\t     High Score : {int(self.high_score)}", align=ALIGNMENT, font=FONT)

    # def reset_(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         with open("data.txt", mode='w') as edit_file:
    #             edit_file.write(str(self.high_score))
    #     self.score = 0
    #     self.update_scoreboard()

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER ", align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as edit_file:
                edit_file.write(str(self.high_score))

    def score_increment(self):
        self.score += 0.5
        self.update_scoreboard()
