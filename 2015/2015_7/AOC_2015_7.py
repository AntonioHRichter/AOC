commands = {}
result = {}

for line in open('2015\\2015_7\\input.txt', 'r'):
    (op, signal) = line.replace('\n', '').split("->")
    commands[signal.strip()] = op.strip().split(' ')

def calculateSignal(wire):
    if len(commands[wire]) == 1:
        return findSignal(commands[wire][0])
    chooseWhatToDo(commands[wire])

def findSignal(wire):
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in result:
        if len(commands[wire]) == 1:
            signal = findSignal(commands[wire][0])
        else:
            signal = chooseWhatToDo(commands[wire])
        result[wire] = signal
    return result[wire]

def chooseWhatToDo(commands):
    match commands[1]:
        case 'AND':
            return findSignal(commands[0]) & findSignal(commands[2])
        case 'OR':
           return findSignal(commands[0]) | findSignal(commands[2])
        case 'LSHIFT':
            return findSignal(commands[0]) << findSignal(commands[2])
        case 'RSHIFT':
            return findSignal(commands[0]) >> findSignal(commands[2])
        case _:
            if commands[0] == 'NOT':
                return 65535 - findSignal(commands[1])
            else:
                return findSignal(commands[0])

print('part 1 answer: ',findSignal('a'))
commands.update({'b': ['16076']})
result = {}
print('part 2 answer: ',findSignal('a'))