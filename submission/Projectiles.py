# Name: Brian McCarthy
# Program: Projectiles

from visual import *
autoscale = True

# floor object
floor = box(length=100, height=5, width=10, color =color.yellow,)

# ball object
ball =  sphere(pos=(-50,10,0),radius=2, color=color.red,make_trail =True,
trail_type ="curve")

# shoot the ball up with it's velocity
ball.velocity = vector(10,25,0)

# gravity
g = 10

e = 0.95

# delta time
dt = 0.01

# time
t=0

# same code as BouncingBall.py
while ball.pos.x<75:
    rate(1000)
    ball.pos =  ball.pos + ball.velocity*dt
    if ball.y < ball.radius+floor.height/2:
        ball.velocity.y = -e*ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - g*dt
    t=t+dt
