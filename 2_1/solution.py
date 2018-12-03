from functools import reduce

def incrementAtIndex(inputList, index):
    inputList[index] += 1
    return inputList

with open('input.txt') as input:
    boxIds = input.readlines()

boxIds = [boxId.strip() for boxId in boxIds]

boxIdsAsBytes = [boxId.encode() for boxId in boxIds]

counts = [reduce(lambda l, byte: incrementAtIndex(l, byte), boxIdAsBytes, [0]*256) for boxIdAsBytes in boxIdsAsBytes]

containsTwoOfLetter = len(list(filter(lambda c: 2 in c, counts)))
containsThreeOfLetter = len(list(filter(lambda c: 3 in c, counts)))

print(containsTwoOfLetter * containsThreeOfLetter)