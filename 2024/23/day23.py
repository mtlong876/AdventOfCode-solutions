import collections
input = open('input.txt','r')
computers = collections.defaultdict(list)
for line in input:
    computer = line.strip().split("-")
    computers[computer[0]].append(computer[1])
    computers[computer[1]].append(computer[0])

SoS = set()
def findConnections(key,comps):
    if tuple(sorted(comps)) in SoS: return
    SoS.add(tuple(sorted(comps)))
    for connection in computers[key]:
        if connection in comps: continue
        if not all(connection in computers[ckey] for ckey in comps): continue
        findConnections(connection,comps | {connection})

triple = set()
for key in computers:
    findConnections(key,{key})
    for i in range(len(computers[key])):
        for x in range(i+1,len(computers[key])):
            if computers[key][x] in computers[computers[key][i]]:
                tup = (key,computers[key][i],computers[key][x])
                triple.add(tuple(sorted(tup)))

total = 0                
for cs in triple:
    test = False
    for c in cs:
        if list(c)[0] == 't':
            test = True
    if test:
        total += 1

print(total)
print(",".join(sorted(max(SoS,key=len))))