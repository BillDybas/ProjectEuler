#
# Solution to Problem 2: Even Fibonacci Numbers
# by Bill Dybas
#

def calculate(limit):
    sum = 0
    fib_1, fib_2 = 1, 2

    while fib_1 < limit:
        if fib_1 % 2 == 0:
            sum += fib_1

        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return sum

if __name__ == '__main__':
    print(calculate(4000000))
