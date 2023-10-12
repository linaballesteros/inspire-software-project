def binADeci(bin4bits):
    decimalValue = 0
    base = 1

    for i in range(len(bin4bits) - 1, -1, -1):
        bitChar = bin4bits[i]
        bit = int(bitChar)
        
        decimalValue += bit * base
        base *= 2 

    return decimalValue

def decimalToBinary(decimalValue):
    binaryString = ""

    if decimalValue == 0:
        binaryString = "0"
    else:
        while decimalValue > 0:
            remainder = decimalValue % 2
            binaryString = str(remainder) + binaryString
            decimalValue = decimalValue // 2

    return binaryString

def getUnidades(decimalValue):
    digitoUnidades = decimalValue % 10
    return digitoUnidades

def getDecenas(decimalValue):
    digitoDecenas = (decimalValue // 10) % 10
    return digitoDecenas

def decimalToBinary1(decimalValue, bitLength):
    binaryString = ""
    
    while bitLength > 0:
        remainder = decimalValue % 2
        binaryString = str(remainder) + binaryString
        decimalValue = decimalValue // 2
        bitLength -= 1

    return binaryString




print(binADeci('1100'))
print(getUnidades(12))
print(getDecenas(12))
print(decimalToBinary1(1, 4))