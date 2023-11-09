import json

for line in open('2015\\2015_12\\input.json', 'r'):
    input_file = json.loads(line)
summary = []

class Node:
    _parent = None
    _depth = 0
    _data = None
    _child = None
    _active = True

    def __init__(self, data, parent, depth, red = False):
        self._data = data
        self._parent = parent
        self._depth = depth
        if red and self.isRed():
            self._active = False

    def __repr__(self):
        return str([self._data, self._parent, self._depth, self._active])

    def __str__(self):
        return str([self._data, self._parent, self._depth, self._active])

    def set_child(self, child):
        self._child = child

    def get_child(self):
        return self._child

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def isActive(self):
        return self._active

    def desactive(self):
        self._active = False

    def isRed(self):
        return isinstance(self._data, dict) and 'red' in self._data.values()   

def getParent(obj, depth):
    for item in summary:
        if item[0] == obj and item[1] == depth:
            return item[3]
    return None

def correctObj(obj, parent, depth):
    return obj if isinstance(obj, Node) else Node([*obj,], parent, depth) if isinstance(obj, tuple) else Node(obj, parent, depth)

def readJson(head):
    obj = Node(head, None, 0)
    depth = 0
    parent = None
    total = 0
    while obj.get_parent() is not None or obj.isActive() or depth < 0:
        obj = correctObj(obj, parent, depth)
        if isinstance(obj.get_data(), int) or isinstance(obj.get_data(), str) or not obj.isActive():
            total += (obj.get_data() if isinstance(obj.get_data(), int) else 0)
            obj = obj.get_parent()
            depth -= 1
            parent = obj.get_parent()
        else: 
            temp_obj = obj.get_data().popitem() if isinstance(obj.get_data(), dict) else obj.get_data().pop()
            if len(obj.get_data()) == 0:
                obj.desactive()
            parent = obj
            depth += 1
            obj = correctObj(temp_obj, parent, depth)
    return total

def isRed(obj):
    return isinstance(obj, dict) and 'red' in obj.values()
    

def removeRed(head):
    obj = Node(head, None, 0, True)
    depth = 0
    parent = None
    total = 0
    while obj.get_parent() is not None or obj.isActive() or depth < 0:
        if(not isRed(obj.get_data())):
            if isinstance(obj.get_data(), int) or isinstance(obj.get_data(), str) or not obj.isActive():
                total += (obj.get_data() if isinstance(obj.get_data(), int) else 0)
                obj = obj.get_parent()
                depth -= 1
                parent = obj.get_parent()
            else: 
                temp_obj = obj.get_data().popitem() if isinstance(obj.get_data(), dict) else obj.get_data().pop()
                if len(obj.get_data()) == 0:
                    obj.desactive()
                parent = obj
                depth += 1
                obj = correctObj(temp_obj, parent, depth)
        else:
            obj = obj.get_parent()
            depth -= 1
            parent = obj.get_parent()
    return total    

print(readJson(input_file))
print(removeRed(input_file))  
