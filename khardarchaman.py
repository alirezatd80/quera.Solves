a,b,l = map(int,input().split())
time = 0
result = 0
while(time != l ):
    result+= a
    time +=1
    if time != l:
        result+=b
        time +=1
print (result)