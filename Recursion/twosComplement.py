非常に難しいため明日もう一度復習

def twosComplement(bits):
    twosComplement = onesComplement(bits)
    carryOut = False

    for i in reversed(range(0, len(twosComplement))):
        if twosComplement[i] == '0':
            twosComplement = twosComplement[:i] + '1' + twosComplement[i + 1:]
            carryOut = False
            break

        elif twosComplement[i] == '1':
            twosComplement = twosComplement[:i] + '0' + twosComplement[i + 1:]
            carryOut = True
    return '1' + twosComplement if carryOut else twosComplement

def onesComplement(bists):
    onesComplement = ''
    for b in bists:
        if b == '1':
            onesComplement += '0'
        else:
            onesComplement +='1'
    return onesComplement
