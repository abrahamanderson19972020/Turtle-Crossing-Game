from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        y_coordinate = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_coordinate)

    def down(self):
        y_coordinate = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor() , y_coordinate)

    def go_right(self):
        x_coordinate = self.xcor() + MOVE_DISTANCE
        self.goto(x_coordinate, self.ycor())

    def go_left(self):
        x_coordinate = self.xcor() - MOVE_DISTANCE
        self.goto(x_coordinate, self.ycor())

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
