with open('input.txt') as input:
    frequencyChanges = input.readlines()

frequencyChanges = [int(change.strip()) for change in frequencyChanges]

frequency = 0
knownFrequencies = [frequency]
searching = True

while searching:
    for frequencyChange in frequencyChanges:
        frequency += frequencyChange
        if frequency in knownFrequencies:
            searching = False
            break
        knownFrequencies.append(frequency)

print(frequency)