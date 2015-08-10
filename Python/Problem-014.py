#
# Solution to Problem 14: Longest Collatz sequence
# by Bill Dybas
#

def even_rule(n):
    # int'd because this will always evenly
    # divide and never produce floats
    return int(n / 2)

def odd_rule(n):
    return 3 * n + 1

def calculate():
    # Chain for '1' as default, as the for/while
    # loops won't properly find '1's chain if run at 1
    # (to guarantee full search coverage)
    longest_chain = [1, 4, 2, 1]

    # Run backwards, as the longest chains are presumed
    # to be at higher numbers
    for i in range(999999, 1, -1):
        chain = []
        current_number = i
        while current_number != 1:
            chain.append(current_number)
            if current_number % 2 == 0:
                current_number = even_rule(current_number)
            else:
                current_number = odd_rule(current_number)

        chain.append(1)
        if len(chain) > len(longest_chain):
            longest_chain = list(chain)

    print("Longest Chain @ {0}: {1}".format(longest_chain[0], longest_chain))

if __name__ == '__main__':
    calculate()
