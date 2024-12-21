from collections import defaultdict
input = open('input.txt','r')
p2 = False
rules = []
updates = []
correctUpdates = []
incorrectUpdates = []
total = 0
total2 = 0

for line in input:
    if line == "\n":
        p2 = True
        continue
    if p2:
        temp = []
        for x in line.strip().split(","):
            temp.append((int)(x))
        updates.append(temp)
    else:
        temp = []
        for x in line.strip().split("|"):
            temp.append((int)(x))
        rules.append(temp)

order = defaultdict(list)
for x in rules:
    order[x[0]].append(x[1])

for update in updates:
    previous = []
    correct = True
    for i in update:
        if not previous:
            previous.append(i)
            continue
        for p in previous:
            if i in order[p]:
                continue
            else:
                correct = False
                break
        if correct == False:
            break
        previous.append(i)
    if correct:
        correctUpdates.append(update)
    else:
        incorrectUpdates.append(update)

for cu in correctUpdates:
    total+=cu[(int)((len(cu)/2)-0.5)]
print(total)

fixed = []
for update in incorrectUpdates:
    corrected = []
    while update: 
        for u in update:
            correct = True
            for x in update:
                if x == u:
                    continue
                if u in order[x]:
                    continue
                else:
                    correct = False
                    break
            if correct:
                corrected.append(u)
                update.remove(u)
    fixed.append(corrected)

for fu in fixed:
    total2+=fu[(int)((len(fu)/2)-0.5)]
print(total2)