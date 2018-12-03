with open('input.txt') as input:
    frequencyChanges = input.readlines()

frequencyChanges = [int(change.strip()) for change in frequencyChanges]

frequency = sum(frequencyChanges, 0)

print(frequency)