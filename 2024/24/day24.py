class instruction:
    def __init__(self,input1,input2,type,output):
        self.input1 = input1
        self.input2 = input2
        self.type = type
        self.output = output
    def __str__(self):
        return f"{self.input1},{self.type},{self.input2},{self.output}"
    
import collections        

input = open('input.txt','r')
wires = {}
instructions = collections.deque()
instructions2 = []
for line in input:
    if line == "\n":
        break
    wires[line.strip().split(":")[0]] = int(line.strip().split(":")[1])

for line in input:
    instructions.append(instruction(line.strip().split()[0],line.strip().split()[2],line.strip().split()[1],line.strip().split()[4]))
    instructions2.append(instruction(line.strip().split()[0],line.strip().split()[2],line.strip().split()[1],line.strip().split()[4]))
while(instructions):
    i = instructions.popleft()
    if i.input1 in wires.keys() and i.input2 in wires.keys():
        match i.type:
            case "XOR":
                wires[i.output] = wires[i.input1] ^ wires[i.input2]
            case "AND":
                wires[i.output] = wires[i.input1] & wires[i.input2]
            case "OR":
                wires[i.output] = wires[i.input1] | wires[i.input2]
    else:
        instructions.append(i)
output = ""
for key in sorted(wires):
    if list(key)[0] == "z":
        output = str(wires[key]) + output
print(int(output,2))

wrong = set()
for i in instructions2:
    if i.output[0] == "z" and i.type != "XOR" and i.output != "z45":
        wrong.add(i.output)
    if i.type == "XOR" and i.output[0] not in ["x", "y", "z"] and i.input1[0] not in ["x", "y", "z"] and i.input2[0] not in ["x", "y", "z"]:
        wrong.add(i.output)
    if i.type == "AND" and "x00" not in [i.input1, i.input2]:
        for si in instructions2:
            if (i.output == si.input1 or i.output == si.input2) and si.type != "OR":
                wrong.add(i.output)
    if i.type == "XOR":
        for si in instructions2:
            if (i.output == si.input1 or i.output == si.input2) and si.type == "OR":
                wrong.add(i.output)

print(",".join(sorted(wrong)))