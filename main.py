from game_manager import Paddle, screen, Ball, GameBrain, Block



#________________________________________Definition of Functions_______________________________________________#

def set_up_level():
    """Creates a new ball, blocks, scoreboard and level display. Draws the line at the top of the screen"""
    ball.create_ball(brain.random_heading())
    lay_blocks(brain.level)
    brain.top_line()
    brain.create_scoreboard()
    brain.display_level(brain.level)



def lay_blocks(level):
    """Creates the appropriate number of blocks for the level. Lays out blocks in correct position and changes block
    color and strength to reflect level"""
    xcor = -162
    ycor = 0
    global brain
    for i in range((level) * 8):
        new_block = block.make_block()
        new_block.score = 20
        new_block.goto(xcor, ycor)
        brain.blocks_list.append(new_block)
        new_block.xcor = xcor
        new_block.ycor = ycor
        new_block.strength = 1
        xcor += 45

        #Check position of blocks and power up

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
        if xcor >= 162:
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
        ball.hit_walls()
        ball.check_position()
        paddle.check_coordinates()
        brain.update_score()
        brain.display_lives(brain.lives)
        if brain.check_paddle_collision(ball, paddle):
            ball.bounce_hor()
            if brain.check_left_pad_collision(ball.ball, paddle):
                print("Hit left paddle")
                ball.change_angle_left()
            if brain.check_right_pad_collision(ball.ball, paddle):
                print("Hit right paddle")
                ball.change_angle_right()
        for block in brain.blocks_list:
            if brain.check_block_collision(ball, block):
                ball.bounce_hor()
                brain.score += block.score
                brain.update_score()
                block.strength -= 1
                if block.strength == 0:
                    brain.blocks_list.remove(block)
                    block.hideturtle()
        if ball.ycor <= -265:
            brain.lives -= 1
            ball.create_ball(brain.random_heading())
        if brain.lives == 0:
            game_over = True
            brain.game_over_msg(score=brain.score)


    else:
        block = Block()
        set_up_level()
        brain.level += 1
        if brain.level == 8:
            game_over = True


#________________________________________Breakout of Game Loop_______________________________________________#


brain.declare_winner(brain.score())



screen.mainloop()