a , b , c , d, m = map(int , input().split())
number1 =a+(c*m)
number2 =b+(d*m)
max  = max(number1,number2)
min = min(number1,number2)

if max-min > a+b:
    print('Eyval baba!')
else:
    print('Naaa, eshtebahe!')