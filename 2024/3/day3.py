import re
input = open('input.txt','r')
mul = []
numbers = []
total = 0
mul2 = []
numbers2 = []
total2 = 0
do = True

for line in input:
    mul.extend(re.findall("mul\\([0-9]+,[0-9]+\\)",line))
    mul2.extend(re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)",line))


for m in mul:
    numbers.append(re.sub("[^0-9]"," ",m).split())
for n in numbers:
    total = total + ((int)(n[0])*(int)(n[1]))
print(total)

for m in mul2:
    if m == "do()":
        do = True
        continue
    if m == "don't()":
        do = False
        continue
    if do:
        numbers2.append(re.sub("[^0-9]"," ",m).split())
for n in numbers2:
    total2 = total2 + ((int)(n[0])*(int)(n[1]))

print(total2)