# TC: O(N)
# SC: O(1)
def factorial_iteratively(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans

# TC: O(N)
# SC: O(N)
def factorial_recursively(n):
    if(n == 1 or n == 0):
        return 1
    return n*factorial_recursively(n-1)

# TC: O(N)
# SC: O(1)
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

def main():
    n = int(input("Enter n: "))
    print()
    print("Factorial(iteratively):", factorial_iteratively(n))
    print("Factorial(recursively):", factorial_recursively(n))
    print()
    print("Fibonacci series")
    fib(n)
    

if __name__ == '__main__':
    main()
