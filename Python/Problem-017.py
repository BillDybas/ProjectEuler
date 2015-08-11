#
# Solution to Problem 17: Number Letter Counts
# by Bill Dybas
#

def digit_to_word(n):
    if n == 0:
        return ""
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"

def tens_to_word(n):
    m = n % 10
    if n < 10:
        return digit_to_word(m)
    elif n < 20:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 14:
            return "fourteen"
        elif n == 15:
            return "fifteen"
        elif n == 16:
            return "sixteen"
        elif n == 17:
            return "seventeen"
        elif n == 18:
            return "eighteen"
        elif n == 19:
            return "nineteen"
    elif n < 30:
        return "twenty" + digit_to_word(m)
    elif n < 40:
        return "thirty" + digit_to_word(m)
    elif n < 50:
        return "forty" + digit_to_word(m)
    elif n < 60:
        return "fifty" + digit_to_word(m)
    elif n < 70:
        return "sixty" + digit_to_word(m)
    elif n < 80:
        return "seventy" + digit_to_word(m)
    elif n < 90:
        return "eighty" + digit_to_word(m)
    elif n < 100:
        return "ninety" + digit_to_word(m)

def hundreds_to_word(n):
    o = n % 100

    if n >= 100:
        num = digit_to_word(int(str(n)[-3])) + "hundred"
        if o != 0:
            num += "and" + tens_to_word(o)

        return num
    else:
        return tens_to_word(n)

def thousands_to_word(n):
    p = n % 1000

    if n >= 1000:
        num = digit_to_word(int(str(n)[-4])) + "thousand"
        if p != 0:
            num += hundreds_to_word(p)

        return num
    else:
        return hundreds_to_word(n)

def calculate():
    total = 0
    for i in range(1,1001):
        total += len(thousands_to_word(i))

    return total

if __name__ == '__main__':
    print(calculate())
