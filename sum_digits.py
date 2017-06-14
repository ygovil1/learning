import sys

digits = '0123456789'

def sum_digits(int):
	word = '' + int
	
	sum = 0
	for dig in word:
		sum += digits.index(dig)

	return sum


