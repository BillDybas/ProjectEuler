#
# Solution to Problem 25: 1000-Digit Fibonacci Number
# by Bill Dybas
#

def calculate():
    nums = [1,1]
    i = 0
    while(len(str(nums[i] + nums[i+1])) < 1000):
        nums.append(nums[i] + nums[i+1])
        i += 1

    return len(nums) + 1

if __name__ == '__main__':
    print(calculate())
