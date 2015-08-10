#
# Solution to Problem 1: Multiples of 3 and 5
# by Bill Dybas
#

def calculate():
	multiples = []

	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			multiples.append(i)

	return sum(multiples)

if __name__ == '__main__':
	print(calculate())
