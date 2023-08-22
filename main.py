from game_manager import Paddle, screen, Ball, GameBrain, Block



#________________________________________Definition of Functions_______________________________________________#

def set_up_level():
    ball.create_ball()
    lay_blocks(brain.level)
    brain.top_line()
    brain.create_scoreboard()
    brain.display_level(brain.level)



def lay_blocks(level):
    xcor = -162
    ycor = 50
    global brain
    for i in range((level + 6) * 8):
        new_block = block.make_block()
        new_block.score = 20
        new_block.goto(xcor, ycor)
        brain.blocks_list.append(new_block)
        new_block.xcor = xcor
        new_block.ycor = ycor
        new_block.strength = 1
        xcor += 45
        if i > 15:
            new_block.strength += 1
            new_block.score += 20
            new_block.color("green")
            if i > 31:
                new_block.strength += 1
                new_block.score += 20
                new_block.color("orange")
                if i > 47:
                    new_block.strength += 1
                    new_block.score += 20
                    new_block.color("red")
        if xcor >= 162: ##Once blocks reach the edge of the screen, reset xcor and increase ycor to lay next row
            xcor = -162
            ycor += 12















#_______________________________________Creation of Class Objects_______________________________________________#

paddle = Paddle()
ball = Ball(paddle.paddle)
brain = GameBrain()
block = Block()
paddle.create_paddle()


#__________________________________Screen & Listening Event Setup______________________________________________#

screen.setup(width=400, height=600)
screen.bgcolor("black")

screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

screen.listen()



#______________________________________________Game Loop_____________________________________________________#

game_over = False
while not game_over:
    if brain.blocks_list != []:
        ball.move()
        ball.hit_paddle()
        ball.hit_walls()
        ball.check_position()
        brain.update_score()
        for block in brain.blocks_list:
            if brain.check_collision(ball, block):
                ball.bounce_hor()
                brain.score += block.score
                brain.update_score()
                block.strength -= 1
                if block.strength == 0:
                    brain.blocks_list.remove(block)
                    block.hideturtle()


    else:
        set_up_level()
        brain.level += 1



screen.mainloop()