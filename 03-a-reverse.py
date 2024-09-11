s = input("Enter a string: ")
r = ''
for c in s:
    r = c + r
print(r)

s = input("Enter a string: ")
i = 0
r = ''
while(i < len(s)):
    c = s[i]
    r = c + r;
    i += 1
print(r)

