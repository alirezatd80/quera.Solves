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

number = "27711"
mylist = set(sorted(Jaygasht(number)))
numberslist = sorted(list(mylist))
i = numberslist.index(int(number))
print(numberslist[i+1])