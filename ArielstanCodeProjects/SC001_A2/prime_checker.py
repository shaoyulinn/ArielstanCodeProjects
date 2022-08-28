"""
File: prime_checker.py
Name: Ariel
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program checks if the given input is a prime number or not.
	"""
	print('Welcome to the prime checker!')
	while True:
		data = int(input('n: '))
		a = 2
		# We use this variable to find factors of the input
		if data == -100:
			break
		remainder = data % a
		# If "remainder" equals zero and "a" equals "data",
		# the input is a prime number
		while remainder != 0:
			a += 1
			remainder = data % a
		if a != data:
			print(str(data)+' is not a prime number.')
		else:
			print(str(data)+' is a prime number.')
	print('Have a good one! ')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
