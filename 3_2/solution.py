import re

with open('input.txt') as input:
    claims = input.readlines()

claims = [claim.strip() for claim in claims]

regex = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
matches = [re.match(regex, claim) for claim in claims]

claims = [{
    'id': int(match.group(1)),
    'left': int(match.group(2)),
    'top': int(match.group(3)),
    'width': int(match.group(4)),
    'height': int(match.group(5))
} for match in matches]

fabric = {}

def claim_pattern(fabric, claim):
    overlap = False
    for x in range(claim['left'], claim['left']+claim['width']):
        for y in range(claim['top'], claim['top'] + claim['height']):
            key = f'{x}|{y}'
            inch = fabric.setdefault(key, 0)
            inch += 1
            if inch > 2 and iteration == 2: overlap = True
            fabric[key] = inch
    return overlap

iteration = 1
for claim in claims:
    claim_pattern(fabric, claim)

iteration = 2
for claim in claims:
    overlap = claim_pattern(fabric, claim)
    if not overlap: print(claim['id'])
