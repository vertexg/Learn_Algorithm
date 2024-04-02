#　わからなかったためもう一度復習

def reverseString(s):
    return reverseStringHelper(s[0], 1, s)

def reverseStringHelper(reversedString, index, originalString) :
    if index >= len(originalString): return reversedString
    return reverseStringHelper(originalString[index] + reversedString, index + 1, originalString)

print(reverseString("recursion")) # noisrucer
