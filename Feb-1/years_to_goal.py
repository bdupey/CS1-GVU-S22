# years_to_goal.py
# Return the number of years until a goal is met

def years_to_goal(principal, rate, goal):
    """ Return number of years to reach savings goal. """
    balance = principal
    years = 0
    while balance < goal:
        interest = balance * rate
        balance = balance + interest
        years += 1
    
    return years
        
    
def main():
    years_1 = years_to_goal(1000, .01, 1000000)
    print(years_1)
    
    years_2 = years_to_goal(1000, .1, 1000000)
    print(years_2)
    
    years_3 = years_to_goal(1000, 1, 1000000)
    print(years_3)
    
main()
