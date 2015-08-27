#
# Solution to Problem 22: Name Scores
# by Bill Dybas
#

def calculate(names):
    total = 0

    for name in names:
        name_total = 0
        for ch in name:
            name_total += (ord(ch) - 64)
        total += (name_total * (names.index(name) + 1))

    return total

if __name__ == '__main__':
    filename = "p022_names.txt"

    with open(filename) as f:
        names = f.read().split(',')
        for n in names:
            names[names.index(n)] = n.replace("\"",'')
        names.sort()

        print(calculate(names))
