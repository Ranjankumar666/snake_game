from turtle import Turtle
import random
MAX_X = 280
MAX_Y = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = super()
        self.create()

    def create(self):
        food = self.food
        food.shape('circle')
        food.shapesize(stretch_wid=0.5, stretch_len=0.5)
        food.color('blue')
        food.speed('fastest')
        food.penup()
        food.goto(random.randint(-MAX_X, MAX_X),
                  random.randint(-MAX_Y, MAX_Y))
