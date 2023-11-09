import re
import math
import itertools
bossStats = []
shop = {}

for line in open('2015\\2015_21\\shop.txt'):
    line = ' '.join(line.strip().split())
    if ':' in line:
        category, stats = line.strip().split(': ')
        stats = stats.split(' ')
    else:
        if not category in shop:
            shop[category] =[{'Cost' : 0, 'Damage' : 0, 'Armor' : 0}]
        if category == 'Rings':
            (eType, quality, cost, damage, armor) = line.strip().split(' ')
            shop[category].append({stats[0]: int(cost), stats[1]: int(damage), stats[2]: int(armor)})
        else:
            (eType, cost, damage, armor) = line.strip().split(' ')
            shop[category].append({stats[0]: int(cost), stats[1]: int(damage), stats[2]: int(armor)})

for line in open('2015\\2015_21\\input.txt'):
    bossStats.append(int(line.strip().split(': ')[1]))

def playerWon(hp, damage, armor):
    dmgTaken = bossStats[1] - armor
    dmgDelt = damage - bossStats[2]
    roundsToDie = math.ceil(hp / (1 if dmgTaken <= 0 else dmgTaken)) 
    roundsToKill = math.ceil(bossStats[0] / (1 if dmgDelt <= 0 else dmgDelt))
    return roundsToDie - roundsToKill >= 0

def createIterations():
    return itertools.product([*range(1,6)], [*range(0,6)], [*range(0,7)], [*range(0,7)])

def gearUp(equipment):
    cost = shop['Weapons'][equipment[0]]['Cost']
    cost += shop['Armor'][equipment[1]]['Cost']
    cost += shop['Rings'][equipment[2]]['Cost']
    cost += shop['Rings'][equipment[3]]['Cost']
    damage = shop['Weapons'][equipment[0]]['Damage']
    damage += shop['Armor'][equipment[1]]['Damage']
    damage += shop['Rings'][equipment[2]]['Damage']
    damage += shop['Rings'][equipment[3]]['Damage']
    armor = shop['Weapons'][equipment[0]]['Armor']
    armor += shop['Armor'][equipment[1]]['Armor']
    armor += shop['Rings'][equipment[2]]['Armor']
    armor += shop['Rings'][equipment[3]]['Armor']
    return cost, damage, armor

def testItens(hp):
    price = -1
    for i in createIterations():
        if i[-1] != i[-2] or i[-1] == 0:
            tempC, damage, armor = gearUp(i)
            if playerWon(hp, damage, armor) and (tempC < price or price < 0):
                price = tempC
    return price

def testItensTwo(hp):
    price = -1
    for i in createIterations():
        if i[-1] != i[-2] or i[-1] == 0:
            tempC, damage, armor = gearUp(i)
            if not playerWon(hp, damage, armor) and tempC > price:
                price = tempC
    return price


print(testItens(100))
print(testItensTwo(100))

