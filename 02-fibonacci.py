# TC: O(N)
# SC: O(1)
def fib(n):
    first = 0
    second = 1

    if(n == 1):
        print(first, end=' ')
        return
    if(n == 2):
        print(first, end=' ')
        print(second, end=' ')
        return
    
    print(first, end=' ')
    print(second, end=' ')

    for _ in range(n-2):
        next = first + second
        print(next, end= ' ')
        first = second
        second = next

def main():
    n = int(input("Enter n: "))
    fib(n)

if __name__ == '__main__':
    main()
