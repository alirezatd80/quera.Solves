def Jaygasht(num, jomle="", numbers=None):
    if numbers is None:
        numbers = []

    if len(num) == 0:
        numbers.append(int(jomle))
        return 
    
    for i in range(len(num)):
        adadentekhbi = num[i]
        edame = num[:i] + num[i+1:]
        Jaygasht(edame, jomle + adadentekhbi, numbers)
    
    return numbers

number = str(input())
mylist = set(sorted(Jaygasht(number)))
numberslist = sorted(list(mylist))
i = numberslist.index(int(number))
if i+1 == len(numberslist):
    print(0)
else:
    print(numberslist[i+1])