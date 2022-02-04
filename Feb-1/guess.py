# guess.py
# User guesses a random number

from random import randint

def userguess(secret): 
    """ Ask user for guesses until matching secret. """
    response = int(input("Your guess? "))
    while response != secret:
        response = int(input("Wrong! Next guess? "))
    if response == secret:
        print("Correct!")
    
    
def main():
    secret_num = randint(1, 10)
    userguess(secret_num)
    
main()
