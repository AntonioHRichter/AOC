input = 'vzbxkghb'

def firstRule(p):
    for c in p:
        if c in ('l', 'i', 'o'):
            return False
    return True

def removeCharFromFirsRule(p, pos):
    if pos == len(p) -1:
        return p
    if p[pos] in ('l', 'i', 'o'):
        p[pos] = chr(ord(p[pos]) + 1)
        p[pos+1:] = 'a'*(len(p)-pos-1)
        return p
    return removeCharFromFirsRule(p, pos+1)

def secondRule(p):
    pair = ''
    for i in range(0,len(p)-1):
        if len(pair) == 2:
            return True
        if p[i] == p[i+1] and p[i] not in pair:
            pair += p[i]
    return len(pair) == 2

def thirdRule(p):
    sec = ''
    for i in range(1, len(p)):
        if len(sec) == 2:
            return True
        sec = sec + p[i] if chr(ord(p[i]) - 1) == p[i-1] else ''
    return len(sec) == 2
    
def resolveResidue(p, r):
    if secondRule(p) and thirdRule(p):
        return p 
    if r == -8:
        p[r] = chr(ord(p[r]) + 1) if ord(p[r]) + 1 <= 122 else chr(97) 
        return p
    if ord(p[r]) + 1 <= 122:
        p[r] = chr(ord(p[r]) + 1)
        return p
    p[r] = chr(97)
    return resolveResidue(p, r-1)

def findNextPass(p):
    while not firstRule(p) or not secondRule(p) or not thirdRule(p):
        print(p)
        if ord(p[-1]) + 1 > 122:
            p = resolveResidue(p, -1)
        else:
            p[-1] = chr(ord(p[-1]) + 1)
        p = removeCharFromFirsRule(p, 0)
    return p


print(''.join(findNextPass(list(input))))