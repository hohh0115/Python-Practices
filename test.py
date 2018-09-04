
"""
import turtle

a = turtle.Turtle()
a.speed(50)

for i in range(180):
    a.forward(100)
    a.right(30)
    a.forward(20)
    a.left(60)
    a.forward(50)
    a.right(30)
    a.penup()
    a.setposition(0, 0)
    a.pendown()
    a.right(2)
    # turtle.done()
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()