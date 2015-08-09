#
# Solution to Problem 1
# by Bill Dybas
#

def calculate():
	multiples = []

	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			multiples.append(i)

	print(sum(multiples))

if __name__ == '__main__':
	calculate()
