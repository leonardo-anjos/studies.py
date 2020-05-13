import random


# 1
def convertC2F(c):
    return (9 / 5) * c + 32


print convertC2F(40), 'degrees Fahrenheit'


def convertF2C(f):
    return (5 * (f - 32)) / 9


print convertF2C(100), 'degrees convertF2C'


# 2
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


for i in range(1, 100):
    print i, "->", isPrime(i)


# 3
def breakList(l):
    return reduce(lambda x, y: x+y, l)


print breakList([['Geeks', 'For'], ['Geeks']])


# 4
def dic(d):
    print "sum:", sum(d.values()), "average:", sum(
        d.values())/len(d.values()), "round:", (round, d.values())


dic({'key1': 1, 'key2': 14, 'key3': 47})


# 5
def newWords(w):
    for l in w:
        print l


newWords("test")


# 6
def hard(d, k, r):
    print sorted(d, key=lambda tup: tup[1])


hard([
    ('a', 1),
    ('bit', 1),
    ('of', 1),
    ('butter', 2),
    ('but', 1),
    ('the', 1),
    ('was', 1),
    ('bitter', 1)
], 1, True)
