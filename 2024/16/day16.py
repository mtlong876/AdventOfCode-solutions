import heapq
input = open('input.txt','r')
map = []
for line in input:
    map.append([x for x in line.strip()])

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "E":
            end = [y,x]
        if map[y][x] == "S":
            start = [y,x]

mapQ =[(0,start[0],start[1],0,1,[])]
seen = {(start[0],start[1],0,1)}
seat = set()
bestcost = 100000
paths = []
while mapQ:
    #print(mapQ)
    cost,y,x,dy,dx,path= heapq.heappop(mapQ)
    seen.add((y,x,dy,dx))
    seat.add((y,x))
    #print(path)
    
    if map[y][x] == "E":
        if cost <= bestcost:
            bestcost = cost
            print(cost)
            #print(path)
            paths.append(path)
    for new_cost,ny,nx,ndy,ndx in [(cost+1,y+dy,x+dx,dy,dx),(cost+1000,y,x,dx,-dy),(cost+1000,y,x,-dx,dy)]:
        if map[ny][nx] =="#":
            #print("DFSDFSD")
            continue
        if (ny,nx,ndy,ndx) in seen:
            continue
        #print(ny,nx)
        heapq.heappush(mapQ,(new_cost,ny,nx,ndy,ndx,path+[[ny,nx]]))    
tiles = set()
for p in paths:
    for x in p:
        tiles.add(str(x[0])+"."+str(x[1]))
print(len(tiles))