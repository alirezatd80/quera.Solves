number_test = int(input())
for i in range(number_test):
    a , b, h = map(int , input().split())
    higth = 0
    day = 1
    while( higth< h) :
        higth+=a
        if higth<h:
            higth-=b
            day+=1
        else:
            
            break
    print(day)