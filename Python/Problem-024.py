#
# Solution to Problem 24: Lexicographic Permutations
# by Bill Dybas
#

import itertools

def calculate():
    p = itertools.permutations(range(10))
    j = 1
    for i in p:
        if j == 1000000:
            return i
        else:
            j += 1

if __name__ == '__main__':
    print(calculate())
