# balance_table.py
# Print table of account balances earning interest.

def balance(p, r, t):
    """Return new balance using compound annual interest. """
    return p*(1 + r)**t
    
def main():
    print("Calculates compound interest over time.")
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): " ))
    years = int(input("Years: " ))
    
    for year in range(years+1):
        print(year, balance(principal, rate, year))
    
main()


0 100.0
1 101.0
2 102.01
3 103.03010000000002
4 104.060401
5 105.10100501000001
6 106.15201506010001
7 107.21353521070101






