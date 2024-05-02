def isPangram(string):
    # キャッシュを作成
    cache = [0] * 26

    for i in string:
        list = ord(i.lower())
        if list >= 97 and list <= 122:
            cache[list - 97] = True
    return not min(cache) == False
