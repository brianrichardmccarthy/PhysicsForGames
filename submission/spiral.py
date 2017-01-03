# Name: Brian McCarthy
# Program: Spiral.py

from visual import *

# moving ball object
ball = sphere(pos=(5, 0,0),radius=0.2, color=color.cyan, make_trail = True, trail_type = "curve")

# stationary ball object
b = sphere(pos=(0, 0, 0), radius=0.2, color=color.red)

# arrow object
velocityArrow = arrow(pos=(0,0,0), axis=(5,0,0), shaftwidth=.1)
autoscale = True

# delta time
dt = 0.01

# time
t = 0

# while t is less than 5
while t<50:
    rate(1000)

    # move the ball in a circle
    ball.pos = vector(5*cos(2*t), 5*sin(2*t), ball.pos.z+dt)

    # move the arrow pointer
    velocityArrow.axis = ball.pos

    # increment t by delta t
    t=t+dt
