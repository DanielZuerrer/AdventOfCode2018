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

frequency = reduce(lambda value, operation: addOrSubtract(value, operation), frequencyOperations, 0)

print(frequency)