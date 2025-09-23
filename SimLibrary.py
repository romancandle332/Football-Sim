import random
import math

def WeightedRound(number):
    chance = round(number - math.floor(number),2)
    roll = random.random()
    if roll <= chance:
        return math.floor(number) + 1
    else:
        return math.floor(number)

def ConvertSkillToAdvantage(option,skill_value):
    if option == 0: ##2.5 deviation, 0 base
        skill_score = WeightedRound(skill_value/2.5)
    elif option == 1: ##2.5 deviation, 10 mean
        skill_score = WeightedRound((skill_value-10)/2.5)
    return skill_score

def DiceRollHigh(advantage):
    rollbucket = []
    rolls = 0
    if advantage < 0:
        while rolls <= abs(advantage):
            r = random.randint(0,100)
            rollbucket.append(r)
            rolls += 1
        q = int(min(rollbucket))
    elif advantage == 0:
        q = random.randint(0,100)
    elif advantage > 0:
        while rolls <= advantage:
            r = random.randint(0,100)
            rollbucket.append(r)
            rolls += 1
        q = int(max(rollbucket))
    return q

def DiceRollLow(advantage):
    rollbucket = []
    rolls = 0
    if advantage < 0:
        while rolls <= abs(advantage):
            r = random.randint(0,100)
            rollbucket.append(r)
            rolls += 1
        q = int(max(rollbucket))
    elif advantage == 0:
        q = random.randint(0,100)
    elif advantage > 0:
        while rolls <= advantage:
            r = random.randint(0,100)
            rollbucket.append(r)
            rolls += 1
        q = int(min(rollbucket))
    return q

def DiceRollFifty(advantage):    
    rollbucket = []
    rolls = 0
    if advantage < 0:
        while rolls <= abs(advantage):
            r = abs(50-random.randint(0,100))
            rollbucket.append(r)
            rolls += 1
        q = int(max(rollbucket))
    elif advantage == 0:
        q = abs(50-random.randint(0,100))
    elif advantage > 0:
        while rolls <= advantage:
            r = abs(50-random.randint(0,100))
            rollbucket.append(r)
            rolls += 1
        q = int(min(rollbucket))
    return q