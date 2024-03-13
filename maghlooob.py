def magloob(number):
    strnumber = str(number)
    return(strnumber[::-1])

number =int(input())
maglobnum =int(magloob(number))
if number == maglobnum :
    print("YES")
else:
    print('NO')


