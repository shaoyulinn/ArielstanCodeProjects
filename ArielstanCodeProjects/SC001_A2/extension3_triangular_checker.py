"""
File: extension3_triangular_checker.py
Name: Ariel
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
    """
    This program checks if the given input is a triangular number or not.
    """
    print('Welcome to the triangular number checker!')
    while True:
        data = int(input('n: '))
        a = 1
        if data == EXIT:
            break
        else:
            # If the double of "data" can be calculates by two consecutive numbers multiplied,
            # the input is a triangular number
            while a * (a+1) < data * 2:
                if a * (a+1) != data * 2:
                    a += 1
            if a * (a+1) == data * 2:
                print(str(data)+' is a triangular number')
            else:
                print(str(data)+' is not a triangular number')
    print('Have a good one!')


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
