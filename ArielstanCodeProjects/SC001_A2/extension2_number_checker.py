"""
File: extension2_number_checker.py
Name: Ariel
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
    """
    The program checks the input is a
    perfect, abundant, or deficient number.
    """
    print('Welcome to the number checker!')
    while True:
        data = int(int(input('n: ')))
        a = 1
        # We use this variable to find factors of the input
        total = 1
        if data == EXIT:
            break
        while a != data:
            a += 1
            remainder = data % a
            if remainder == 0:
                total = total + a
        total -= data
        # This variable represents the sum of all the factors except the input itself
        if total == data:
            print(str(data)+' is a perfect number')
        elif total > data:
            print(str(data)+' is an abundant number')
        else:
            print(str(data)+' is a deficient number')
    print('Have a good one!')


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
