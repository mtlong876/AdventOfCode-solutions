import time
input = open('input.txt','r')
a = int(input.readline().strip().split(':')[1])
b = int(input.readline().strip().split(':')[1])
c = int(input.readline().strip().split(':')[1])
initial = [b,c]
next(input)
instructions = [int(x) for x in input.readline().strip().split(':')[1].split(",")]
point = 0
output = []
while(point<len(instructions)):
    #print(point)
    
    opcode = instructions[point]
    operand = instructions[point+1]
    match operand:
        case 0:
            combo = 0
        case 1:
            combo = 1
        case 2: 
            combo = 2
        case 3:
            combo = 3
        case 4:
            combo = a
        case 5:
            combo = b
        case 6:
            combo = c

    match opcode:
        case 0:
            i = a/pow(2,combo)
            a = int(str(i).split(".")[0])
        case 1:
            b = b ^ operand
        case 2:
            b = combo%8
        case 3:
            if a != 0:
                point = operand
                continue
            else:
                pass
        case 4:
            b = b ^ c
        case 5:
            output.append(combo%8)
        case 6:
            i = a/pow(2,combo)
            b = int(str(i).split(".")[0])
        case 7:
            i = a/pow(2,combo)
            c = int(str(i).split(".")[0])
    point +=2
    #print("A:",a,"B:",b,"C:",c)
print(output)
found = False

def part2(instruction, ans):
    #print(instruction)
    if instruction == []:
        return ans
    for b in range(8):
        a = (ans << 3) +b
        sa = a
        b = b ^ 5
        c = a >> b
        a = a >> 3
        b = b ^ 6
        b = b ^ c
        if b % 8 == instruction[-1]:
            sub = part2(instruction[:-1],sa)
            if sub is None:
                continue
            return sub

print(part2(instructions,0))