from turtle import *

#we want to paint a house

#step 1: draw a square

width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 

forward(70)
color("purple")
begin_fill()
left(90)   
forward(110)     
right(90)      #height of the door
forward(60)
right(90)
forward(110)
end_fill()
#drawing a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a window
penup()
goto(10, 120)
pendown()
color("brown")
begin_fill()
left(120)
forward(40)
right(180)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
#drawing a second window
penup()
goto(190,120)
pendown()
color("brown")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
exitonclick()


