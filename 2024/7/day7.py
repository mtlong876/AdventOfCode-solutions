def isValid(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    if isValid(target,[nums[0]+nums[1]] + nums[2:]):
        return True
    if isValid(target,[nums[0]*nums[1]] + nums[2:]):
        return True
    return False

def isValid2(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    if isValid2(target,[nums[0]+nums[1]] + nums[2:]):
        return True
    if isValid2(target,[nums[0]*nums[1]] + nums[2:]):
        return True
    if isValid2(target,[int(str(nums[0])+str(nums[1]))] + nums[2:]):
        return True
    return False

input = open('input.txt','r')
tv = []
eq = []
total = 0
total2 = 0
for line in input:
    tv.append(int(line.strip().split(":")[0]))
    eq.append([int(x) for x in line.strip().split(":")[1].split()])

for i in range(len(tv)):
    if isValid(tv[i],eq[i]):
        total+=tv[i]
    if isValid2(tv[i],eq[i]):
        total2+=tv[i]
print(total)
print(total2)