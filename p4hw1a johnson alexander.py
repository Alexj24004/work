# #alexander johnson
# 4-25-25
# shows the ability to be able to create shapes using turtle graphics

import turtle


screen = turtle.Screen()
screen.bgcolor("white")  

t = turtle.Turtle()

=t.penup()  
t.goto(-100, 0)  
t.pendown()  # 

for _ in range(4): 
    t.forward(100)  
    t.left(90)  

t.penup()
t.goto(50, 0)  
t.pendown()


for _ in range(3):  
    t.forward(100)  
    t.left(120) 


t.hideturtle()

turtle.done()