from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-100, 240)
        self.hideturtle()
        self.score = 0


    def update(self):
        self.print_score = f"Current level = {self.score}"
        self.clear()
        self.write(self.print_score, align="center", font=FONT)

    def win(self):
        self.score += 1


