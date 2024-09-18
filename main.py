import time
from snake import Snake
from turtle import Screen
from food import  Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision
    if snake.segments[0].distance(food) < 25:
        food.refresh()
        snake.extend()
        score.refresh_count()

    #Wall colision
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect tail collision
    for segment in snake.segments[1:]:
         if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()