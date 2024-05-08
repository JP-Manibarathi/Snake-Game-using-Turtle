from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("Blue")
        self.shapesize(0.5,0.5)
        self.goto(rd.randint(-280, 260), rd.randint(-280, 260))

    def place_food(self):
        self.goto(rd.randint(-280,260),rd.randint(-280,260))



