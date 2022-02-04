"""
Create a program that prints your letter grade based on 
your numeric grade

Created on Tue Jan 18 17:52:25 2022
@author: mrobbins
"""

def letter_grade(grade):
    """Print the letter grade given the numeric grade"""
    if grade >= 91:
        print("Excellent")
    elif grade >= 81:
        print("b")
    elif grade >= 70:
        print("Cool kids")
    elif grade >= 61:
        print("Doing great!")
    else:
        print("Fantastic!")
    
def main():
#    letter_grade(95)
#    letter_grade(87)
#    letter_grade(78)
#    letter_grade(63)
    letter_grade(90)
    
main()
