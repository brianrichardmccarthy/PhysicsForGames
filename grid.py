# creates a grid across the axis

from visual import *
L=10
ball = sphere(pos=(0,0,0),radius=0.3,   color=color.red)
autoscale = True
dt =0.01
t=0

x = 0
while x <= 10:
    # x axis
    # bottom
    xaxis = curve(pos=[(0,0,x), (L,0,x)], color=color.red)
    # top
    # xaxis = curve(pos=[(0,L,x), (L,L,x)], color=color.red)

    # y axis
    # back
    yaxis = curve(pos=[(x,0,0), (x,L,0)], color=color.blue)
    # front
    # yaxis = curve(pos=[(x,0,L), (x,L,L)], color=color.blue)

    # z axis
    # left
    zaxis = curve(pos=[(0,x,0), (0,x,L)], color=(0.5,0.5,0.5))
    # right
    zaxis = curve(pos=[(L,x,0), (L,x,L)], color=(0.5,0.5,0.5))

    # update loop counter
    x += 1


while 1:
    rate(100)
    t=t+dt
