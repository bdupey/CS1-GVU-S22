
from turtle import *

def square_at(x, y, side_length):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    
def main():
    square_at(10, 25, 50)
    square_at(100, 0, 25)
    exitonclick()
    
main()
