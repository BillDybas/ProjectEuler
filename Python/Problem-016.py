#
# Solution to Problem 16: Power Digit Sum
# by Bill Dybas
#

def calculate():
    long_number = str(2**1000)

    total = 0
    for i in long_number:
        total += int(i)

    return total

if __name__ == '__main__':
    print(calculate())
