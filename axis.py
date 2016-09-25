from visual import *

L=10

# create the three axis
xaxis = curve(pos=[(0,0,0), (L,0,0)], color=color.red)
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=color.blue)
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))
ball = sphere(pos=(0,0,0),radius=0.3,   color=color.red)

# enable autoscale
autoscale = True

# variables to update the time
dt =0.01
t=0

while 1:
    rate(100)
    t=t+dt
