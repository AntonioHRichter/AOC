import re

instructions = []
register = {'a' : 0, 'b' : 0}

for line in open('2015\\2015_23\\input.txt'):
    offset, r = 0, ''
    if ',' in line:
        (i, offset) = line.strip().split(',')
        (i, r) = i.strip().split(' ')
    elif re.search(r'\d', line):
        (i, offset) = line.strip().split(' ')
    else: 
        (i, r) = line.strip().split(' ')
    instructions.append([i, r, int(offset)])

def runProgram():
    global register, instructions
    count = 0
    while count < len(instructions):
        offset = 0
        inst = instructions[count]
        match inst[0]:
            case 'hlf':
                if register[inst[1]] > 0:
                    register[inst[1]] = int(register[inst[1]]/2)
            case 'tpl':
                register[inst[1]] *= 3
            case 'inc':
                register[inst[1]] += 1
            case 'jmp':
                offset = inst[2]
            case 'jie':
                if register[inst[1]] % 2 == 0:
                    offset = inst[2]
            case 'jio':
                if register[inst[1]] == 1:
                    offset = inst[2]
        if offset == 0:
            count += 1
        else:
            count += offset

runProgram()
print(register)
register['a'] = 1
runProgram()
print(register)