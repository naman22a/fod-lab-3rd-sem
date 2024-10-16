a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

def maxi(a,b,c):
    if(a > b and a > c):
        return a
    if(b > a and b > c):
        return b
    return c

print("Max: ", maxi(a,b,c))
