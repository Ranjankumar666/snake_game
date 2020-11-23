from turtle import Turtle
FONT_STYLES = ("Courier", 16, "bold")
FONT_ALIGN = 'center'
GAME_OVER = ("Courier", 30, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.scorecard = super()
        self.write()

    def write(self):
        self.scorecard.clear()
        self.scorecard.color('red')
        self.scorecard.hideturtle()
        self.scorecard.penup()
        self.scorecard.goto(x=0, y=270)
        self.scorecard.write(f'Score: {self.score}',
                             move=False, align=FONT_ALIGN, font=FONT_STYLES)

    def clear(self):
        self.scorecard.clear()

    def increment(self):
        self.score += 1

    def endgame(self):
        self.scorecard.goto(x=0, y=0)
        self.scorecard.write(f'Game Over',
                             move='FALSE', align=FONT_ALIGN, font=GAME_OVER)
