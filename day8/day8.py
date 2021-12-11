# Day 8

# 0 - 6
# 1 - 2
# 2 - 5
# 3 - 5
# 4 - 4 
# 5 - 5
# 6 - 6
# 7 - 3
# 8 - 7
# 9 - 6 




# ------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
notes = list(map(lambda line: line.replace('\n', ''), input.readlines()))
print('Notes:', notes)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in notes:
    digits = line.split('|')[1].strip().split(' ')
    print(digits)

    for digit in digits:
        if len(digit) == 2:
            count[1] += 1
        if len(digit) == 4:
            count[4] += 1
        if len(digit) == 3:
            count[7] += 1
        if len(digit) == 7:
            count[8] += 1

print('1s:', count[1])
print('4s:', count[4])
print('7s:', count[7])
print('8s:', count[8])
print('-------------')
print('1, 4, 7, or 8:', count[1] + count[4] + count[7] + count[8])



