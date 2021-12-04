x = open('test.txt', 'r')
x = open('input.txt', 'r')

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

    #print('rrbcv', column, value, newList)

    return newList

def oxygen_generator_rating(list):
    digitLength = getDigitLength(list)

    newList = list[:]
    for column in range(digitLength):
        most_common_digit = get_most_common_value(newList, column)
        newList = keep_rows_with_column_value(newList, column, most_common_digit)

    return newList[0]

def co2_scrubber_rating(list):
    digitLength = getDigitLength(list)
    # print('2', list)

    newList = list[:]
    column = 0
    while len(newList) > 1:
        if column > digitLength:
            raise Exception('We have run out of digits')

        least_common_digit = get_least_common_value(newList, column)
        #print (column + 1, newList, least_common_digit)
        newList = keep_rows_with_column_value(newList, column, least_common_digit)
        #print(column + 1, newList)
        column += 1

    return newList[0]
                
print('BEFORE')
print(i_a)

oxygen_generator_rating_binary = oxygen_generator_rating(i_a)
co2_scrubber_rating_binary = co2_scrubber_rating(i_a)

print('AFTER')
print('oxygen_generator_rating (binary)', oxygen_generator_rating_binary)
print('co2_scrubber_rating (binary)', co2_scrubber_rating_binary)

oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)
co2_scrubber_rating_decimal = int(co2_scrubber_rating_binary, 2)
#print(dec_mc * dec_lc)
print('oxygen_generator_rating (decimal)', oxygen_generator_rating_decimal)
print('co2_scrubber_rating (decimal)', co2_scrubber_rating_decimal)

print('RESULT:', oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)
