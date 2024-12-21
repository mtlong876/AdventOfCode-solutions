from string import ascii_uppercase
import collections
input = open('input.txt','r')
farm = []
total = 0
total2 = 0
for line in input:
    farm.append([x for x in line.strip()])

for letter in ascii_uppercase:
    visited = []
    for farmy in range(len(farm)):
        for farmx in range(len(farm[0])):
            if farm[farmy][farmx] == letter and [farmy,farmx] not in visited:
                visited.append([farmy,farmx])
                farmQ = collections.deque([(farmy,farmx)])
                p = 0
                perimiter = set()
                area = 0
                while(farmQ):
                    area +=1
                    y,x = farmQ.popleft()
                    if y - 1 >= 0 and farm[y-1][x] == letter:
                        if [y-1,x] not in visited:
                            farmQ.append([y-1,x])
                            visited.append([y-1,x])
                    else:
                        p+=1
                        perimiter.add((y,x,'u'))
                    if x - 1 >= 0 and farm[y][x-1] == letter:
                        if [y,x-1] not in visited:
                            farmQ.append([y,x-1])
                            visited.append([y,x-1])
                    else:
                        p+=1
                        perimiter.add((y,x,'l'))
                    if y + 1 < len(farm) and farm[y+1][x] == letter:
                        if [y+1,x] not in visited:
                            farmQ.append([y+1,x])
                            visited.append([y+1,x])
                    else:
                        p+=1
                        perimiter.add((y,x,'d'))
                    if x + 1 < len(farm[0]) and farm[y][x+1] == letter:
                        if [y,x+1] not in visited:
                            farmQ.append([y,x+1])
                            visited.append([y,x+1])
                    else:
                        p+=1
                        perimiter.add((y,x,'r'))
                total +=p*area
                p2 = perimiter.copy()
                for p in perimiter:
                    y,x,d = p
                    if (y,x+1,d) in perimiter:
                        p2.remove((y,x,d))
                    if (y+1,x,d) in perimiter:
                        p2.remove((y,x,d))
                total2 += (len(p2) * area)
print(total)
print(total2)


                
