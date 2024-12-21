input = open('input.txt','r')
lines=[]
total = 0
total2 = 0
for line in input: 
    lines.append(line.strip())
width = len(lines[0])
height = len(lines)
for h in range(height):
    for w in range(width):
        if lines[h][w] == "X":
            if w+3 < width:
                if lines[h][w]+lines[h][w+1]+lines[h][w+2]+lines[h][w+3] == "XMAS":
                    total +=1
            if w+3 < width and h+3<height:
                if lines[h][w]+lines[h+1][w+1]+lines[h+2][w+2]+lines[h+3][w+3] == "XMAS":
                    total +=1
            if w+3 < width and h-3>=0:
                if lines[h][w]+lines[h-1][w+1]+lines[h-2][w+2]+lines[h-3][w+3] == "XMAS":
                    total +=1
            if w-3 >= 0:
                if lines[h][w]+lines[h][w-1]+lines[h][w-2]+lines[h][w-3] == "XMAS":
                    total +=1
            if w-3 >= 0 and h+3<height:
                if lines[h][w]+lines[h+1][w-1]+lines[h+2][w-2]+lines[h+3][w-3] == "XMAS":
                    total +=1
            if w-3 >= 0 and h-3>=0:
                if lines[h][w]+lines[h-1][w-1]+lines[h-2][w-2]+lines[h-3][w-3] == "XMAS":
                    total +=1
            if h -3>=0:
                 if lines[h][w]+lines[h-1][w]+lines[h-2][w]+lines[h-3][w] == "XMAS":
                    total +=1
            if h +3<height:
                 if lines[h][w]+lines[h+1][w]+lines[h+2][w]+lines[h+3][w] == "XMAS":
                    total +=1


for h in range(height):
    for w in range(width):
        if lines[h][w] == "A":
            if h -1 >= 0 and h +1 < height and w-1 >= 0 and w+1 < width:
                if lines[h-1][w-1] == "M" and lines[h-1][w+1] == "M" and lines[h+1][w-1] == "S" and lines[h+1][w+1] == "S":
                    total2 +=1
                if lines[h-1][w-1] == "S" and lines[h-1][w+1] == "M" and lines[h+1][w-1] == "S" and lines[h+1][w+1] == "M":
                    total2 +=1
                if lines[h-1][w-1] == "S" and lines[h-1][w+1] == "S" and lines[h+1][w-1] == "M" and lines[h+1][w+1] == "M":
                    total2 +=1
                if lines[h-1][w-1] == "M" and lines[h-1][w+1] == "S" and lines[h+1][w-1] == "M" and lines[h+1][w+1] == "S":
                    total2 +=1   

print(total)
print(total2)