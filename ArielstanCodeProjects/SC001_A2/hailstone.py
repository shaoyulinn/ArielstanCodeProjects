"""
File: hailstone.py
Name: Ariel
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program shows the process of Hailstone Sequence of any given number,
    and counts all the steps it needs to take simultaneously.
    """
    print('This program computes Hailstone sequences.')
    print('')
    n = int(input('Enter a number: '))
    steps = 0
    while True:
        remainder = n % 2
        # This variable helps distinguish odd from even
        if n == 1:
            break
        else:
            if remainder != 0:
                next_n = 3*n + 1
                print(str(n)+' is odd, so I make 3n+1: '+str(next_n))
                steps += 1
            else:
                next_n = n // 2
                print(str(n)+' is even, so I take half: ' + str(next_n))
                steps += 1
            n = next_n
    print('It took '+str(steps)+' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
