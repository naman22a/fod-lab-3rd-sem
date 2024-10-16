a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    result = None
else:
    print(result)
