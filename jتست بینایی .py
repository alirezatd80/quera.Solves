numberletter = int(input())
textinput = input()
testuser= input()
j= 0
counter = 0
for i in textinput:
    if i != testuser[j]:
        counter+=1
        j+=1
    else:
        j+=1
print(counter)