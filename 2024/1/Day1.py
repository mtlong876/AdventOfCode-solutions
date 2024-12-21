input = open('input.txt','r')
l1 = []
l2 = []
distance = 0
count = {}
similarirty = 0
for line in input:
    l1.append((int)(line.strip().split()[0]))
    l2.append((int)(line.strip().split()[1]))
    if (int)(line.strip().split()[1]) in count:
        count[(int)(line.strip().split()[1])] += 1
    else:
        count[(int)(line.strip().split()[1])] = 1

l1.sort()
l2.sort()   

for x in range(len(l2)):
    distance += abs(l1[x]-l2[x])
    if l1[x] in count:
        similarirty = similarirty + (l1[x] * count[l1[x]])

print(distance)
print(similarirty)