# Make A Pyhton Game #1

# Game 1: Pong
# First Import Turtle (Built in Library)

import turtle as t

# Declare Player A and Player B score variables
playerAscore = 0
playerBscore = 0

# Need to create a window variable and call the screen from turtle
# -------------------------------------------------------------- #
window = t.Screen()
# Set the title as "Pong Game"
window.title("Pong Game")
# Set the background color
window.bgcolor("green")
# Set dimensions of the screen
window.setup(width= 800, height = 800)
# Set the screen speed
window.tracer(0)
# --------------------------------------------------------------- #

# Need to create the two paddles for the players
# --------------------------------------------------------------- #
# Create the variables for the paddles and call the turtle object
leftpaddle=t.Turtle()
# Set the paddle's speed, shape, color, and shape size 
# These are the object's attributes
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# To create the right paddle, just copy and paste, and change the position
rightpaddle=t.Turtle()

rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)
# goto is the position method. Notice left is negative, right is positive 
# --------------------------------------------------------------- #

# Need to create the ball
# --------------------------------------------------------------- #
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.3
ballydirection=0.3
# --------------------------------------------------------------- #

# Need to create pen object
# --------------------------------------------------------------- #
# This object updates the scoreboard, and gives attributes such 
# as speed, color, position, text, and alignment

# Scoreboard Update
pen=t.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {}     Player 2: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))
# --------------------------------------------------------------- #

# Need to do the movements of objects and the logistics
# --------------------------------------------------------------- #
# Moving the leftpaddle
# Declare functions for up and down
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

# Copy the functions for the right paddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
# --------------------------------------------------------------- #

# Need to assign the keys to movement
# --------------------------------------------------------------- #
# Get the window to listen for input
window.listen()
# Assign keys
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')
# --------------------------------------------------------------- #

# Need to create the main game loop
# --------------------------------------------------------------- #
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety((ball.ycor()+ballydirection))

    # Set border width between the paddle boundaries of the screen
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    # Set right width border and count a score
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("Player 1: {}     Player 2: {}".format(playerAscore, playerBscore), align='center', font=('Arial', 24, 'normal'))

    # Set left width border and count b score
    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerBscore=playerBscore+1
        pen.clear()
        pen.write("Player 1: {}     Player 2: {}".format(playerAscore, playerBscore), align='center', font=('Arial', 24, 'normal'))

    # Handling the Collisions
    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor() > rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection*-1

    if (ball.xcor()<-340) and (ball.xcor()>-350)and(ball.ycor()<leftpaddle.ycor()+40) and ball.ycor() > leftpaddle.ycor()-30:
        ball.setx(-340)
        ballxdirection=ballxdirection*-1

# --------------------------------------------------------------- #