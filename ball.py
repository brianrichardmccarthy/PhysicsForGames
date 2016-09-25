# Brian McCarthy
# 16/09/2016
# ball.py

from visual import *

# create two ball objects and a box object "floor"
ball = sphere(pos=(2, 2, 2), color=color.red)
ball2 = sphere(pos=(4,4,4), color=color.yellow)
floor = box(length=2, height=0.2, width=2, color=color.green)
