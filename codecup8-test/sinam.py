number_employe , size_cinema = map(int,input().split())
list_employe = []
list_employe = map(int , input().split(' '))
list_employe = list(map(lambda x:x+1 , list_employe))
list_employe.sort()
number_go = 0
i =0 
while(size_cinema>0 and i <number_employe):
    if size_cinema >= list_employe[i]:
        size_cinema-=list_employe[i]
        i+=1
        number_go+=1
    else:
        i+=1
    
print(number_go)
