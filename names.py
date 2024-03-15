numberOfName =int(input())
max = 0
for i in range(numberOfName):
    name = input()
    myset = set(name)
    if len(myset) > max:
        max = len(myset)
print(max)
