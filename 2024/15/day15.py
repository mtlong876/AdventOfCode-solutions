import collections
input = open('input.txt','r')
lines = []
fmap = True
instructions = []
total = 0
total2 = 0
for line in input:
    if line == "\n":
        fmap = False
        continue
    if fmap:
        lines.append([x for x in line.strip()])
    else:
        instructions.append([x for x in line.strip()])

posX, posY = (0,0)
for line in lines:
    if "@" in line:
        posX = line.index("@")
        break
    posY += 1

newlines = []
for line in lines:
    newline  = []
    for char in line:
        if char == "#":
            newline.append('#')
            newline.append('#')
        elif char == 'O':
            newline.append('[')
            newline.append(']')
        elif char == '.':
            newline.append('.')
            newline.append('.')
        elif char == '@':
            newline.append('@')
            newline.append('.')
    newlines.append(newline)


for i in instructions:
    for move in i:
        if move == '^':
            if lines[posY-1][posX] == "#":
                 continue
            elif lines[posY-1][posX] == "O":
                rock = collections.deque([[posY-1,posX]])
                totalrock = collections.deque([[posY-1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y-1][x] == 'O':
                        totalrock.append([y-1,x])
                        rock.append([y-1,x])
                    elif lines[y-1][x] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y-1][x] = 'O'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posY -=1
            else:
                lines[posY][posX] = '.'
                lines[posY-1][posX] = '@'
                posY = posY-1
        if move == 'v':
            if lines[posY+1][posX] == "#":

                 continue
            elif lines[posY+1][posX] == "O":
                rock = collections.deque([[posY+1,posX]])
                totalrock = collections.deque([[posY+1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y+1][x] == 'O':
                        totalrock.append([y+1,x])
                        rock.append([y+1,x])
                    elif lines[y+1][x] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y+1][x] = 'O'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posY += 1
            else:
                lines[posY][posX] = '.'
                lines[posY+1][posX] = '@'
                posY = posY+1
        if move == '<':
            if lines[posY][posX-1] == "#":
                 continue
            elif lines[posY][posX-1] == "O":
                rock = collections.deque([[posY,posX-1]])
                totalrock = collections.deque([[posY,posX-1]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y][x-1] == 'O':
                        totalrock.append([y,x-1])
                        rock.append([y,x-1])
                    elif lines[y][x-1] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y][x-1] = 'O'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posX -= 1
            else:
                lines[posY][posX] = '.'
                lines[posY][posX-1] = '@'
                posX = posX-1
        if move == '>':
            if lines[posY][posX+1] == "#":
                 continue
            elif lines[posY][posX+1] == "O":
                rock = collections.deque([[posY,posX+1]])
                totalrock = collections.deque([[posY,posX+1]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y][x+1] == 'O':
                        totalrock.append([y,x+1])
                        rock.append([y,x+1])
                    elif lines[y][x+1] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y][x+1] = 'O'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posX +=1
            else:
                lines[posY][posX] = '.'
                lines[posY][posX+1] = '@'
                posX = posX+1
                    
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if(lines[y][x]) == "O":
            total += (100*y) + x
print(total)

posX, posY = (0,0)
for line in newlines:
    if "@" in line:
        posX = line.index("@")
        break
    posY += 1
lines = newlines

for i in instructions:
    for move in i:
        if move == '^':
            if lines[posY-1][posX] == "#":
                 continue
            elif lines[posY-1][posX] == "[":
                rock = collections.deque([[posY-1,posX]])
                totalrock = collections.deque([[posY-1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y-1][x] == '[' and lines[y-1][x+1] == ']':
                        totalrock.append([y-1,x])
                        rock.append([y-1,x])
                    elif lines[y-1][x] == '#' or lines[y-1][x+1] == '#':
                        wall = True
                    if lines[y-1][x] == ']':
                        totalrock.append([y-1,x-1])
                        rock.append([y-1,x-1])
                    if lines[y-1][x+1] == '[':
                        totalrock.append([y-1,x+1])
                        rock.append([y-1,x+1])
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y-1][x] = '['
                        lines[y-1][x+1] = ']'
                        lines[y][x+1] = '.'
                        lines[y][x] = '.'
                    lines[posY-1][posX] = "@"
                    lines[posY][posX] = '.'
                    posY -= 1
            elif lines[posY-1][posX] == "]":
                rock = collections.deque([[posY-1,posX]])
                totalrock = collections.deque([[posY-1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y-1][x] == ']' and lines[y-1][x-1] == '[':
                        totalrock.append([y-1,x])
                        rock.append([y-1,x])
                    elif lines[y-1][x] == '#' or lines[y-1][x-1] == '#':
                        wall = True
                    if lines[y-1][x] == '[':
                        totalrock.append([y-1,x+1])
                        rock.append([y-1,x+1])
                    if lines[y-1][x-1] == ']':
                        totalrock.append([y-1,x-1])
                        rock.append([y-1,x-1])
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y-1][x] = ']'
                        lines[y-1][x-1] = '['
                        lines[y][x-1] = '.'
                        lines[y][x] = '.'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posY -= 1
            else:
                lines[posY][posX] = '.'
                lines[posY-1][posX] = '@'
                posY = posY-1
        if move == 'v':
            if lines[posY+1][posX] == "#":
                 continue
            elif lines[posY+1][posX] == "[":
                rock = collections.deque([[posY+1,posX]])
                totalrock = collections.deque([[posY+1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y+1][x] == '[' and lines[y+1][x+1] == ']':
                        totalrock.append([y+1,x])
                        rock.append([y+1,x])
                    elif lines[y+1][x] == '#' or lines[y+1][x+1] == '#':
                        wall = True
                    if lines[y+1][x] == ']':
                        totalrock.append([y+1,x-1])
                        rock.append([y+1,x-1])
                    if lines[y+1][x+1] == '[':
                        totalrock.append([y+1,x+1])
                        rock.append([y+1,x+1])
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y+1][x] = '['
                        lines[y+1][x+1] = ']'
                        lines[y][x+1] = '.'
                        lines[y][x] = '.'
                    lines[posY+1][posX] = "@"
                    lines[posY][posX] = '.'
                    posY += 1
            elif lines[posY+1][posX] == "]":
                rock = collections.deque([[posY+1,posX]])
                totalrock = collections.deque([[posY+1,posX]])
                wall = False
                while(rock):
                    y,x = rock.popleft()
                    if lines[y+1][x] == ']' and lines[y+1][x-1] == '[':
                        totalrock.append([y+1,x])
                        rock.append([y+1,x])
                    elif lines[y+1][x] == '#' or lines[y+1][x-1] == '#':
                        wall = True
                    if lines[y+1][x] == '[':
                        totalrock.append([y+1,x+1])
                        rock.append([y+1,x+1])
                    if lines[y+1][x-1] == ']':
                        totalrock.append([y+1,x-1])
                        rock.append([y+1,x-1])
                if not wall:
                    while(totalrock):
                        y,x = totalrock.pop()
                        lines[y+1][x] = ']'
                        lines[y+1][x-1] = '['
                        lines[y][x-1] = '.'
                        lines[y][x] = '.'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posY += 1
            else:
                lines[posY][posX] = '.'
                lines[posY+1][posX] = '@'
                posY = posY+1
        if move == '<':
            if lines[posY][posX-1] == "#":
                 continue
            elif lines[posY][posX-1] == "]":
                rock = collections.deque([[posY,posX-1,posX-2]])
                totalrock = collections.deque([[posY,posX-1,posX-2]])
                wall = False
                while(rock):
                    y,x,x2 = rock.popleft()
                    if lines[y][x2-1] == ']':
                        totalrock.append([y,x2-1,x2-2])
                        rock.append([y,x2-1,x2-2])
                    elif lines[y][x2-1] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x,x2 = totalrock.pop()
                        lines[y][x-1] = ']'
                        lines[y][x2-1] = '['
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posX -= 1
            else:
                lines[posY][posX] = '.'
                lines[posY][posX-1] = '@'
                posX = posX-1
        if move == '>':
            if lines[posY][posX+1] == "#":
                 continue
            elif lines[posY][posX+1] == "[":
                rock = collections.deque([[posY,posX+1,posX+2]])
                totalrock = collections.deque([[posY,posX+1,posX+2]])
                wall = False
                while(rock):
                    y,x,x2 = rock.popleft()
                    if lines[y][x2+1] == '[':
                        totalrock.append([y,x2+1,x2+2])
                        rock.append([y,x2+1,x2+2])
                    elif lines[y][x2+1] == '#':
                        wall = True
                if not wall:
                    while(totalrock):
                        y,x,x2 = totalrock.pop()
                        lines[y][x+1] = '['
                        lines[y][x2+1] = ']'
                    lines[y][x] = "@"
                    lines[posY][posX] = '.'
                    posX += 1
            else:
                lines[posY][posX] = '.'
                lines[posY][posX+1] = '@'
                posX = posX+1

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if(lines[y][x]) == "[":
            total2 += (100*y) + x

print(total2)