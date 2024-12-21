import collections
input = open('input.txt','r')
coords = []
grid = []
for line in input:
    coords.append([int(x) for x in line.strip().split(',')])
h = 71
v = 71
for y in range(v):
    line  = []
    for x in range(h):
        line.append('.')
    grid.append(line)
for i in range(1024):
    x,y = coords[i]
    grid[y][x] = "#"
for g in grid:
    print("".join(g))
pathq = collections.deque([[0,0,0]])
visited = set((0,0))
while pathq:
    y,x,count = pathq.popleft()
    if [y,x] == [v-1,h-1]:
        break
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=y+dy<v and  0<=x+dx<h:
            if grid[y+dy][x+dx] != "#" and (y+dy,x+dx) not in visited:
                pathq.append([y+dy,x+dx,count+1])
                visited.add((y+dy,x+dx))
print(count)

for i in range(1024,len(coords)):
    x,y = coords[i]
    grid[y][x] = "#"
    pathq = collections.deque([[0,0,0]])
    visited = set((0,0))
    success = False
    while pathq:
        y,x,count = pathq.popleft()
        if [y,x] == [v-1,h-1]:
            success = True
            break
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=y+dy<v and  0<=x+dx<h:
                if grid[y+dy][x+dx] != "#" and (y+dy,x+dx) not in visited:
                    pathq.append([y+dy,x+dx,count+1])
                    visited.add((y+dy,x+dx))
    if not success:
        print(coords[i])
        break