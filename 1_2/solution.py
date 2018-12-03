from functools import reduce

def addOrSubtract(value, operation):
    if operation[0] == '+':
        return value + int(operation[1])
    elif operation[0] == '-':
        return value - int(operation[1])


with open('input.txt') as input:
    frequencyChanges = input.readlines()

frequencyChanges = [change.strip() for change in frequencyChanges]

frequencyOperations = [(change[0], change[1:]) for change in frequencyChanges]

frequency = 0
knownFrequencies = [frequency]
searching = True

while searching:
    for frequencyOperation in frequencyOperations:
        frequency = addOrSubtract(frequency, frequencyOperation)
        if frequency in knownFrequencies:
            searching = False
            break
        knownFrequencies.append(frequency)

print(frequency)