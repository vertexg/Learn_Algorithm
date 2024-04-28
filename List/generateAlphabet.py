def generateAlphabet(firstAlphabet, secondAlphabet):
    # 各文字を文字コードに変換し、どちらがaに近い文字か判別。値が小さい方がaに近くなる。
    start = min(getAscii(firstAlphabet), getAscii(secondAlphabet))
    end = max(getAscii(firstAlphabet), getAscii(secondAlphabet))
    
    list = []

    # aに近い文字から順に配列へ格納
    for i in range(start, end + 1):
        # 文字コードを文字へ変換して、配列に格納
        list.append(chr(i))

    return list

def getAscii(char):
    # 文字列を小文字に変換して、文字コードへ変換
    return ord(char.lower())
