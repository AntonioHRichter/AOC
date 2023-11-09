summary = {}

def whoIsWinning():
    winner = [0]
    for key, rein in summary.items():
        if rein['point'] > winner[0]:
            winner = [rein['point'], key]
        elif rein['point'] == winner[0]:
            winner.append(key)
    return winner
    
def pontuate(sW):
    for w in sW:
        temp = summary[w]
        temp['point'] += 1
        summary[w] = temp

def race():
    wD = 0
    sW = []
    for key, rein in summary.items():
        if rein['stamina'] == 0:
            rein['stamina'] = rein['t_stamina'] if rein['rest'] == 1 else rein['stamina']
            rein['rest'] -= 1
        else:
            rein['distance'] += rein['speed']
            rein['stamina'] -= 1
            rein['rest'] = rein['t_rest']
        if rein['distance'] > wD:
            wD = rein['distance']
            sW = [key]
        elif rein['distance'] == wD:
            sW.append(key)
    return sW

def secondRace():
    for i in range(0, 2503): 
        pontuate(race())
    return whoIsWinning()


def fly(reindeer):
    i = 0
    distance = 0
    reindeer = summary[reindeer]
    while i <= 2503:
        if reindeer['stamina'] == 0:
            reindeer['stamina'] = reindeer['t_stamina']
            i += reindeer['t_rest']
        else:
            distance += reindeer['speed']
            reindeer['stamina'] -= 1
            i += 1
    return distance

def beginRace():
    distance = 0
    for reindeer in summary.keys():
        tempD = fly(reindeer)
        distance = tempD if tempD > distance else distance
    return distance

    
for line in open('2015\\2015_14\\input.txt'):
    line = line.strip().split(' ')
    (reindeer, speed, stamina, rest) = [n for i, n in enumerate(line) if i in (0, 3, 6, 13)]
    summary[reindeer] = {'speed': int(speed), 't_stamina': int(stamina), 'stamina': int(stamina), 't_rest': int(rest), 'rest': int(rest), 'distance': 0, 'point': 0}

print(beginRace())
print(secondRace())