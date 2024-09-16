import time
from turtle import Screen, Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:

segments = []
for i in STARTING_POSITIONS:
    t2 = Turtle()
    t2.shape("square")
    t2.penup()
    t2.color("white")
    t2.goto(i)
    segments.append(t2)



def move():
    for seg_num in range(len(segments)-1,  0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)