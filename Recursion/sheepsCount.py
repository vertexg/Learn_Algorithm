def sheeps(count):
    return sheepsHelper(count, "")

def sheepsHelper(count, string):
    if count <= 0: #ベースケース
        return string
    return sheepsHelper(count - 1, str(count) + " sheep ~ " + string)

print(sheeps(5))
print(sheeps(10))
