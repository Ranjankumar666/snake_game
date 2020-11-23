from turtle import Turtle
MOVE_DISTANCE = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[- 1]

    def create_snake(self):
        for p in POSITIONS:
            self.add_segment(p)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()

            self.segments[i].goto(new_x, new_y)

        self.segments[0].fd(MOVE_DISTANCE)

    def add_segment(self, p):
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.speed('fastest')
        new_turtle.goto(p)
        new_turtle.color('white')
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.tail.position())

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
