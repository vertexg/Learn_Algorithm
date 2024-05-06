def oneComplement(bits):
    answer = ''
    for i in range(len(bits)):
        answer += "1"if bits[i] == "0" else "0"
    return answer
