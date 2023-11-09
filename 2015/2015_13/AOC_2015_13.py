summary = {}

class Node:
    _name = ''
    _h = 0
    _hL = 0
    _hR = 0
    _pL = None
    _pR = None

    def __init__(self, name, hL = 0, hR = 0, pL = None, pR = None):
        self._name = name
        self._hL = hL
        self._hR = hR
        self._pL = pL
        self._pR = pR
        self._h = hL + hR

    def __repr__(self):
        return str([self._pL.get_name() if self._pL is not None else None,
             self._hL, self._name,self._hR, self._pR.get_name() if self._pR is not None else None])

    def __str__(self):
        return str([self._pL.get_name() if self._pL is not None else None,
             self._hL, self._name,self._hR, self._pR.get_name() if self._pR is not None else None])

    def sitLeft(self, h, p):
        self._hL = h
        self._pL = p
        self._h = self._hL + self._hR
        return h

    def sitRight(self, h, p):
        self._hR = h
        self._pR = p
        self._h = self._hL + self._hR
        return h

    def get_h(self):
        return self._h
    def get_name(self):
        return self._name
    def get_hL(self):
        return self.hL
    def set_hL(self, hL):
        self._hL = hL
    def get_hR(self):
        return self._hR
    def set_hR(self, hR):
        self._hR = hR
    def get_pL(self):
        return self._pL
    def set_pL(self, pL):
        self._pL = pL
    def get_pR(self):
        return self._pR
    def set_pR(self, pR):
        self._pR = pR
        

def findHappiness(people, sitter):
    for i in summary[people.get_name()]:
        if sitter.get_name() in i:
            return i[0]
    return 0

def findBestCandidate(people, sitted):
    totalHappiness = 0
    candidate = ''
    for c in summary[people]:
        for i in summary[c[1]]:
            if people in i:
                (totalHappiness, candidate) = (i[0] + c[0], c[1]) if ( i[0] + c[0] > totalHappiness or not bool(candidate)) and c[1] not in sitted else (totalHappiness, candidate)
                break
    return Node(candidate)

def sitPeople(people, sitted, result):
    if people.get_name() not in sitted:
        sitted.append(people.get_name())
        result.append(people)
    if people.get_pR() is None:
        sitNext = findBestCandidate(people.get_name(), sitted)
        if bool(sitNext.get_name()):
            result[0] += people.sitRight(findHappiness(people, sitNext), sitNext)
            result[0] += sitNext.sitLeft(findHappiness(sitNext, people), people)
            sitPeople(sitNext, sitted, result)
    if people.get_name() == sitted[-1]:
        result[0] += result[1].sitLeft(findHappiness(result[1], result[-1]), result[-1])
        result[0] += result[-1].sitRight(findHappiness(result[-1], result[1]), result[1])
    return result

def arrangeTable():
    totalHappiness = None
    for p in summary.items():
        sitted = []
        result = [0]
        result = sitPeople(Node(p[0]), sitted, result)
        totalHappiness = result[0] if totalHappiness is None or result[0] > totalHappiness else totalHappiness
    return totalHappiness

for line in open('2015\\2015_13\\input.txt', 'r'):
    (person, happiness) = line.split(' would ')
    (happiness, nextTo) = happiness.strip().replace('.','').split(' to ')
    happiness = int(happiness.split(' ')[1]) if 'gain' in happiness else int(happiness.split(' ')[1]) * -1
    if person not in summary:
        summary[person] = [[happiness, nextTo]]
    else:
        summary[person].append([happiness, nextTo])

print(arrangeTable())