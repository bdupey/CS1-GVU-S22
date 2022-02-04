# balance_accum.py
# Calculate balance with accumulated interest

def balance_accum(principal, rate, years):
    """ Return balance with accumulated compound interest. """
    balance = principal
    for _ in range(years):
        interest = balance * rate
        balance += interest
        
    return balance
    

def main():
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): " ))
    years = int(input("Years: " ))
    
    new_balance = balance_accum(principal, rate, years)
    
    print("Balance after ", years, "years is: ", new_balance)
    
    
    
main()


# Balance after  7 years is:  107.213535210701



