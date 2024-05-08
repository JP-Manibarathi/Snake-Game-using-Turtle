from turtle import Turtle,Screen
from highScore import High_score


class Score(Turtle):
    high_score = High_score()
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"SCORE :{self.score} HIGH SCORE: {self.high_score.get_highscore()}", True, align="center", font=("Roman", 20, "normal"))

    def inc_score(self):
        self.score = self.score+1
        self.high_score.update_highscore(self.score)
        self.update_score()

    def get_score(self):
        return self.score

    def game_over(self):
        self.home()
        self.write("HAHAHA U LOST! GAME OVER !!!", True, align="center",font=("Roman",20,"normal"))
        self.goto(0,-280)
        self.write("Press 'Space' to lose again. LOL :)", True, align="center", font=("Roman", 20, "normal"))





















