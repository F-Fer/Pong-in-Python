#simple Pong Game

import turtle
import time

wndw = turtle.Screen()
wndw.title("pong")
wndw.bgcolor("black")
wndw.setup(width = 800, height = 600)
wndw.tracer(0)


#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1.5

# Score Counter
scoreA = 0 
scoreB = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("player A: " + str(scoreA) + "    Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))



#functions
def updateScore():
    pen.write("player A: " + str(scoreA) + "    Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))

def paddleAUp():
    y = paddleA.ycor()
    if y <= 280:
        y += 20
        paddleA.sety(y)
    else:
        paddleA.sety(300)


def paddleADown():
    y = paddleA.ycor()
    if y >= -280:
        y -= 20
        paddleA.sety(y)
    else:
        paddleA.sety(-300)


def paddleBUp():
    y = paddleB.ycor()
    if y <= 280:
        y += 20
        paddleB.sety(y)
    else:
        paddleB.sety(300)


def paddleBDown():
    y = paddleB.ycor()
    if y >= -280:
        y -= 20
        paddleB.sety(y)
    else:
        paddleB.sety(-300)


#Keyboard Bindings

wndw.listen()
wndw.onkeypress(paddleAUp, "w")
wndw.onkeypress(paddleADown, "s")
wndw.onkeypress(paddleBUp, "Up")
wndw.onkeypress(paddleBDown, "Down")

#Main Game Loop
while True:
    pen.clear()
    pen.write("player A: " + str(scoreA) + "    Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))
    wndw.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("player A: " + str(scoreA) + "    Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))
        ball.dx = -1.5
        ball.dy = -1.5
        wndw.update()
        time.sleep(1)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        scoreB += 1
        pen.clear()
        pen.write("player A: " + str(scoreA) + "    Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))
        ball.dx = 1.5
        ball.dy = 1.5
        wndw.update()
        time.sleep(1)

    if (ball.xcor() >= 340) and (ball.xcor() <= 345) and (ball.ycor() >= paddleB.ycor() - 50.0) and (ball.ycor() <= paddleB.ycor() + 50.0):
        ball.dx *= -1.2
        ball.dy *= 1.2

    if (ball.xcor() <= -340) and (ball.xcor() >= -345) and (ball.ycor() >= paddleA.ycor() - 50.0) and (ball.ycor() <= paddleA.ycor() + 50.0):
        ball.dx *= -1.2
        ball.dy *= 1.2

