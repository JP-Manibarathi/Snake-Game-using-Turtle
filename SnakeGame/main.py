import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
import snakeShape


screen = Screen()
screen.bgcolor("black")
snake_shape = snakeShape
screen.tracer(0)
screen.setup(width = 600,height=600)
screen.addshape("snake_head", snake_shape.create_head())

snake = Snake()

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("white")
turtle.goto(0, 240)



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



def play_game():
    high_score = 0
    game_is_on = True
    score = Score()
    food = Food()
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280  or snake.segments[0].ycor() < -280:
            score.game_over()
            game_is_on = False
        if snake.segments[0].distance(food) < 20:
            food.place_food()
            score.inc_score()
            snake.extend_snake()
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                score.game_over()
                game_is_on = False


play_game()

def restart_game():
    screen.reset()
    snake.reset()
    play_game()

screen.listen()
screen.onkey(restart_game, "space")


screen.mainloop()
screen.exitonclick()


