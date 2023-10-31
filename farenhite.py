from statistics import mean

def chomp(s):
    return s[:-1]


def c2f(c):
    return c * (9 / 5) + 32


def f2c(f):
    return (f - 32) * 5 / 9


if __name__ == '__main__':

    temps = []

    for _ in range(3):
        temp = float(chomp(input('enter temp in C  (e.g. 11C): ')))
        temps.append(temp)

    print(f'max temp: {max(temps)}C, or {c2f(max(temps))}')
    print(f'min temp: {min(temps)}C, or {c2f(min(temps))}')
    print(f'mean temp: {mean(temps)}C, or {c2f(mean(temps))}F')
