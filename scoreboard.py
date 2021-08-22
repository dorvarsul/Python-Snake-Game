from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open(r"C:\Users\User\Desktop\data.txt", "r") as file:
            self.high_score = file.read()
        self.refresh_high_score()
        self.refresh()

    def refresh_high_score(self):
        with open("C:/Users/User/Desktop/data.txt") as file:
            self.high_score = int(file.read())

    def increase_score(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}     High Score: {self.high_score}", True, "center", ("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, "center", ("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("C:/Users/User/Desktop/data.txt", "w") as file:
                file.write(f"{self.score}")
            self.refresh_high_score()
        self.score = 0
        self.refresh()
