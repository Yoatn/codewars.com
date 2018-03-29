import math

def zeros(n):
    a = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            a += 1
        if i == a ** 2:
            a += 1
    return a


while 1:
    x = int(input())
    print(zeros(x))
    print(math.factorial(x))

