'''
Enhanced Multiplication Table Generator
Lets the user print a multiplication table, starting at 1, for any number.
The user will specify the highest number to multiply by.
'''

def print_table(x, y):
    for i in range(1, int(y)+1):
        print('{:>2} x {:>2} = {:>3}'.format(x,i,(x*i)))

if __name__ == '__main__':
    print("Floating point numbers will be converted to integers.")
    print("Using very large numbers will break the formatting of the table.")
    try:
        num = int(input("Enter an integer to generate a multiplication table: "))
    except:
        exit("Input was not an integer. Please try again.")
    try:
        last = int(input("Enter the highest integer to multiply the number by: "))
    except:
        exit("Input was not an integer. Please try again.")
    print_table(num, last)