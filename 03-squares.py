# TC: O(N)
# SC: O(N)
def squares():
    l = []
    for i in range(6, 30+1):
        l.append(i**2)
    return l

def main():
    l = squares()
    print(l)

if __name__ == '__main__':
    main()
