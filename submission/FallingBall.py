# Name: Brian McCarthy
# Program: FallingBall.py

from visual import *
autoscale = True

# final box, once the ball hits this line (their respective y match) stop the ball
floor = box(pos=(0,-12.5,0),length=500, height=5, width=10, color =color.blue)
check1 = box(pos=(0,400,0),length=500, height=5, width=10, color =color.yellow)
check2 = box(pos=(0,300,0),length=500, height=5, width=10, color =color.yellow)
check3 = box(pos=(0,200,0),length=500, height=5, width=10, color =color.yellow)
check4 = box(pos=(0,100,0),length=500, height=5, width=10, color =color.yellow)

# ball object
ball =  sphere(pos=(0,500,0),radius=10, color=color.red,make_trail = True,
trail_type="curve")

# time
t = 0.0

# delta time
dt = 0.01

# while the position of the ball on the y direction is greater than -12.5
while ball.pos.y > -12.5:
    rate(1000)
    ball.pos.y = 500-5*(t**2)
    t=t+dt
