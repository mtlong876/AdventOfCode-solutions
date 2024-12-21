from collections import defaultdict
from itertools import combinations
input = open('input.txt','r')
lines = []
antennas = defaultdict(list)
pairs = defaultdict(list)
antinode = []
total = 0
antinode2 = []
total2 = 0
for line in input:
    lines.append([x for x in line.strip()])
    antinode.append(["." for x in line.strip()])
    antinode2.append(["." for x in line.strip()])

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != ".":
            antennas[lines[y][x]].append([y,x])
   
for frequency in antennas:
    for combo in list(combinations(antennas[frequency],2)):
        y1,x1 = combo[0]
        y2,x2 = combo[1]
        offsetY = combo[0][0]-combo[1][0]
        offsetX = combo[0][1]-combo[1][1]

        if 0<=y1+offsetY<len(lines) and 0<=x1+offsetX<len(lines[0]):
            antinode[y1+offsetY][x1+offsetX] = "#"
        if 0<=y2-offsetY<len(lines) and 0<=x2-offsetX<len(lines[0]):
            antinode[y2-offsetY][x2-offsetX] = "#"


for x in antinode:
    total+=x.count("#")
print(total)

for frequency in antennas:
    for x in antennas[frequency]:
        antinode2[x[0]][x[1]] = "#"
    for combo in list(combinations(antennas[frequency],2)):
        y1,x1 = combo[0]
        y2,x2 = combo[1]
        offsetY = combo[0][0]-combo[1][0]
        offsetX = combo[0][1]-combo[1][1]

        while(0<=y1<len(lines) or 0<=y2<len(lines) or 0<=x2<len(lines[0]) or 0<=x2<len(lines[0])):
            if 0<=y1+offsetY<len(lines) and 0<=x1+offsetX<len(lines[0]):
                antinode2[y1+offsetY][x1+offsetX] = "#"
            if 0<=y2-offsetY<len(lines) and 0<=x2-offsetX<len(lines[0]):
                antinode2[y2-offsetY][x2-offsetX] = "#"
            y1 = y1+offsetY
            y2 = y2-offsetY
            x1 = x1+offsetX
            x2 = x2-offsetX

for x in antinode2:
    total2+=x.count("#")

print(total2)