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

def main():
    n = int(input("Enter n: "))
    print(factorial_iteratively(n))
    print(factorial_recursively(n))

if __name__ == '__main__':
    main()
