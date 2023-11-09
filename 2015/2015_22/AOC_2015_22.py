import random 

attacks = {'M' : {'Cost' : 53, 'EffectType' : 'Damage', 'Timer' : 0, 'Effect' : 4},
    'D' : {'Cost' : 73, 'EffectType' : 'Damage Heal', 'Timer' : 0, 'Effect' : 2},
    'S' : {'Cost' : 113, 'EffectType' : 'Armor', 'Timer' : 6, 'Effect' : 7},
    'P' : {'Cost' : 173, 'EffectType' : 'Damage', 'Timer' : 6, 'Effect' : 3},
    'R' : {'Cost' : 229, 'EffectType' : 'Mana', 'Timer' : 5, 'Effect' : 101} }

bossStats = {}
playerStats = {}
spellTimers = {'S' : 0, 'P': 0, 'R': 0}
manaSpent = 0
debug = True
actions = []

def resetGame():
    global bossStats, playerStats, spellTimers, manaSpent, actions
    bossStats = {'hp' : 71, 'damage' : 10}
    playerStats = {'hp' : 50, 'mana' : 500, 'armor' : 0}
    spellTimers = {'S' : 0, 'P': 0, 'R': 0}
    actions = []
    manaSpent = 0

def spellAvailble():
    for k,a in attacks.items():
        if (not k in spellTimers or spellTimers[k] == 0) and playerStats['mana'] - a['Cost'] >= 0:
            return True
    return False

def resolveTimers():
    if spellTimers['S'] > 0:
        spellTimers['S'] -= 1
        if spellTimers['S'] == 0:
            playerStats['armor'] -= attacks['S']['Effect']
    if spellTimers['P'] > 0:
        bossStats['hp'] -= attacks['P']['Effect']
        spellTimers['P'] -= 1
    if spellTimers['R'] > 0:
        playerStats['mana'] += attacks['R']['Effect']
        spellTimers['R'] -= 1

def fightEnded():
    return bossStats['hp'] <= 0 or playerStats['hp'] <= 0 or playerStats['mana'] <= 0

def bossTurn():
    resolveTimers()
    if not fightEnded():
        dmgTaken = bossStats['damage'] - playerStats['armor']
        playerStats['hp'] -= dmgTaken if dmgTaken > 0 else 1

def castSpell():
    global manaSpent
    while True: 
        spell = 'MDSPR'[random.randrange(0,5)]
        if (not spell in spellTimers or spellTimers[spell] == 0) and playerStats['mana'] - attacks[spell]['Cost'] >= 0:
            match spell:
                case 'M':
                    playerStats['mana'] -= attacks[spell]['Cost']
                    bossStats['hp'] -= attacks[spell]['Effect']
                    manaSpent += attacks[spell]['Cost']
                    break
                case 'D':
                    playerStats['mana'] -= attacks[spell]['Cost']
                    bossStats['hp'] -= attacks[spell]['Effect']
                    playerStats['hp'] += attacks[spell]['Effect']
                    manaSpent += attacks[spell]['Cost']
                    break
                case 'S':
                    playerStats['mana'] -= attacks[spell]['Cost']
                    playerStats['armor'] += attacks[spell]['Effect']
                    spellTimers[spell] = attacks[spell]['Timer']
                    manaSpent += attacks[spell]['Cost']
                    break
                case 'P':                
                    playerStats['mana'] -= attacks[spell]['Cost']
                    spellTimers[spell] = attacks[spell]['Timer']
                    manaSpent += attacks[spell]['Cost']
                    break
                case 'R':
                    playerStats['mana'] -= attacks[spell]['Cost']
                    spellTimers[spell] = attacks[spell]['Timer']
                    manaSpent += attacks[spell]['Cost']
                    break
        elif not spellAvailble():
            playerStats['mana'] = 0
            break
    actions.append(spell)

def start(partTwo = False):
    global manaSpent, actions
    smallestMana = 0
    bestAction = []
    for i in range(20000000):
        resetGame()
        while not fightEnded():
            if partTwo:
                playerStats['hp'] -= 1
            resolveTimers()
            castSpell()
            if manaSpent >= smallestMana and smallestMana > 0:
                manaSpent = -1
                break;
            bossTurn()
        if bossStats['hp'] <= 0 and playerStats['mana'] >= 0:
            bestAction = bestAction if manaSpent < 0 else actions if smallestMana == 0 or manaSpent < smallestMana else bestAction
            smallestMana = smallestMana if manaSpent < 0 else manaSpent if smallestMana == 0 or manaSpent < smallestMana else smallestMana
    return smallestMana, bestAction

print(start())
print(start(True))