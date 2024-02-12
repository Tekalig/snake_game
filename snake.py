from turtle import Turtle

MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.__snake_body = []
        for pos in range(3):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.shapesize(0.7, 0.7)
            snake.penup()
            snake.setpos(-MOVE * pos, 0)
            self.__snake_body.append(snake)

    def move(self):
        for i in range(len(self.__snake_body) - 1, 0, -1):
            x = self.__snake_body[i - 1].xcor()
            y = self.__snake_body[i - 1].ycor()
            self.__snake_body[i].goto(x, y)
        self.__snake_body[0].forward(MOVE)

    def extend_tail(self):
        snake = Turtle()
        snake.shape("square")
        snake.shapesize(0.7, 0.7)
        snake.color("white")
        snake.penup()
        self.__snake_body.append(snake)

    def well_collision(self):
        return self.__snake_body[0].xcor() > 330 or self.__snake_body[0].ycor() > 330 or self.__snake_body[
            0].xcor() < -330 or self.__snake_body[0].ycor() < -330

    def tail_collision(self):
        for i in range(1, len(self.__snake_body[1:])):
            if self.__snake_body[0].distance(self.__snake_body[i]) < 10:
                return True
        return False

    def position(self, food):
        return self.__snake_body[0].distance(food)

    def left(self):
        if self.__snake_body[0].heading() != RIGHT:
            self.__snake_body[0].setheading(180)

    def right(self):
        if self.__snake_body[0].heading() != LEFT:
            self.__snake_body[0].setheading(0)

    def up(self):
        if self.__snake_body[0].heading() != DOWN:
            self.__snake_body[0].setheading(90)

    def down(self):
        if self.__snake_body[0].heading() != UP:
            self.__snake_body[0].setheading(270)
