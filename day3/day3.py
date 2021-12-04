x = open('input.txt', 'r')
x = open('test.txt', 'r')

i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

# test = 5 long
# input = 12 long

print(i_a)
mc = [0] * len(i_a[0])
lc = [0] * len(i_a[0])

# If same, return 1
def get_most_common_value(list, column):
    ones = 0
    zeros = 0
    for item in list:
        if int(item[column]) == 1:
            ones += 1
        else:
            zeros += 1            
    if zeros > ones:
        return 0
    return 1

# If same, return 0
def get_least_common_value(list, column):
    ones = 0
    zeros = 0
    for item in list:
        if int(item[column]) == 1:
            ones += 1
        else:
            zeros += 1            
    if ones < zeros:
        return 1
    return 0

mc = ''
lc = ''

for i in range(len(i_a[0])):
    answer = get_most_common_value(i_a, i)
    mc = mc + str(answer)
    lc = lc + str(1 - answer) 

# new_i_a = i_a[:]

# Part2
def getDigitLength(list):
    if len(list) == 0:
        return 0

    digitLength = len(list[0])

    for item in list:
        if len(item) != digitLength:
            raise Exception('Inconsistent digit length')

    return digitLength

def keep_rows_with_column_value(list, column, value):
    newList = []
    for item in list:
        if int(item[column]) == value:
            newList.append(item)

    return newList

def get_rating(list, get_value):
    digitLength = getDigitLength(list)

    newList = list[:]
    column = 0
    while len(newList) > 1:
        if column > digitLength:
            raise Exception('We have run out of digits')

        value = get_value(newList, column)
        newList = keep_rows_with_column_value(newList, column, value)
        column += 1

    return newList[0]    

print('BEFORE')
print(i_a)

oxygen_generator_rating_binary = get_rating(i_a, get_most_common_value)
co2_scrubber_rating_binary = get_rating(i_a, get_least_common_value)

print('AFTER')
print('oxygen_generator_rating (binary)', oxygen_generator_rating_binary)
print('co2_scrubber_rating (binary)', co2_scrubber_rating_binary)

oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)
co2_scrubber_rating_decimal = int(co2_scrubber_rating_binary, 2)
#print(dec_mc * dec_lc)
print('oxygen_generator_rating (decimal)', oxygen_generator_rating_decimal)
print('co2_scrubber_rating (decimal)', co2_scrubber_rating_decimal)

print('RESULT:', oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)
