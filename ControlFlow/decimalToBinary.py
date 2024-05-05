import math
def decimalToBinary(decNumber):
  answer = ''
  binary = 0

  while decNumber >= 0:
    binary = decNumber % 2
    answer = str(binary) + answer
    decNumber = math.floor(decNumber / 2)

    if decNumber == 0: break

  return answer
print(decimalToBinary(2))
