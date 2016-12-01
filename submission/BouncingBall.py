# Name: Brian McCarthy
# Program: BouncingBall.py
from visual import *

autoscale = True

# floor the ball bounces off
floor = box(length=100, height=5, width=10, color =color.yellow,)

# ball
ball =  sphere(pos=(-50,60,0),radius=2, color=color.red,make_trail =True, trail_type ="curve")

# sets the ball to move left to right, and down
ball.velocity = vector(1,-1,0)

# gravity
g = 10

e = 0.95

# delta time
dt = 0.01

# time
t=0

# let the ball move 100px
while ball.pos.x<50:
    # set the rate
    rate(100)

    # move the ball
    ball.pos =  ball.pos + ball.velocity*dt

    # bounce the ball up
    if ball.y < ball.radius+floor.height/2:
        ball.velocity.y = -e*ball.velocity.y

    # bounce the ball down, (due to gravity)
    else:
        ball.velocity.y = ball.velocity.y - g*dt

    # update time
    t=t+dt
