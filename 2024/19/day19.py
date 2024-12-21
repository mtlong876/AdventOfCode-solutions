from functools import cache
input = open('input.txt','r')
towels = [x.strip() for x in input.readline().strip().split(',')]
next(input)
patterns = []
for lines in input:
    patterns.append(lines.strip())


def tester(goal):
    test = False
    if not goal:
        return True
    for i in range(len(towels)):      
        if towels[i] == goal[:len(towels[i])]:
            test = tester(goal[len(towels[i]):])
        if test == True: break
    return test

@cache
def tester2(goal):
    if not goal:
        return 1
    count = 0
    for i in range(len(towels)):      
        if towels[i] == goal[:len(towels[i])]:
            count += tester2(goal[len(towels[i]):])
    return count


total = 0
total2 = 0
for pattern in patterns:
    if tester(pattern):
        total+=1
    total2 += tester2(pattern)
print(total)
print(total2)