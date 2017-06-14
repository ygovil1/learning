import sys

digits = '0123456789'
args = sys.argv

def sum_digits(int):
	'''
	Funtion to sum the digits of the input of integer
	'''
	# create a string from the int
	word = '' + int
	
	# find sum by referring to the index of digits string
	sum = 0
	for dig in word:
		sum += digits.index(dig)
	return sum

# store first arg
first = int(args[0])

# if only one arg
if len(args) == 1:
	# loop until you reach square of input
	for x in range(1, first + 1):
		print(sum_digits(x*first))

# if 2 args 
elif len(args) == 2:
	for x in range(1, int(args[1]) + 1):
		if x%first==0:
			print(sum_digits(x*first)) 

# if not 1 or 2 args, return error
else:
	print('incorrect number of command line arguments')
