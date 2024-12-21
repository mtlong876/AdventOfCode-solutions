input = open('input.txt','r')
reports = []
safe = 0
safe2 = 0
unsafeReports = []

for line in input:
    temp = []
    for x in line.strip().split():
        temp.append((int)(x))
    reports.append(temp)
#1
for report in reports:
    previous = -1
    increase = False
    safeC = True
    if report[0]<report[1]:
        increase =  True
    for level in report:
        if previous == -1:
            previous = level
        else:
            diff = abs(level-previous)
            if diff == 0:
                safeC = False
                break
            elif increase and level>previous and diff<4:
                previous = level
            elif not increase and level<previous and diff<4:
                previous = level
            else:
                safeC = False
                break
    if safeC:
        safe +=1
    else:
        unsafeReports.append(report)

print(safe)
#2
for report in unsafeReports:
    for x in range(len(report)):
        temp = report.copy()
        temp.pop(x)
        previous = -1
        increase = False
        safeC = True
        if temp[0]<temp[1]:
            increase =  True
        for level in temp:
            if previous == -1:
                previous = level
            else:
                diff = abs(level-previous)
                if diff == 0:
                    safeC = False
                    break
                elif increase and level>previous and diff<4:
                    previous = level
                elif not increase and level<previous and diff<4:
                    previous = level
                else:
                    safeC = False
                    break
        if safeC:
            safe2 += 1
            break

print (safe2 + safe)