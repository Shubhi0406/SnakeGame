from turtle import Turtle, Screen
screen = Screen()

move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for square in range(3):
            self.add_square(0, 0)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            x_new = self.squares[square_num - 1].xcor()
            y_new = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(x_new, y_new)
        self.squares[0].forward(move_distance)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def extend(self):
        x = self.squares[-1].xcor()
        y = self.squares[-1].ycor()
        self.add_square(x, y)

    def add_square(self, x, y):
        sq = Turtle(shape="square")
        sq.color("white")
        sq.penup()
        sq.goto(x, y)
        x -= 20
        self.squares.append(sq)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
