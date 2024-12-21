import copy
input = open('input.txt','r')
lines = []
total = 0
for line in input: 
    lines.append([x for x in line.strip()])
original = copy.deepcopy(lines)
guard = [">","<","^","v"]
posX, posY = (0,0)
for line in lines:
    found = False
    for g in guard:
        if g in line:
            posX = line.index(g)
            found = True
    if found:
        break
    posY += 1
start = [posX,posY]
visited = []
while(True):
    if [posY,posX] not in visited:
        visited.append([posY,posX])
    if lines[posY][posX] == "^":
        if lines[posY-1][posX] == "#":
            lines[posY][posX] = ">"
        else:
            lines[posY][posX] = "X"
            if posY-1 < 0:
                break
            lines[posY-1][posX] = "^"
            posY-= 1
    if lines[posY][posX] == ">":
        if posX+1 >= len(lines[0]):
            lines[posY][posX] = "X"
            break
        if lines[posY][posX+1] == "#":
            lines[posY][posX] = "v"
        else:
            lines[posY][posX] = "X"
            if posX+1 >= len(lines[0]):
                break
            lines[posY][posX+1] = ">"
            posX+= 1
    if lines[posY][posX] == "v":
        if posY+1 >= len(lines):
            lines[posY][posX] = "X"
            break
        if lines[posY+1][posX] == "#":
            lines[posY][posX] = "<"
        else:
            lines[posY][posX] = "X"
            if posY+1 >= len(lines):
                break
            lines[posY+1][posX] = "v"
            posY+= 1
    if lines[posY][posX] == "<":
        if posX-1 < 0:
            lines[posY][posX] = "X"
            break
        if lines[posY][posX-1] == "#":
            lines[posY][posX] = "^"
        else:
            lines[posY][posX] = "X"
            if posX-1 < 0:
                break
            lines[posY][posX-1] = "<"
            posX-= 1

for x in lines:
    total += x.count("X")
print(total)
visited.pop(0)
total2 = 0
#print(len(visited))
test = 0
for x in visited:
    temp = copy.deepcopy(original)
    temp[x[0]][x[1]] = "#"
    posY,posX = (start[1],start[0])
    count = 0
    if test % 200 == 0:
        print(test)
    while(True):
        if temp[posY][posX] == "^":
            if temp[posY-1][posX] == "#":
                temp[posY][posX] = ">"
            else:
                temp[posY][posX] = "X"
                if posY-1 < 0:
                    break
                temp[posY-1][posX] = "^"
                posY-= 1
        if temp[posY][posX] == ">":
            if posX+1 >= len(temp[0]):
                temp[posY][posX] = "X"
                break
            if temp[posY][posX+1] == "#":
                temp[posY][posX] = "v"
            else:
                temp[posY][posX] = "X"
                if posX+1 >= len(temp[0]):
                    break
                temp[posY][posX+1] = ">"
                posX+= 1
        if temp[posY][posX] == "v":
            if posY+1 >= len(temp):
                temp[posY][posX] = "X"
                break
            if temp[posY+1][posX] == "#":
                temp[posY][posX] = "<"
            else:
                temp[posY][posX] = "X"
                if posY+1 >= len(temp):
                    break
                temp[posY+1][posX] = "v"
                posY+= 1
        if temp[posY][posX] == "<":
            if posX-1 < 0:
                temp[posY][posX] = "X"
                break
            if temp[posY][posX-1] == "#":
                temp[posY][posX] = "^"
            else:
                temp[posY][posX] = "X"
                if posX-1 < 0:
                    break
                temp[posY][posX-1] = "<"
                posX-= 1
        if count > 10000:
            total2 += 1
            break
        count+=1
    test+=1
print(total2)
