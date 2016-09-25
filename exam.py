# previous paper
# creates a bouncing ball
# goes down until hits the "floor"
# the goes up
# repeats indifinitly
from visual import *

floor = box(pos = (0, -25, 0), length = 4, height = 0.5, width = 4, color = color.blue)

ball = sphere(pos=(0, 10, 0), radius = 0.25, color=color.red)
ball.velocity = vector(0, -1, 0)

dt = 0.1

while 1:
    rate(100)
    ball.pos = ball.pos + ball.velocity * dt
if ball.y < ball.radius/2:
    ball.velocity.y = -ball.velocity.y
else:
    ball.velocity.y = ball.velocity.y - 9.8*dt
