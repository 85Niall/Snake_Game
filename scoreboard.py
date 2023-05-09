from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def create_screen(self):
        screen_line = Turtle()
        screen_line.hideturtle()
        screen_line.color("white")
        screen_line.penup()
        screen_line.goto(-280, 280)
        screen_line.pendown()
        screen_line.goto(280, 280)
        screen_line.goto(280, -280)
        screen_line.goto(-280, -280)
        screen_line.goto(-280, 280)
        screen_line.penup()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
