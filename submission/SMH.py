# Name: Brian McCarthy
# Program: SMH.py

from visual import *

autoscale = True

# length of ball to the celling
l = 0.6125

# gravity
g = 9.8

# omega pf ball 1
omega = sqrt((g/l))

# time
t = 0

# delta time
dt = 0.01

# floor object
floor = box(pos=(0,5,0), length=5, height=0.5, width=5, color = color.blue)

# ball object
ball = sphere(pos=(1, l ,0), radius=0.5)

# infinite loop
while True:
    rate(100)

    # set the ball position x equal to (0.4)x(cos((omega)x(time)))+(0.125*(sin((omega)(t))))
    ball.pos.x = (0.4*(cos((omega*t)))) + (0.125*(sin(omega*t)))
    ball.pos.y = (l/2)*ball.pos.x**2
    
    t+=dt
