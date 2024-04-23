def maxAscilString(stringList):
  maxValue = sumAscii(stringList[0])
  maxIndex = 0
  for a, b in enumerate(stringList):
        curr = sumAscii(b)
        if maxValue < curr:
           maxValue = curr
           maxIndex = a
  return maxIndex




def sumAscii(string):
    total = 0
    for a in string.lower():
        total += ord(a)
    return total


print(maxAscilString(["Fantastic","Bridge","Superior","Fantastic","Operator"]))
print(maxAscilString(["HeLlo","HelLo","bridge"]))
print(maxAscilString(["eatDjrPNbj","IehUUSEMVe","hpcbBvlTOc","egvnPZgyCh"]))
print(maxAscilString(["egvnPZgyCh","bridge","Fantastic"]))
