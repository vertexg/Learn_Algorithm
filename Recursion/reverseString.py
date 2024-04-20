#　わからなかったためもう一度復習

def reverseString(s):
    return reverseStringHelper(s[0], 1, s)

def reverseStringHelper(reversedString, index, originalString) :
    if index >= len(originalString): return reversedString
    return reverseStringHelper(originalString[index] + reversedString, index + 1, originalString)

print(reverseString("recursion")) # noisrucer


def reverseString(s):
  return reverseStringHelper(s, "")

def reverseStringHelper(s,string):
  if len(s)<= 0:
    return string
  return reverseStringHelper(s[:-1], string + s[-1])

print(reverseString("abcd"))



s[:-1]とs[-1:]の違い

s[:-1]:
最初の要素から最後の要素の一つ前までを取り出すことができる
例　s = "Hello"の場合、s[:-1]は"Hell"を返す

s[-1:]:
最後の要素のみを取り出す。
例　s = "Hello"の場合、s[-1:]は"o"を返す
