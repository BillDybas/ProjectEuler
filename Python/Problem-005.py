#
# Solution to Problem 5: Smallest Multiple
# by Bill Dybas
#

def is_divisible(n):

    if not n % 11 == 0:
        return False

    # Divisible by 12 means also divisible by 3 and 4
    elif not n % 12 == 0:
        return False

    elif not n % 13 == 0:
        return False

    # Divisible by 14 means also divisible by 2 and 7
    elif not n % 14 == 0:
        return False

    # Divisible by 15 means also divisible by 3 and 5
    elif not n % 15 == 0:
        return False

    # Divisible by 16 means also divisible by 2, 4, and 8
    elif not n % 16 == 0:
        return False

    elif not n % 17 == 0:
        return False

    # Divisible by 18 means also divisible by 2, 3, 6, and 9
    elif not n % 18 == 0:
        return False

    elif not n % 19 == 0:
        return False

    # Divisible by 20 means also divisible by 2, 4, 5, and 10
    elif not n % 20 == 0:
        return False
    else:
        return True

def calculate():
    result = 1
    while not is_divisible(result):
        result += 1

    return result

if __name__ == '__main__':
    # Brute Force Method by checking divisibility
    print(calculate())

    # Could also note that:
    # Result = LCM({2..20})
    # Result = 2 * 3 * 2 * 5 * 7 * 3 * 11 * 13 * 2 * 17 * 19
