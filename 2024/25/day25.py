input = open('input.txt','r')
key = False
found = False
keys = []
locks = []
c = [0,0,0,0,0]
count = 0
for line in input:
    if count == 6:
        if key:
            keys.append(c)
        else:
            locks.append(c)
        count = 7
        continue 
    if count == 7:
        count = 0
        c = [0,0,0,0,0]
        continue 
    if count == 0:
        if line[0] == "#":
            key = False
        else:
            key = True
        count = 1
        continue
    if count > 0:
        for i in range(len(line)):
            if line[i] == "#":
                c[i] +=1
        count +=1 
total = 0
for k in keys:
    for l in locks:
        overlap = False
        for i in range(5):
            if k[i] + l[i] > 5:
                overlap = True
                break
        if overlap:
            continue
        else:
            total += 1
print(total)