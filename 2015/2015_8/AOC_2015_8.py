import re

nCharInMemory = 0
nCharStringLiteral = 0
nEncodedChar = 0

def countMemoryChar(line):
    line = re.sub(r"\\x[0-9a-f]{2}", 'c', line)
    line = re.sub(r"\\\"", 'c', line)
    line = re.sub(r"\\{2}", 'c', line)
    return len(line)

def encondeLine(line):
    line = re.sub(r"\\", '\\\\\\\\', line)
    line = '"'+re.sub(r"\"", '\\\\\"', line)+'"'
    return len(line)

for line in open('2015\\2015_8\\input.txt', 'r'):
    line = line.strip().replace('\n', '').replace(' ', '')
    nCharStringLiteral += len(line)
    nCharInMemory += countMemoryChar(line[1:-1])
    nEncodedChar += encondeLine(line)
print(nCharStringLiteral - nCharInMemory)
print(nEncodedChar - nCharStringLiteral)