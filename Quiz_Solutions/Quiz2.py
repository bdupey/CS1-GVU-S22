""" Quiz 2: rewrite polygon() to use a while loop instead of a for loop """

from turtle import *

# This is the original polygon function
def polygon(n, length):
    for _ in range(n):
        forward(length)
        left(360/n)

# Rewritten with a while loop
def polygon_2(n, length):
    side = 0
    while side < n:
        forward(length)
        left(360/n)
        side += 1
        
# Test using main from original polygon file
def main():
    """Draw polygons with 3-9 sides"""
    for j in range(3, 10):
        polygon_2(j, 80)
    
    exitonclick()
    
main()
