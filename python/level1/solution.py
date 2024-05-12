def calculator(n, m, li):
    result = 0
    counter = 0
    for i in range(n):
        if counter < m :
            result += li[i]
            counter += 1
        else: 
            result -= li[i]
            counter +=1
        if counter == m*2:
            counter =0
    return result


        
       
        
