# mymax2.py
# Write max function without build-in max()

def mymax2(x, y):
    """ Return larger of x and y. """
    largest_so_far = x
    if y > largest_so_far:
        largest_so_far = y
        
    return largest_so_far
    
def main():
    print("MyMax: Enter two values to find the larger.")
    first = float(input("First value: "))
    second = float(input("Second value: "))
    
    larger = mymax2(first, second)
    print("The larger value is: ", larger)
    
main()
