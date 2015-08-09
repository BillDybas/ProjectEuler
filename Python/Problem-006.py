#
# Solution to Problem 6
# by Bill Dybas
#

def sum_of_squares(num):
    sum = 0

    for i in range(num + 1):
        sum += i**2

    return sum

def square_of_sum(num):
    return ((num*(num+1))/2)**2

if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_squares(100))
