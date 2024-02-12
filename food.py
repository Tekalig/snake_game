from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x = random.randint(-15, 15) * 20
        y = random.randint(-15, 15) * 20
        self.goto(x, y)
