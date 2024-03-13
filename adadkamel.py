def magsom(number):
    result = []
    for i in range(1,number):
        if number%i==0:
            result.append(i)
    return result
usernumber = int(input())
sumNumber = 0
for item in magsom(usernumber):
    sumNumber += item
if sumNumber == usernumber:
    print('YES')
else:
    print('NO')