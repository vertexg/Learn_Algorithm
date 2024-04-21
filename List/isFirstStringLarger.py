わからなかったためもう一度復習
def isFirstStringLarger(s1,s2):
    # 2つの文字列を文字コードに変換し、どちらが大きいか比べます
    return getAscii(s1) > getAscii(s2)

# 文字を文字コードに変換する関数
def getAscii(string):
    sumOfAscii = 0
    # 文字列を小文字に変換し、1文字ずつ文字コードへ変換します
    for char in string.lower():
        # 文字コードを足していきます
        sumOfAscii += ord(char)
    return sumOfAscii

print(isFirstStringLarger("Fantastic","Bridge"))
