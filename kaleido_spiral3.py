import turtle

from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angel,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angel)
    turtle.forward(shift)
    draw_circle(size+5,angel+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
turtle.circle(30)
