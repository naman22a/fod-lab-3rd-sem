with open('05-file.txt') as f:
    content = f.read()
    print(content)

with open('05-file.txt', 'w') as f:
    f.write('Hello world')
