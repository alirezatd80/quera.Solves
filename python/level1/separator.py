def separator(ls):
    evenlist = []
    oddlist = []
    resultlist=[]
    for i in ls:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
            
    resultlist.append(evenlist)
    resultlist.append(oddlist)
    result = tuple(resultlist)
    return result
