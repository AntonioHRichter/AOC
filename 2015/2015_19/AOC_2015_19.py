import itertools
import re 

replacements = {}
molecule = ''
moleculeCalibration = []

for line in open('2015\\2015_19\\input.txt'):
    if '>' in line:
        (name, value) = line.strip().split(' => ')
        if name in replacements:
            replacements[name].append(value)
        else:
            replacements[name] = [value]
    else:
        molecule += line.strip()

def replaceCalibrator(k, v):
    for r in re.finditer(k, molecule):
        pos = r.span()
        tempM = molecule[:pos[0]] + v + molecule[pos[1]:]
        if tempM != molecule and not tempM in moleculeCalibration:
            moleculeCalibration.append(tempM)

def moleculeCalibrator():
    for k, values in replacements.items():
        for v in values:
            replaceCalibrator(k, v)

def quantRnAr():
    return len([i for i in re.finditer('Ar', molecule)]) + len([i for i in re.finditer('Rn', molecule)])

def quantY():
    return len([i for i in re.finditer('Y', molecule)])

def getElements():
    tempM = molecule
    return len(re.sub(r'[a-z]', '' ,tempM.replace('Ar', ')').replace('Rn', '(').replace('Y', ',')))

def calculateSecondPart():
    return getElements() - quantRnAr() - (2*quantY()) - 1


moleculeCalibrator()
print(len(moleculeCalibration))
print(calculateSecondPart())
