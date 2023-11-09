import re
summary = {}
answer = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

count = 1
for line in open('2015\\2015_16\\input.txt', 'r'):
    properties = {'children':-1, 'cats':-1, 'samoyeds':-1, 'pomeranians':-1, 'akitas':-1, 'vizslas':-1, 'goldfish':-1, 'trees':-1, 'cars':-1, 'perfumes':-1}
    line = re.sub(r'Sue \d*: ', '', line)
    line = line.strip().replace(' ','').split(',')
    for p in line:
        p = p.split(':')
        properties[p[0]] = int(p[1])
    summary[count] = properties
    count += 1

def findRealPercentage(properties):
    percentage = 0
    for k, p in properties.items():
        if p > -1:
            if k in ('cats', 'trees'):
                if answer[k] < p:
                    percentage += 1
            elif k in ('pomeranians', 'goldfish'):
                if answer[k] > p:
                    percentage += 1
            elif answer[k] == p :
                percentage += 1
    return (percentage/len(properties)) * 100

def findPercentage(properties):
    percentage = 0
    for k, p in properties.items():
        if answer[k] == p :
            percentage += 1
    return (percentage/len(properties)) * 100

def mFCSAM(partTwo = False):
    percentage = 0
    bestCandidates = ''
    for k,v in summary.items():
        tempP = findPercentage(v) if not partTwo else findRealPercentage(v)
        if tempP > percentage:
            percentage = tempP
            bestCandidates = k
    return bestCandidates, percentage

print(mFCSAM())