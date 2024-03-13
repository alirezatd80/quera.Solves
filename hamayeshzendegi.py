x , y = map(int , input().split())
if y <= 10:
    print('Right',(10-x)+1,y)
else:
    print('Left',(10-x)+1,(y-10)+1)