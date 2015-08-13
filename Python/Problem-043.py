#
# Solution to Problem 43: Sub-string Divisibility
# by Bill Dybas
#

import itertools

def is_pandigital(number):
    if "1" in str(number) and "2" in str(number) and "3" in str(number) \
        and "4" in str(number) and "5" in str(number) and "6" in str(number) \
        and "7" in str(number) and "8" in str(number) and "9" in str(number):
        return True
    else:
        return False

def is_divisible(number):
    if int(str(number)[1:4]) % 2 == 0 \
        and int(str(number)[2:5]) % 3 == 0 \
        and int(str(number)[3:6]) % 5 == 0 \
        and int(str(number)[4:7]) % 7 == 0 \
        and int(str(number)[5:8]) % 11 == 0 \
        and int(str(number)[6:9]) % 13 == 0 \
        and int(str(number)[7:10]) % 17 == 0:
        return True
    else:
        return False

def calculate():
    permutations = itertools.permutations('1023456789', 10)
    total = 0

    for i in permutations:
        num = int(''.join(i))
        if is_pandigital(num) and is_divisible(num):
            total += num

    return total

if __name__ == '__main__':
    print(calculate())
