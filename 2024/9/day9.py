input = open('input.txt','r')
dmap = input.readline()
IDmap = []
check = 1
id = 0
total = 0
total2 = 0
IDmap2 = []
for i in range(len(dmap)):
    if check>0:
        for x in range(int(dmap[i])):
            IDmap.append(id)
        id += 1
    else:
        for x in range(int(dmap[i])):
            IDmap.append(-1)
    check = check * -1

a = -1
iml = list(IDmap)
for i in range(len(iml)):
    if i >= len(iml) + a:
        total += int(iml[i]) * i
        break
    if iml[i] == -1:
        while(iml[a] == -1):
            a -= 1
        iml[i] = iml[a]
        iml[a] = -1
        a -= 1
    total += iml[i] * i

print(total)
id = 0
check = 1
for i in range(len(dmap)):
    if dmap[i] == "0":
        check = check * -1
        continue
    if check>0:
        IDmap2.append([id]*int(dmap[i]))
        id += 1
    else:
        IDmap2.append([-1]*int(dmap[i]))        
    check = check * -1
for i in range(len(IDmap2)):
    if -1 in IDmap2[len(IDmap2)-i-1]:
        continue
    s = len(IDmap2[len(IDmap2)-i-1])
    for x in range(len(IDmap2)-i-1):
        if -1 in IDmap2[x] and len(IDmap2[x]) >= s:
            IDmap2.insert(x,IDmap2[len(IDmap2)-i-1])
            IDmap2.pop(len(IDmap2)-i-1)
            for y in range(s):
                IDmap2[x+1].pop()
            IDmap2.insert(len(IDmap2)-i,[-1]*s)
            break
IDmap2 = [i for i in IDmap2 if i]
count = 0
for x in IDmap2:
    for y in x:
        if y != -1:
            total2 += y * count
        count +=1
print(total2)
 