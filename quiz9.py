"""
Fibonacci Series:
                0 1 1 2 3 5 8 13 21 ...
"""


def fib_gen(number):
    result = 0
    n1, n2 = 0, 1
    for i in range(number):
        yield result
        result = n1 + n2
        n1, n2 = n2, result


def fac_gen(number):
    result = 1
    for i in range(number):
        result = result * (i + 1)
    yield result

num1 = int(input("Enter the number of which you want to find factorial: "))
fac = fac_gen(num1)
for i in fac:
    print(i)
num2 = int(input("Enter the number to which limit you want to see fibonacci series: "))
fab = fib_gen(num2)
for i in fab:
    print(i, end=" ")
