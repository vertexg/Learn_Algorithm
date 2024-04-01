import math
def totalSquareArea(x):
  if x <= 1: # ベースケース
    return 1
  return int(math.pow(x,3)) + totalSquareArea(x - 1)

print(totalSquareArea(3))
print(totalSquareArea(12))

