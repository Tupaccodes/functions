def char_stats(s):

    upper = 0
    lower = 0

    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

        return upper, lower


if __name__ == '__main__':

    s = input('enter a string: ')

    up, low = char_stats(s)

    print(f'upper: {up}, lower: {low}.')