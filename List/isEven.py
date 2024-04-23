整数の配列 listOfInts を入力として受け取り、偶数が何個あるかを調べる totalEven という関数を作成
def isEven(n):
    return n % 2 == 0

def countEven(listOfInts):
    count = 0
    for i in range(0, len(listOfInts)):
        if isEven(listOfInts[i]):
            count += 1
    return count

list1 = [3,43,5,4,2,100,6]
print(countEven(list1))
