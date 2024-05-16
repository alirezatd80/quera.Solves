numberjoice , V = map(int , input().split())
dic = {}
for i in range(numberjoice):
    happy , hajm = map(int , input().split())
    dic[i] = [happy,hajm]
    
print(dic)