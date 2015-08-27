#
# Solution to Problem 20: Factorial Digit Sum
# by Bill Dybas
#

import math

def calculate():
    total = 0
    number = str(math.factorial(100))

    for i in number:
        total += int(i)

    return total

if __name__ == '__main__':
    print(calculate())
