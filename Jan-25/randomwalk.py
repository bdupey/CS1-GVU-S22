"""
Draw path of a random walk. 

Created on Wed Jan 19 22:28:25 2022
@author: mrobbins
"""

from turtle import * 
from random import randrange

def random_move(distance):
    """Take random step on a grid."""
    left(randrange(0, 360, 90))
    forward(distance)
    
def main():
    speed(0)
    while abs(xcor()) < 200 and abs(ycor()) < 200:
        random_move(25)
    exitonclick()
    
main()






