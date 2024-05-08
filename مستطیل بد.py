def numbersinlist(numbers:list ,x:int,y:int,z:int):
    for i in numbers:
        if i == [x,y,z] or i==[x,z,y] or i==[y,x,z] or i==[y,z,x] or i==[z,x,y] or i==[z,y,x]:
            return False
    return True
       


def Sumofnumbers(numinput):
    x = numinput-2
    numbers = []
    
    while(x>=1):
        for i in range(1 , int(numinput/2)+1):
            for j in range(i , int(numinput/2)+1):
                if i+j+x == numinput and numbersinlist(numbers,i,j,x):
                    littlelist = [i , j , x]
                    numbers.append(littlelist)    
                            
                            
                    
        x-=1
    return numbers


numinput = int(input())
result = Sumofnumbers(numinput)
counter = 0
for i in result:
    # print(i[0],i[1],i[2])
    if i[0]+i[1]>i[2]:
        if i[0]+i[2]>i[1]:
            if i[1]+i[2]> i[0]:
                counter+=1
print(counter)