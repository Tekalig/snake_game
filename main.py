from turtle import Screen
from snake import Snake
from food import Food
from Score_board import Score
import time

# screen object
road = Screen()
road.setup(width=700, height=700)
road.bgcolor("gray")
road.title("Snake Game")
road.tracer(0)

# snake object
snake = Snake()
food = Food()
score = Score()
# This will call the up function if the "Left" arrow key is pressed
road.listen()
road.onkey(snake.left, "Left")
road.onkey(snake.right, "Right")
road.onkey(snake.up, "Up")
road.onkey(snake.down, "Down")


going_on = True
while going_on:

    road.update()
    time.sleep(0.1)
    
    if snake.position(food) < 10:
        snake.extend_tail()
        food.new_food()
        score.count()

    if snake.well_collision():
        going_on = False
        score.game_over()
        
    if snake.tail_collision():
        going_on = False
        score.game_over()

    snake.move()

road.exitonclick()
