from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.__value = 0
        self.__high_score = 0
        with open("/home/besu/Soft-Pro/Py/_py/score_result.txt") as score_file:
            self.__high_score = int(score_file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 320)
        self.update()

    def count(self):
        self.clear()
        self.__value += 1
        self.update()

    def update(self):
        self.write(f"Score: {self.__value}  High Score: {self.__high_score}",
                   align="center", font=("monospace", 16, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=("Monospace", 24, "bold"))
        if self.__high_score < self.__value:
            with open("/home/besu/Soft-Pro/Py/_py/score_result.txt", mode='w') as score_file:
                score_file.write(str(self.__value))
