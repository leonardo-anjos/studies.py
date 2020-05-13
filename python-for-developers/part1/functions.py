# fatorial implemented with recursion
def factorialRec(num):
    if num <= 1:
        return 1
    else:
        return(num * factorialRec(num - 1))


# print factorial(5)

# factorial without recursion
def factorialNoRec(n):
    n = n if n > 1 else 1
    j = 1

    for i in range(1, n + 1):
        j = j * i
    return j


# for i in range(1, 6):
#     print i, "->", factorialNoRec(i)


# fibonacci series with recursion
def fibRec(n):
    if n > 1:
        return fibRec(n - 1) + fibRec(n - 2)
    else:
        return 1


# for i in [1, 2, 3, 4, 5]:
#     print i, '=>', fib(i)


# fibonacci withou recursion
def fibNoRec(n):
    # the first two values
    l = [1, 1]

    # Calculating the others
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])

    return l[n]


for i in [1, 2, 3, 4, 5]:
    print i, '=>', fibNoRec(i)
