from turtle import Turtle, Screen
import random


screen = Screen()

class Paddle:
        def __init__(self):
            self.paddle = Turtle()
            self.xcor = 0
            self.ycor = 0
            self.left_end = Turtle()
            self.left_end_y = self.ycor - 49
            self.right_end_y = self.xcor + 49
            self.right_end = Turtle()


        def create_paddle(self):
            """Creates a paddle and sets its position at the bottom of the screen"""
            screen.tracer(0)
            paddle = Turtle()
            paddle.penup()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(0.6, stretch_len=5)
            paddle.goto(0, -260)
            paddle.setheading(0)
            left_end = Turtle()
            left_end.penup()
            left_end.color("blue")
            left_end.shape("circle")
            left_end.shapesize(0.6)
            left_end.goto(paddle.xcor() - 49, -260)
            right_end = Turtle()
            right_end.penup()
            right_end.color("blue")
            right_end.shape("circle")
            right_end.shapesize(0.6)
            right_end.goto(paddle.xcor() + 49, -260)
            self.paddle = paddle
            self.left_end = left_end
            self.right_end = right_end
            screen.update()

        def move_left(self):
            """Moves paddle 30 pixels to the left"""
            screen.tracer(0)
            self.paddle.backward(30)
            self.left_end.backward(30)
            self.right_end.backward(30)
            screen.update()


        def move_right(self):
            """Moves paddle 30 pixels to the right"""
            screen.tracer(0)
            self.paddle.forward(30)
            self.left_end.forward(30)
            self.right_end.forward(30)
            screen.update()

        def check_coordinates(self):
            """Updates the xcor and ycor attributes to the current turtle position"""
            self.xcor = self.paddle.xcor()
            self.ycor = self.paddle.ycor()

class Ball:

        def __init__(self, paddle):
            self.ball = Turtle()
            self.screen = screen
            self.paddle = paddle
            self.speed = 0.5
            self.xcor = 0
            self.ycor = 0

        def create_ball(self, heading):
            """Takes a heading as an input, creates a ball and sets it's heading to the one input"""
            self.ball.goto(0, -120)
            self.ball.shape("circle")
            self.ball.shapesize(0.8)
            self.ball.penup()
            self.ball.color("white")
            self.ball.showturtle()
            self.ball.setheading(heading)
            self.xcor = self.ball.xcor()
            self.ycor = self.ball.ycor()


        def move(self):
            """Moves the ball forward by the amount defined in the class speed attribute"""
            self.ball.forward(self.speed)
            self.screen.update()

        def bounce_hor(self):
            """Resets the ball heading to reflect a bounce off a horizontal surface"""
            heading = 360 - self.ball.heading()
            self.ball.setheading(heading)

        def bounce_ver(self):
            """Resets the ball heading to reflect a bounce off a vertical surface"""
            heading = 180 - self.ball.heading()
            self.ball.setheading(heading)

        def hit_walls(self):
            """Detects collissions with the north, west and east walls then calls the appropriate type of bounce"""
            if self.ball.xcor() >= 178 or self.ball.xcor() <= -185:
                self.bounce_ver()
            if self.ball.ycor() >= 225:
                self.bounce_hor()


        def check_position(self):
            """Updates the class attributes xcor and ycor to current turtle position"""
            self.xcor = self.ball.xcor()
            self.ycor = self.ball.ycor()


        def change_angle_left(self):
            """Changes the angle of the ball to reflect a collision with the left of the paddle"""
            heading = self.ball.heading()
            self.ball.setheading(heading + 15)

        def change_angle_right(self):
            """Changes the angle of the ball to reflect a collision with the right of the paddle"""
            heading = self.ball.heading()
            self.ball.setheading(heading - 15)

