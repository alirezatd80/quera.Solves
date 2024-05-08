def numbersinlist(numbers:list ,x:int,y:int,z:int):
    for i in numbers:
        if i == [x,y,z] or i==[x,z,y] or i==[y,x,z] or i==[y,z,x] or i==[z,x,y] or i==[z,y,x]:
            return False
    return True
       


def Sumofnumbers(numinput):
    x = int(numinput/2)
    numbers = []
    counter = 0
    while(x>=numinput/3):
        i = int(numinput/2)
        while(i>=1):
        
            j = numinput-(i+x)
            if i+j+x == numinput and numbersinlist(numbers,i,j,x) and j!= 0 and j <= i and i+j >x and i+x > j and j+x > i :
                counter+=1
                littlelist = [i , j , x]
                numbers.append(littlelist) 
            i-=1   
                            
                            
                    
        x-=1
    return counter


numinput = int(input())
result = Sumofnumbers(numinput)
print(result)