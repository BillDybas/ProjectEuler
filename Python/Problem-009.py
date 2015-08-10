#
# Solution to Problem 9
# by Bill Dybas
#

import math
guess = 500

def calculate():
    for i in range(1,guess):
        for j in range(i,guess):
                k = math.sqrt(i**2 + j**2)
                if i < j < k and i + j + k == 1000:
                    return i*j*k

if __name__ == '__main__':
    print(calculate())
