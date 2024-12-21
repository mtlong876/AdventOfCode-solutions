def hike(trail,coords,score,visited,score2):
    y,x = coords
    cur = trail[y][x]
    if cur == 9:
        score2[0] += 1
        if [y,x] not in visited:
            score[0] += 1
            visited.append([y,x])
        return True
    if trail[y-1][x] == cur+1 and y-1>=0:
        hike(trail,[y-1,x],score,visited,score2)
    if  y+1<(len(trail)) and trail[y+1][x] == cur+1:
        hike(trail,[y+1,x],score,visited,score2)
    if trail[y][x-1] == cur+1 and x-1>=0:
        hike(trail,[y,x-1],score,visited,score2)
    if x+1<len(trail[y]) and trail[y][x+1] == cur+1:
        hike(trail,[y,x+1],score,visited,score2)
    return False

input = open('input.txt','r')
trail = []
trailheads = []
scores=[]
scores2=[]
total = 0
total2 = 0
for line in input:
    trail.append([int(x) for x in line.strip()])


for y in range(len(trail)):
    for x in range(len(trail[0])):
        if trail[y][x] == 0:
            trailheads.append([y,x])
for head in trailheads:
    score = [0]
    visited = []
    score2 = [0]
    hike(trail,head,score,visited,score2)
    scores.append(score)
    scores2.append(score2)
for s in scores:
    total +=s[0]
print(total)
for s in scores2:
    total2 +=s[0]
print(total2)