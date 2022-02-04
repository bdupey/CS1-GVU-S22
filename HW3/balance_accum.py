"""
Created on Mon Jan 24 22:14:07 2022

@author: Robbins
"""

def balance_accum(principal, rate, years):
    """ Return balance with accumulated compound interest."""
    balance = principal
    for _ in range(years):
        interest = balance * rate
        balance += interest
    return balance

def main():
    """These tests are to demonstrate the function and are not required for the homework. """
    b1 = balance_accum(1000, .01, 10)
    print(b1)
    
    b2 = balance_accum(1000, .1, 10)
    print(b2)
    
    b3 = balance_accum(1000, 1, 10)
    print(b3)
    
main()
