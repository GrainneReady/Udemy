from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH_HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.setheading(NORTH_HEADING)
        self.reset()

    def reset(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def finishLineCheck(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset()
            return True
        return False
