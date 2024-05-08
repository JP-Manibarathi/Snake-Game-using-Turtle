from turtle import Turtle

INIT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in INIT_POSITIONS:
            self.addsegment(pos)

    def addsegment(self,pos):
        turtle = Turtle()
        self.pos = pos
        turtle.penup()
        turtle.color("red")
        if pos == (0,0):
            turtle.shape("snake_head")
        else:
            turtle.shape("triangle")
        turtle.goto(pos)
        self.segments.append(turtle)

    def extend_snake(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(DISTANCE)
        #self.segments[0].left(180)

    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)
    def reset(self):
        self.segments.clear()

        self.create_snake()
