
class Node:
    _value = False
    _nextValue = False
    _tL = None
    _t = None
    _tR = None
    _l = None
    _r = None
    _dL = None
    _d = None
    _dR = None

    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)

    def __str__(self):
        return str([self.getTopLeft(), self.getTop(), self.getTopRight()]) +'\n'+'\t\t\t'+ (str([self.getLeft(), self.isOn(), self.getRight()]))+'\n'+'\t\t\t'+str([self.getBottomLeft(), self.getBottom(), self.getBottomRight()])
    
    def append(self, node, direction):
        match direction:
            case 'tL':
                self.topLeftAppend(node)
            case 't':
                self.topAppend(node)
            case 'tR':
                self.topRightAppend(node)
            case 'l':
                self.leftAppend(node)
            case 'r':
                self.rightAppend(node)
            case 'dL':
                self.bottomLeftAppend(node)
            case 'd':
                self.bottomAppend(node)
            case 'dR':
                self.bottomRightAppend(node)

    def rightAppend(self, node):
        if self._r == None and not node is None:
            self._r = node
            node.leftAppend(self)

    def leftAppend(self, node):
        if self._l == None and not node is None:
            self._l = node
            node.rightAppend(self)

    def topLeftAppend(self, node):
        if self._tL == None and not node is None:
            self._tL = node
            node.bottomRightAppend(self)

    def topAppend(self, node):
        if self._t == None and not node is None:
            self._t = node
            node.bottomAppend(self)

    def topRightAppend(self, node):
        if self._tR == None and not node is None:
            self._tR = node
            node.bottomLeftAppend(self)

    def bottomLeftAppend(self, node):
        if self._dL == None and not node is None:
            self._dL = node
            node.topRightAppend(self)
    
    def bottomAppend(self, node):
        if self._d == None and not node is None:
            self._d = node
            node.topAppend(self)

    def bottomRightAppend(self, node):
        if self._dR == None and not node is None:
            self._dR = node
            node.topLeftAppend(self)
   
    def step(self):
        count = 0
        if self._tL != None and self._tL.isOn():
            count+=1 
        if self._t != None and self._t.isOn():
            count+=1 
        if self._tR != None and self._tR.isOn():
            count+=1 
        if self._l != None and self._l.isOn():
            count+=1 
        if self._r != None and self._r.isOn():
            count+=1 
        if self._dL != None and self._dL.isOn():
            count+=1 
        if self._d != None and self._d.isOn():
            count+=1 
        if self._dR != None and self._dR.isOn():
            count+=1 
        self._nextValue = '#' if (self.isOn() and count in [2,3]) or (not self.isOn() and count == 3) else '.'

    def updateValue(self):
        self._value = self._nextValue
        return self._value

    def isOn(self):
        return self._value == '#'
    def setValue(self, value):
        self._value = value
        self._nextValue = value
    def getValue(self):
        return self._value
    def getTopLeft(self):
        return self._tL.isOn() if not self._tL is None else None
    def getTop(self):
        return self._t.isOn() if not self._t is None else None
    def getTopRight(self):
        return self._tR.isOn() if not self._tR is None else None
    def getLeft(self):
        return self._l.isOn() if not self._l is None else None
    def getRight(self):
        return self._r.isOn() if not self._r is None else None
    def getBottomLeft(self):
        return self._dL.isOn() if not self._dL is None else None
    def getBottom(self):
        return self._d.isOn() if not self._d is None else None
    def getBottomRight(self):
        return self._dR.isOn() if not self._dR is None else None

def getNode(y, x):
    if not isinstance(grid[y][x], Node):
        value = grid[y][x]
        grid[y][x] = Node(value)
    return grid[y][x]
    
def populateGrid(y, x, y2, x2, direction):
    global grid
    pos = getNode(y, x)
    tempN = getNode(y2, x2)
    pos.append(tempN, direction)
    grid[y2][x2] = tempN
    grid[y][x] = pos
    
def createGrid():
   for y, line in enumerate(grid):
    for x, pos in enumerate(grid[y]):
        chains = []
        if y > 0:
            chains.append((y-1, x, 't'))
            if x > 0:
                chains.append((y-1, x-1, 'tL'))
                chains.append((y, x-1 , 'l'))
            if x < len(grid[y]) - 1:
                chains.append((y-1, x+1, 'tR'))
        else:
            if x > 0:
                chains.append((y, x-1 ,'l'))
        for c in chains:
            populateGrid(y, x, c[0], c[1], c[2])

def printGridDebug():
    print()
    for i, y in enumerate(grid):
        for f, x in enumerate(y):
            print('(',i,f,')',' ->',x)
    print()

def printGrid():
    print()
    for y in grid:
        s = ''
        for x in y:
            s += x.getValue()
        print(s)
    print()

def takeAStep():
    count = 0
    for line in grid:
        for pos in line:
            pos.step()
    for line in grid:
        for pos in line:
            if pos.updateValue() == '#':
                count += 1
    return count

def takeSteps(steps, partTwo = False):
    for i in range(steps):
        if partTwo:
            print('number of lights : ',takeAStepWithouCorners())

        else:
            print('number of lights : ',takeAStep())
        printGrid()

def takeAStepWithouCorners():
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if (y,x) in ((0,0),(0,len(line)-1),(len(grid)-1, 0), (len(grid)-1,len(line)-1)):
                pos.setValue('#')
            else:
                pos.step()
    count = 0
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos.updateValue() == '#':
                count += 1
    return count

grid = []
for line in open('2015\\2015_18\\input.txt'):
    grid.append(list(line.strip()))

createGrid()
takeSteps(100)
takeSteps(100, True)

