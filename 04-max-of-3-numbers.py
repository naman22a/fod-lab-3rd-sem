# TC: O(1)
# SC: O(1)
def max_of_three(a, b, c):
    if a > b and a > c :
        return a
    if b > a and b > c :
        return b
    return c


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    print("Max:", max_of_three(a, b, c))

if __name__ == '__main__':
    main()
