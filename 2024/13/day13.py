input = open('input.txt','r')
inputcount = 0
buttonA = []
buttonB = []
prizes = []
total = 0
total2 = 0
for line in input:
    if inputcount == 0:
        xy = [int(line.strip().split(':')[1].split(',')[0].split("+")[1]),int(line.strip().split(':')[1].split(',')[1].split("+")[1])]
        buttonA.append(xy)
    if inputcount == 1:
        xy = [int(line.strip().split(':')[1].split(',')[0].split("+")[1]),int(line.strip().split(':')[1].split(',')[1].split("+")[1])]
        buttonB.append(xy)
    if inputcount == 2:
        xy = [int(line.strip().split(':')[1].split(',')[0].split("=")[1]),int(line.strip().split(':')[1].split(',')[1].split("=")[1])]
        prizes.append(xy)
    if inputcount == 3:
        inputcount = 0
        continue
    inputcount += 1
            
for i in range(len(buttonA)):
    det = (buttonA[i][0] * buttonB[i][1]) - (buttonA[i][1]* buttonB[i][0])
    a = ((prizes[i][0] * buttonB[i][1])-(prizes[i][1] * buttonB[i][0]))/det 
    b = ((prizes[i][1] * buttonA[i][0])-(prizes[i][0] * buttonA[i][1]))/det 
    if a == int(a) and b == int(b):
        total+= a *3 + b

print(int(total))
prizes2 = []
for p in prizes:
    prizes2.append([p[0]+10000000000000,p[1]+10000000000000])

for i in range(len(buttonA)):
    det = (buttonA[i][0] * buttonB[i][1]) - (buttonA[i][1]* buttonB[i][0])
    a = ((prizes2[i][0] * buttonB[i][1])-(prizes2[i][1] * buttonB[i][0]))/det 
    b = ((prizes2[i][1] * buttonA[i][0])-(prizes2[i][0] * buttonA[i][1]))/det 
    if a == int(a) and b == int(b):
        total2+= a *3 + b
print(int(total2))