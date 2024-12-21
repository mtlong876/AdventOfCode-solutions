from collections import defaultdict
input = open('input.txt','r')
blinks = 75
stonescount = defaultdict(int)
stones = [int(x) for x in input.readline().split()]
total = 0
for stone in stones:
    stonescount[stone] +=1

#for blink in range(blinks):
#    print(blink)
#    split = []
#    for i in range(len(stones)):
#        length = len(str(stones[i]))
#        if stones[i] == 0:
#            stones[i] = 1
#        elif length % 2 == 0:
#            stones[i] = str(stones[i])[0:int(length/2)] + "/" + str(stones[i])[int(length/2):]
#            split.append(i)
#        else:
#            stones[i] = stones[i] *2024
#    split.reverse()
#    for s in split:
#        stone = stones[s].split("/")
#        stones.insert(s, int(stone[0]))
#        stones[s+1] = int(stone[1])
#print(len(stones))

for blink in range(blinks):
    print(blink)
    newcount = defaultdict(int)
    for stone,val in stonescount.items():
        if stone == 0:
            newcount[1] += val
        elif len(str(stone)) % 2 == 0:
            newcount[int(str(stone)[0:int(len(str(stone))/2)])] += val
            newcount[int(str(stone)[int(len(str(stone))/2):])] += val
        else:
            newcount[stone * 2024] += val
    stonescount = newcount
for x in stonescount.values():
    total += x
print(total)