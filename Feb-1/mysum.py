# mysum.py

def mysum(items):
    """ Return the sum of the values in items """
    total = 0
    for item in items:
        total += item 
    return total
    
def main():
    data = [4, 9, 2, 8, 3, 2, 5, 4, 2]
    print("Sum: ", sum(data))
    print("mysum: ", mysum(data))
    
main()
