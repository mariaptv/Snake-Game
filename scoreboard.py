
from turtle import Turtle
URL  = "\\Users\maria\Documents\proyectos python\Snake-Game\data.txt"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(URL) as file:
            contents = file.read()
            self.high_score = int(contents)
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(URL, mode= "a") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    def refresh_count(self):
        self.score += 1
        self.update_score()

    def open_score(self):
        with open(URL) as file:
            contents = file.read()
            self.high_score = int(contents)
            return self.high_score
