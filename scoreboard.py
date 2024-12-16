from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0 , 260)
        self.write(arg= f"Score = {self.score}", move= False, align= ALIGNMENT, font= FONT )

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!! ", move=False, align=ALIGNMENT, font=("Courier", 32, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg= f"Score = {self.score}", move= False, align= ALIGNMENT, font= FONT )

