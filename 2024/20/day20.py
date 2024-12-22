import collections
input = open('input.txt','r')
map = []
for line in input:
    map.append([x for x in line.strip()])

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "E":
            end = [y,x]
            map[y][x] = '.'
        if map[y][x] == "S":
            start = [y,x]

#[print(x) for x in map]

raceq = collections.deque([[start[0],start[1],0]])
visited = set()
visited.add((start[0],start[1]))

shortcut = []
times = {}
while raceq:
    y,x,count = raceq.popleft()
    times[(y,x)] = count
    if[y,x] == [end[0],end[1]]: break
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=y+dy<len(map) and  0<=x+dx<len(map[0]):
            if map[y+dy][x+dx] != "#" and (y+dy,x+dx) not in visited:
                raceq.append([y+dy,x+dx,count+1])
                visited.add((y+dy,x+dx))
        if 0<=y+dy+dy<len(map) and  0<=x+dx+dx<len(map[0]):
            if map[y+dy][x+dx] == "#" and  map[y+dy+dy][x+dx+dx] == "." and (y+dy,x+dx) not in visited:
                sc = [[y,x],[y+dy+dy,x+dx+dx]]
                if sorted(sc) not in shortcut:
                    shortcut.append(sorted(sc))

total = 0
for sc in shortcut:
    if abs(times[(sc[0][0],sc[0][1])]-times[(sc[1][0],sc[1][1])])-2 >= 100:
        total+=1
print(total)

total2 = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "#": continue
        for radius in range(2,21):
            for dy in range(radius+1):
                dx = radius -dy
                for ny,nx in {(y + dy, x + dx),(y +dy,x - dx), (y - dy, x + dx),(y -dy,x - dx)}:
                    if ny <0 or nx <0 or ny>=len(map) or nx  >= len(map[0]): continue
                    if map[ny][nx] == "#": continue
                    if times[(y,x)]-times[(ny,nx)]-radius >= 100:
                        total2 += 1
print(total2)
    