from visual import *
import math

autoscale = True
ball = sphere(pos=(0, 30, 500), radius=2, color = color.red)

ball.velocity = vector(0.5, 0, 0)
acceleration = 0
t = 0
dt = 0.01

while t < 0.4:
    rate(100)
    acceleration = (-4)*(ball.velocity.x)*(t)
    ball.velocity.x = ball.velocity.x + (acceleration*dt)
    ball.pos.x = ball.pos.x + (ball.velocity.x*dt) 
    t+=dt
