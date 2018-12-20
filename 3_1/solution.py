import re

with open('input.txt') as input:
    claims = input.readlines()

claims = [claim.strip() for claim in claims]

regex = r'^.+@ (\d+),(\d+): (\d+)x(\d+)$'
matches = [re.match(regex, claim) for claim in claims]

claims = [{
    'left': int(match.group(1)),
    'top': int(match.group(2)),
    'width': int(match.group(3)),
    'height': int(match.group(4))
} for match in matches]

fabric = {}

def claim_pattern(fabric, claim):
    for x in range(claim['left'], claim['left']+claim['width']):
        for y in range(claim['top'], claim['top'] + claim['height']):
            key = f'{x}|{y}'
            inch = fabric.setdefault(key, 0)
            inch += 1
            fabric[key] = inch


for claim in claims:
    claim_pattern(fabric, claim)

print(len(list(filter(lambda inch: inch > 1, fabric.values()))))
