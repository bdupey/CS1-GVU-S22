"""
Created on Wednesday, Jan 19 22:25:25 2022
@author: mrobbins
"""

from turtle import * 

def spiral(firststep, angle, gap):
  """ Move turtle on a spiral path """
  step = firststep
  while step > 0:
      forward(step)
      left(angle)
      step = step - gap
  
def main():
  spiral(100, 71, 2)
  spiral(100, 71, -5)
  exitonclick()
  
main()
