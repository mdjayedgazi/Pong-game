from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.R_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(x =-100,y=200)
        self.write(self.l_score,align= "center", font=("Comic Sans",40,"normal"))
        self.goto(x =100,y=200)
        self.write(self.R_score,align= "center", font=("Comic Sans",40,"normal"))


    def right_score(self):
        self.R_score +=1
        self.update_scoreboard()

    def left_score(self):
        self.l_score +=1
        self.update_scoreboard()