def fib(n):
    first = 0
    second = 1

    if(n <= 0):
        return

    if(n == 1):
        print(first, end=' ')
        return

    print(first, end=' ')
    print(second, end=' ')

    for _ in range(n-2):
        next = first + second
        print(next, end= ' ')
        first = second
        second = next

n = int(input("Enter n: "))
fib(n)