class Block:
    def __init__(self):
        self.strength = 0
        self.xcor = 0
        self.ycor = 0
        self.score = 20



    def make_block(self):
        """Creates a new block and sets its default colour to yellow"""
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
        self.lives = 3
        self.level_pen = Turtle()
        self.score_pen = Turtle()
        self.lives_pen = Turtle()
        self.pen = Turtle()


    def top_line(self):
        """Draws the boundary at the north of the screen"""
        pen = Turtle()
        pen.penup()
        pen.pensize(3)
        pen.pencolor("white")
        pen.goto(-200, 230)
        pen.pendown()
        pen.goto(200, 230)

    def create_scoreboard(self):
        """Draws the scoreboard in the north-west corner of the screen"""
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.pencolor("white")
        self.pen.goto(-180, 250)
        self.pen.write(f"Score: {self.score}", font=("Arial", 20, "normal"))


    def update_score(self):
        """Clears and redraws the scoreboard to reflect updated score"""
        self.pen.clear()
        self.pen.hideturtle()
        self.pen.pencolor("white")
        self.pen.goto(-180, 250)
        self.pen.write(f"Score: {self.score}", font=("Arial", 20, "normal"))


    def display_level(self, level):
        """Draws the level display in the north-east of the screen"""
        self.level_pen.clear()
        self.level_pen.penup()
        self.level_pen.hideturtle()
        self.level_pen.goto(60, 250)
        self.level_pen.color("white")
        self.level_pen.write(f"Level: {level}", font=("Arial", 20, "normal"))


    def display_lives(self, lives):
        """Draws the lives display in the north-east of the screen"""
        self.lives_pen.clear()
        self.lives_pen.penup()
        self.lives_pen.hideturtle()
        self.lives_pen.goto(-180, 230)
        self.lives_pen.color("white")
        self.lives_pen.write(f"Lives: {lives}", font=("Arial", 10, "normal"))


    def check_block_collision(self, ball, block):
        """Returns true if ball and block come into contact, otherwise returns false"""
        x1, y1 = ball.xcor, ball.ycor
        x2, y2 = block.xcor, block.ycor
        width1, height1 = 14, 14
        width2, height2 = 36, 18

        if (x1 + width1 / 2 > x2 - width2 / 2 and
                x1 - width1 / 2 < x2 + width2 / 2 and
                y1 + height1 / 2 > y2 - height2 / 2 and
                y1 - height1 / 2 < y2 + height2 / 2):
            return True
        return False

    def check_paddle_collision(self, ball, paddle):
        """Returns true if ball comes into contact with paddle, otherwise returns false"""
        x1, y1 = ball.xcor, ball.ycor
        x2, y2 = paddle.xcor, paddle.ycor
        width1, height1 = 14, 14
        width2, height2 = 90, 12

        if (x1 + width1 / 2 > x2 - width2 / 2 and
                x1 - width1 / 2 < x2 + width2 / 2 and
                y1 + height1 / 2 > y2 - height2 / 2 and
                y1 - height1 / 2 < y2 + height2 / 2):
            return True
        return False

    def check_left_pad_collision(self, ball, paddle):
        """Returns true if ball comes into contact with left edge of paddle, otherwise returns false"""
        if ball.distance(paddle.xcor - 49, -265) < 22:
            return True
        return False

    def check_right_pad_collision(self, ball, paddle):
        """Returns true if ball comes into contact with right edge of paddle, otherwise returns false"""
        if ball.distance(paddle.xcor + 49, -265) < 22:
            return True
        return False

    def random_heading(self):
        """Creates a new random heading to be used as an input upon creation of a new ball"""
        random_heading1 = random.randint(240, 260)
        random_heading2 = random.randint(280, 300)
        headings = [random_heading1, random_heading2]
        random_heading = random.choice(headings)
        return random_heading

    def game_over_msg(self, score):
        """Displays a game over message along with player's score"""
        pen = Turtle()
        pen.penup()
        pen.pencolor("white")
        pen.goto(0, -100)
        pen.write(f"Game over\nFinal Score: {score}", font=("Arial", 20, "normal"), align="center")


    def declare_winner(self, score):
        """Displays a winner message along with player's score"""
        pen = Turtle()
        pen.penup()
        pen.pencolor("white")
        pen.goto(0, -100)
        pen.write(f"Congratulations. You win!\nFinal Score: {score}", font=("Arial", 20, "normal"), align="center")













