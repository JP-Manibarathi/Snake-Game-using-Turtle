from turtle import Screen, Turtle

SNAKE_HEAD_SHAPE = [
    (-10, 0),
    (0, 20),
    (10, 0),
    (10, -10),
    (5, -20),
    (-5, -20),
    (-10, -10)
]

def create_head():
    turtle1 = Turtle()
    turtle1.penup()
    turtle1.goto(-10, -10)
    turtle1.begin_poly()

    for x, y in SNAKE_HEAD_SHAPE:
        turtle1.goto(x, y)

    turtle1.end_poly()
    custom_shape = turtle1.get_poly()
    return custom_shape

