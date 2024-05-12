def calculate_floor(string):
    counter = 0
    for i in string:
        if i == 'U':
            counter+=1
        else:
            counter-=1
    return counter

