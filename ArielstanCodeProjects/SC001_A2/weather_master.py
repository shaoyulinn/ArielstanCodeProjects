"""
File: weather_master.py
Name: Ariel
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program analyzes the weather data entered,
	computes the highest, lowest, average temperatures
	and the number of cold days.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		total = float(data)
		average = float(data)
		numbers = 1
		if data < 16:
			cold = 1
		else:
			cold = 0
		# while loop
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			total = float(total + data)
			numbers += 1
			average = total / numbers
			if data < 16:
				cold += 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(average))
		print(str(cold)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
