"""
File: extension1_factorial.py
Name: Ariel
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program calculates the factorial of any given number.
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		factorial = 1
		a = 1
		# We use this variable to calculate the factorial
		number = int(input('Give me a number, and I will list the answer of factorial: '))
		if number == -100:
			break
		else:
			while a != number:
				a += 1
				factorial = factorial * a
			print('Answer: '+str(factorial))
	print('- - - - - - See ya! - - - - - -')


if __name__ == '__main__':
	main()