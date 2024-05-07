# Turtle Party Project
# by Robert Foss
# 5.7.24

import turtle
turtle.color("green")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
  if num <= 2:
    print("Error, Less than 3 sides")
  else:
    pass

def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
