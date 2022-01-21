"""
Created on Wednesday, Jan 19 22:25:25 2022
@author: mrobbins
"""
#Goal of spiral is to use turtle to draw a spiral shape

from turtle import * 

def spiral(firststep, angle, gap):
    """ Move turtle on a spiral path """
    step = firststep
    while step > 0:
        forward (step)
        left(angle)
        step -= gap
        # step -= gap is the same as step = step - gap
        
def main():
  spiral(100,71,2)
  spiral(100,71,-5)
  exitonclick()
  
main()
