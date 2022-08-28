"""
File: extension4_narcissistic_checker.py
Name: Ariel
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
    """
    This program checks if the given input is a narcissistic number or not.
    """
    print('Welcome to the narcissistic checker!')
    while True:
        data = int(input('n: '))
        a = 1
        # This variable represents the power of 10
        total = 0
        if data == EXIT:
            break
        else:
            while data > 10**a:
                a += 1
            power = a
            while a != 0:
                b = (data // 10**(a-1)) % 10
                total = total + b**power
                a -= 1
            if total == data:
                print(str(data)+' is a narcissistic number')
            else:
                print(str(data)+' is not a narcissistic number')
    print('Have a good one!')


if __name__ == '__main__':
    main()
