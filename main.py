from snake import Snake
from turtle import Screen, Turtle
from food import Food
from score import Score
import time

WALL_BREAKS = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


score = Score()
food = Food()
snake = Snake()

screen.listen()

screen.onkeypress(snake.move_up, 'Up')
screen.onkeypress(snake.move_down, 'Down')
screen.onkeypress(snake.move_left, 'Left')
screen.onkeypress(snake.move_right, 'Right')


# game_is_on = False


def gameplay(game_is_on):
    score.clear()
    score.score = 0
    score.write()

    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move_snake()

        if snake.head.distance(food) < 15:
            score.increment()
            score.write()
            snake.extend()
            food.create()

        if(snake.head.xcor() > WALL_BREAKS or snake.head.ycor() > WALL_BREAKS or
           snake.head.xcor() < -WALL_BREAKS or snake.head.ycor() < -WALL_BREAKS):
            game_is_on = False
            snake.head.home()
            score.endgame()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.endgame()


screen._write(pos=(-250, 280), align='left', txt='Click to start', font=(
    'Courier', 8, 'bold'), pencolor='white')


def start(x, y):
    gameplay(True)
    # score.clear()


screen.onclick(fun=start, add=True)


# screen.exitonclick()
screen.mainloop()
