example = 'codecup6'
numUser = int(input())
if numUser <= 8 :
    i = int(numUser-1)
    print(example[i])
else:
   
    while(numUser>8):
        numUser = numUser-8
    i = int(numUser-1)
    print(example[i])