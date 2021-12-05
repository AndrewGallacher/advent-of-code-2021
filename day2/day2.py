
# ----------------------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')

instructions = []
for line in input.readlines():
    instructions.append(line)

aim = 0
horizontal = 0
depth = 0

print(instructions)

for instruction in instructions:
    command = instruction.split(' ')[0]
    value = int(instruction.split(' ')[1])

    if command == 'forward':
        horizontal += value
        depth += aim * value
    elif command == 'up':
        aim -= value
    elif command == 'down':
        aim += value
    else:
        raise Exception('Invalid command ' + command)

print('----------')
print('Horizontal:', horizontal)
print('Depth:', depth) 
print('Score:', horizontal * depth)
