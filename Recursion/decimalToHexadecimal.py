//わからなかったためもう一度復習

import math
def decimalToHexadecimal(decNumber):
  list = "0123456789ABCDEF"
  answer = ''
  binary = 0

  while decNumber >= 0:
    binary = decNumber % 16
    answer = list[binary] + answer
    decNumber = math.floor(decNumber / 16)

    if decNumber == 0: break

  return answer
