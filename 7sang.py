sangList = list(map(int,input().split()))
wichsang = int(input())
for i in sangList:
    if i == wichsang:
        result = 7-sangList.index(wichsang)
        if result == 7 :
            print(6)
        else:
            print(result)