#
# Solution to Problem 4
# by Bill Dybas
#

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def calculate():
    largest = 0

    for a in range(100, 1000):
        for b in range(100, 1000):
            if is_palindrome(a * b) and a * b > largest:
                largest = a * b

    return largest

if __name__ == '__main__':
    print(calculate())
