def Even(number):
    if number%2 == 0:
        return True
    else:
        return False


def separator(ls):
    evenlist = []
    oddlist = []
    resultlist=[]
    for i in ls:
        if Even(i):
            evenlist.append(i)
        else:
            oddlist.append(i)
            
    resultlist.append(evenlist)
    resultlist.append(oddlist)
    return resultlist
    
