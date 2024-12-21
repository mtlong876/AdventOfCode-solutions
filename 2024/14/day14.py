import copy

class robot:
    def __init__(self,px,py,vx,vy):
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)
    def printRobot(self):
        print(self.px,self.py,self.vx,self.vy)

w = 101
h = 103
input = open('input.txt','r')
room = []
quad =[0,0,0,0]
total = 1
seconds = 10000
for he in range(h):
    line = []
    for wi in range(w):
        line.append(0)
    room.append(line)
room2 = copy.deepcopy(room)
robots = []
for line in input:
    px = line.strip().split()[0].split("=")[1].split(",")[0]
    py = line.strip().split()[0].split("=")[1].split(",")[1]
    vx = line.strip().split()[1].split("=")[1].split(",")[0]
    vy = line.strip().split()[1].split("=")[1].split(",")[1]
    robots.append(robot(px,py,vx,vy))
for x in robots:
    #x.printRobot()
    newX = (x.px + 100*x.vx) % w
    newY = (x.py + 100*x.vy) % h
    room[newY][newX] += 1
for he in range(h):
    if he == int(h/2-0.5):
        continue
    cq = 0
    if he>h/2:
        cq = 2
    for wi in range(w):
        if wi == int(w/2-0.5):
            continue
        cq2 = 0
        if wi>w/2:
            cq2  = 1 
        quad[cq + cq2] += room[he][wi]
for q in quad:
    total *=  q
print(total)
for r in robots:
    room2[r.py][r.px] += 1
for s in range(seconds):
    for r in robots:
        room2[r.py][r.px] -= 1
        r.px = (r.px + r.vx) % w
        r.py = (r.py + r.vy) % h
        room2[r.py][r.px] += 1
    for roo in room2:
        #if len([i for i in roo if i >0]) > 15:
        count = 0
        for ro in roo:
            if ro != 0:
                count+=1
            else:
                count = 0
            if count >= 30:
                print(s)
                break
        if count >= 30:
            for x in room2:
                print(*x)
            break
    if count >= 30:
        break
            


