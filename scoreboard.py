
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align='center')
    def refresh_count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align='center', font=('Arial', 20, 'normal'))