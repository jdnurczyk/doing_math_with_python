'''
Even/Odd Vending Machine
This will:
1. Print whether the number is even/odd.
2. Display that number with the next 9 similar (i.e. even or odd) numbers.
3. Display an error message if a float is input.
First exercise
'''

def is_even(n):
    if n % 2 == 0:
        print('Even')
    else:
        print('Odd')

def print_nums(n):
    for i in range(n,(n+20),2):
        print(i)

if __name__ == '__main__':
    end_test = True
    num = 0
    while end_test:
        num = input('Even/Odd Vending Machine! Enter an integer: ')
        end_test = not float(num).is_integer()

    is_even(int(num))
    print_nums(int(num))