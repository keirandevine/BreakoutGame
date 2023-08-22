from turtle import Turtle, Screen


screen = Screen()

class Paddle:
        def __init__(self):
            self.screen = screen
            self.paddle = []
            self.head_turtle = Turtle()

        def create_paddle(self):
            xcor = -50
            screen.tracer(0)
            for i in range(7):
                segment = Turtle()
                segment.penup()
                segment.shape("square")
                segment.color("white")
                segment.shapesize(0.7)
                segment.goto(xcor, -250)
                segment.setheading(0)
                segment.showturtle()
                xcor += 15
                self.paddle.append(segment)
            self.head_turtle = self.paddle[0]
            self.head_turtle.color("blue")
            self.paddle[6].color("blue")
            screen.update()

        def move_left(self):
            self.head_turtle.backward(50)
            xcor = self.head_turtle.xcor() + 15
            for paddle in self.paddle:
                paddle.goto(xcor, -250)
                xcor += 15
                self.screen.update()

        def move_right(self):
            self.head_turtle.forward(50)
            xcor = self.head_turtle.xcor() + 15
            for paddle in self.paddle:
                paddle.goto(xcor, -250)
                xcor += 15
                self.screen.update()

class Ball:

        def __init__(self, paddle):
            self.ball = Turtle()
            self.screen = screen
            self.paddle = paddle
            self.speed = 1
            self.xcor = 0
            self.ycor = 0

        def create_ball(self):
            self.ball.goto(0, -120)
            self.ball.shape("circle")
            self.ball.shapesize(0.8)
            self.ball.penup()
            self.ball.color("white")
            self.ball.showturtle()
            self.ball.setheading(240)
            self.xcor = self.ball.xcor()
            self.ycor = self.ball.ycor()


        def move(self):
            self.ball.forward(self.speed)
            self.screen.update()

        def bounce_hor(self):
            heading = 360 - self.ball.heading()
            self.ball.setheading(heading)

        def bounce_ver(self):
            heading = 180 - self.ball.heading()
            self.ball.setheading(heading)

        def hit_paddle(self):
            for segment in self.paddle:
                if self.ball.distance(segment.xcor(), segment.ycor()) <= 16:
                    self.bounce_hor()
            if self.ball.distance(self.paddle[0].xcor(), self.paddle[0].ycor()) <= 10:
                self.ball.setheading(self.ball.heading() + 20)
            if self.ball.distance(self.paddle[6].xcor(), self.paddle[6].ycor()) <= 10:
                self.ball.setheading(self.ball.heading() - 20)

        def hit_block(self, block_list, brain):
            for block in block_list:
                if self.ball.distance(block.xcor, block.ycor) < 20 and self.ball.ycor() <= block.ycor - 6:
                    self.bounce_hor()
                    brain.break_block(block_list.index(block))


        def hit_walls(self):
            if self.ball.xcor() >= 178 or self.ball.xcor() <= -185:
                self.bounce_ver()
            if self.ball.ycor() >= 225:
                self.bounce_hor()


        def check_position(self):
            self.xcor = self.ball.xcor()
            self.ycor = self.ball.ycor()


class Block:
    def __init__(self):
        self.strength = 0
        self.xcor = 0
        self.ycor = 0
        self.score = 20


    def make_block(self):
        block = Turtle()
        block.color("yellow")
        block.shape("square")
        block.shapesize(0.4, stretch_len=2)
        block.penup()
        block.showturtle()
        return block



class GameBrain:

    def __init__(self):
        self.blocks_list = []
        self.score = 0
        self.level = 1
        self.pen = Turtle()

    def top_line(self):
        pen = Turtle()
        pen.penup()
        pen.pensize(3)
        pen.pencolor("white")
        pen.goto(-200, 230)
        pen.pendown()
        pen.goto(200, 230)

    def create_scoreboard(self):
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.pencolor("white")
        self.pen.goto(-180, 250)
        self.pen.write(f"Score: {self.score}", font=("Arial", 20, "normal"))


    def update_score(self):
        self.pen.clear()
        self.pen.hideturtle()
        self.pen.pencolor("white")
        self.pen.goto(-180, 250)
        self.pen.write(f"Score: {self.score}", font=("Arial", 20, "normal"))


    def display_level(self, level):
        pen = Turtle()
        pen.penup()
        pen.hideturtle()
        pen.goto(60, 250)
        pen.color("white")
        pen.write(f"Level: {level}", font=("Arial", 20, "normal"))

    def check_collision(self, ball, block):
        x1, y1 = ball.xcor, ball.ycor
        x2, y2 = block.xcor, block.ycor
        width1, height1 = 14, 14
        width2, height2 = 18, 36

        if (x1 + width1 / 2 > x2 - width2 / 2 and
                x1 - width1 / 2 < x2 + width2 / 2 and
                y1 + height1 / 2 > y2 - height2 / 2 and
                y1 - height1 / 2 < y2 + height2 / 2):
            return True
        return False








