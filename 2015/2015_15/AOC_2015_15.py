import itertools
from math import prod

ingredients = {}

def getScore(spoons):
    score = [0,0,0,0]
    for v in ingredients.values():
        spoon = spoons[v['id']]
        score[0] += spoon*v['capacity']
        score[1] += spoon*v['durability']
        score[2] += spoon*v['flavor']
        score[3] += spoon*v['texture']
    score = [0 if i < 0 else i for i in score]
    return prod(score)

def balanced(spoons, calories):
    if calories:
        tCalories = 0
        for v in ingredients.values():
            tCalories += spoons[v['id']]*v['calories']
        return sum(spoons) == 100 and tCalories == 500
    return sum(spoons) == 100

def cook(partTwo = False):
    score = 0
    comb = []
    per = itertools.product(range(1,100-len(ingredients)), repeat = len(ingredients))
    for i in list(per):
        if(balanced(i, partTwo)):
            tempS = getScore(i)
            if tempS > score:
                score = tempS
                comb = i
                print(score, comb, sep = ' | ')
    return score, comb

count = 0
for line in open('2015\\2015_15\\input.txt', 'r'):
  line = line.replace('.', '').replace(',','').strip().split(' ')
  ingredients[line[0]] = {line[1] : int(line[2]) ,line[3] : int(line[4]) ,line[5] : int(line[6]) ,line[7] : int(line[8]) ,line[9] : int(line[10]), 'id' : count}
  count += 1

print(cook(True))
