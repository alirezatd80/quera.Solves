n = int(input())
k = int(input())
p = int(input())
q = int(input())
if n-k > p-q:
    print('Shekarestan')
elif n-k < p-q:
    print('Namakestan')
else:
    print('Equal')