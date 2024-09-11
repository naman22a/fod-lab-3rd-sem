n = int(input("Enter n: "))

total = 0
for digit in str(n):
    total += int(digit)

print(total)