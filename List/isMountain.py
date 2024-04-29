わからなかったためもう一度復習
def isMountain(height):
    l = len(height)
    if l <= 0 or height[0] > height[1]: return False

    # 最大値・最小値・インデックスの初期値
    maxVal = -float('inf')
    minVal = float('inf')
    i = 0

    # 昇順が終わるまで処理を繰り返します
    while i < l and height[i] > maxVal:
        maxVal = height[i]
        i += 1

    # 昇順のみの配列の場合、falseを返します
    if i == l or max == height[i]: return False

    # 降順が終わるまで処理を繰り返します
    while i < l and height[i] < minVal:
        minVal = height[i]
        i += 1

    # 配列の末尾まで降順が続いていなかったらfalseを返します
    return i == l
