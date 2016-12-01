from visual import *
import math

autoscale = True
ball = sphere(pos=(0, 30, 500), radius=2, color = color.red, make_trail = True,
               trail_type = "curve")

ball.velocity = vector(1,-1,0)

t = 0
dt = 0.01

while t < 50:
    rate(100)
    ball.velocity.x = ball.velocity.x + (-(6*cos(2*pi*t))/(2*pi) + 6/(2*pi))
    ball.pos = ball.pos + ball.velocity*dt
    t+=dt
