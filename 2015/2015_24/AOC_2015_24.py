import itertools
import math

presents = []

for line in open('2015\\2015_24\\input.txt'):
    presents.append(int(line.strip()))

def quantumEntanglement(smallestGroup):
    smallestQuantumEntanglement = -1
    for g in smallestGroup:
        if smallestQuantumEntanglement < 0 or math.prod(g) < smallestQuantumEntanglement:
            smallestQuantumEntanglement = math.prod(g)
    return smallestQuantumEntanglement

def biggestComb(groupSize):
    total = 0
    for i,p in enumerate(presents):
        total += p
        if total >= groupSize:
            return i+1
    return len(presents) - 1

def getCombinations(groupSize, compartments):
    combinations = []
    tempP = presents
    size, i = 0, 0
    while i < biggestComb(groupSize):
        for c in itertools.combinations(presents, i):
            if i > size and size > 0:
                return combinations
            tempP = presents
            if sum(c) == groupSize and not c in combinations:
                tempP = set(tempP) - set(c)
                if sum(tempP) / (compartments - 1) == groupSize:
                    size = i
                    combinations.append(c)
        i += 1
    return combinations

def arrangePresents(compartments):
    groupSize = sum(presents) / compartments
    return quantumEntanglement(getCombinations(groupSize, compartments))


print(arrangePresents(3))
print(arrangePresents(4))
