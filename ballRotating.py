from visual import *
L=10

# axis
xaxis = curve(pos=[(0,0,0), (L,0,0)], color=color.red)
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=color.blue)
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))

# ball object. 1) at 0,0,0 will not move. 2) ball to be move along the different axis
ball1 = sphere(pos=(-2.5,0,0),radius=0.2, color=color.cyan,make_trail = true, trail_type = "curve")
ball2 = sphere(pos=(0,0,0),radius=0.3,   color=color.red)
autoscale = True
dt =0.01
t=0
while 1:
    rate(100)
    # original
    ball1.velocity =vector(5*sin(2*t),5*cos(2*t))

    # across the x axis only
    # ball1.velocity =vector(5*sin(2*t))
    # ball1.velocity =vector(5*cos(2*t))

    # across the y axis only
    # ball1.velocity =vector(0, 5*sin(2*t))
    # ball1.velocity =vector(0, 5*cos(2*t))

    # across the z axis only
    # ball1.velocity =vector(0, 0, 5*sin(2*t))
    # ball1.velocity =vector(0, 0, 5*cos(2*t))

    # across the x axis and y axis
    # ball1.velocity =vector(5*sin(2*t), 5*sin(2*t))
    # ball1.velocity =vector(5*cos(2*t), 5*cos(2*t))
    # ball1.velocity =vector(5*cos(2*t), 5*sin(2*t))
    # ball1.velocity =vector(5*sin(2*t), 5*cos(2*t))


    # across the y axis and z axis
    # ball1.velocity =vector(0, 5*sin(2*t), 5*sin(2*t))
    # ball1.velocity =vector(0, 5*cos(2*t), 5*cos(2*t))
    # ball1.velocity =vector(0, 5*cos(2*t), 5*sin(2*t))
    # ball1.velocity =vector(0, 5*sin(2*t), 5*cos(2*t))

    # across all axis
    # ball1.velocity =vector(5*sin(2*t), 5*sin(2*t), 5*sin(2*t))
    # ball1.velocity =vector(5*cos(2*t), 5*cos(2*t), 5*cos(2*t))


    ball1.pos += ball1.velocity*dt
    t=t+dt
