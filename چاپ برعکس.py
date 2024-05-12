numbers = []
while(0 not  in numbers ):
    numbers.append(int(input()))
numbers.remove(0)
for i in reversed(numbers):
    print(i)