input = open('test.txt', 'r')
input = open('input.txt', 'r')

value = []
for line in input.readlines():
    value.append(int(line))

print(value)

count = 0
for index in range(3, len(value)):
    if value[index] > value[index - 3]:
        count += 1

print (count) 
