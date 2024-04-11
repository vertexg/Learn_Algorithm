def notDivisibleNumbers(x,y):
    string = ''
    for i in range(1,x+1):
        if i % y != 0: string += str(i) + '-'
        
    return string[0:len(string) - 1]
