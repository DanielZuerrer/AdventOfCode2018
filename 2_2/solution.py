def incrementAtIndex(inputList, index):
    inputList[index] += 1
    return inputList

with open('input.txt') as input:
    boxIds = input.readlines()

boxIds = [boxId.strip() for boxId in boxIds]

for l in range(len(boxIds[0]) + 1):
    slicedIds = list(map(lambda boxId: boxId[:l - 1] + boxId[l:], boxIds))
    uniqueSlicedIds = set(slicedIds)

    if len(slicedIds) != len(uniqueSlicedIds):
        [slicedIds.remove(slicedId) for slicedId in uniqueSlicedIds]
        print(slicedIds[0])
