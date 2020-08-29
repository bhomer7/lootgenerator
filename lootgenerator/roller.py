import random
import re


constant_regex = re.compile('^[0-9]+$')
range_regex = re.compile('^[0-9]+-[0-9]+$')
dice_regex = re.compile('^([1-9][0-9]*)?d([1-9][0-9]*)(\*[1-9][0-9]*)?(\+[1-9][0-9]*)?$')
dice_separators = re.compile('d|\*|\+')

def roll_loot(table, numRolls = 1):
    categories = []
    for cat in table['items']:
        index = table['items'].index(cat)
        for w in range(int(cat['weight'])):
            categories.append(index)
    
    results = {}
    for r in range(numRolls):
        random.shuffle(categories)
        cat = table['items'][categories[0]]
        for a in range(eval_expression(cat['amount'])):
            for item in cat['items']:
                if item['name'] not in results:
                    results[item['name']] = [0, 0, item]
                results[item['name']][0] += eval_expression(item['amount'])
                results[item['name']][1] += 1

    return results


def eval_expression(string):
    string = ''.join(string.split())
    if constant_regex.match(string):
        return int(string)
    if range_regex.match(string):
        return eval_range(string)
    if dice_regex.match(string):
        return eval_dice(string)
    raise SyntaxError('dice expression cannot be evaluated: ' + string)


def eval_range(string):
    values = string.split('-')
    return random.randint(int(values[0]), int(values[1]))


def eval_dice(string):
    values = dice_separators.split(string)
    
    if values[0] == '':
        numDice = 1
    else:
        numDice = int(values[0])

    diceSize = int(values[1])

    if '*' in string:
        multiplier = int(values[2])
    else:
        multiplier = 1

    if '+' in string:
        add = int(values[-1])
    else:
        add = 0

    result = 0
    for i in range(numDice):
        result += random.randint(1, diceSize)
    result *= multiplier
    result += add
    return result




