#1
from turtle import *
def draw_triangle(x):
    for i in range(x):
        if i % 2 ==0:
            color("green")
            forward(200)
            left(100)
            forward(200)
            left(130)
            forward(254)
            left(130)
        else:
            color("blue")
            forward(200)
            left(100)
            forward(200)
            left(130)
            forward(254)
            left(130)
draw_triangle(120)
exitonclick()
