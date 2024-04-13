import math
def isPalindromeInteger(n):
    string = str(n)
    length = len(string)
    mid = math.floor(n / 2)

    for i in range(0, mid+1):
        if string[i] != string[length - 1 - i]:return False
        
    return True
