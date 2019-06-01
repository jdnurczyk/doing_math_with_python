'''
Enhanced Multiplication Table Generator
Lets the user print a multiplication table, starting at 1, for any number.
The user will specify the highest number to multiply by.
'''

def print_table(x, y):
    for i in range(1, int(y)+1):
        print('{:>2}  x {:>2} = {:>3}'.format(x,i,(x*i)))

if __name__ == '__main__':
    num = int(input("Enter the number to generate a multiplication table: "))
    last = int(input("Enter the highest number to multiply the number by: "))
    print_table(num, last)