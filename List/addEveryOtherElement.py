def addEveryOtherElement(intArr):
    num = 0
    for i in range(0, len(intArr), 2): 
        num += intArr[i]
    return num
