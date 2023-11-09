inputP = [2978,3083]

def getCoordinate(row, col):
    pos = col + row - 1
    return int(((pos/2) * (pos + 1) ) - (row - 1))

def getValue():
    v = 20151125
    for x in range(getCoordinate(inputP[0], inputP[1]) - 1):
        v *= 252533
        v = int(v) % 33554393
    return v

print(getValue())