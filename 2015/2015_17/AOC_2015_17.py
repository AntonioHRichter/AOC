from itertools import combinations, permutations


containers = []
answers = []

for line in open('2015\\2015_17\\input.txt'):
    containers.append(int(line.strip()))
containers.sort(reverse=True)

def smallestComb(quant):
    total = 0
    tempC = containers
    tempC.sort()
    for i, c in enumerate(tempC):
        total += c
        if total > quant:
            return i+1

def biggestComb(quant):
    total = 0
    tempC = containers
    tempC.sort(reverse=True)
    for i, c in enumerate(tempC):
        total += c
        if total > quant:
            return i+1
        

def findComb(quant):
    for i in range(biggestComb(quant), smallestComb(quant)):
        for c in combinations(containers, i):
            if sum(c) == quant:
                answers.append(c)
    return answers

def findCombPartTwo(quant):
    for c in combinations(containers, biggestComb(quant)):
        if sum(c) == quant:
            answers.append(c)
    return answers


print(len(findComb(150)))
answers = []
print(len(findCombPartTwo(150)))