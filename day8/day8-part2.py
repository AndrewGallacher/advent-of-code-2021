# Day 8.2
from solver import solve_patterns, sort_segments

# -----------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = list(map(lambda line: line.replace('\n', '').strip(), input.readlines()))

total = 0
for input_line in input_lines:
    
    patterns = input_line.split('|')[0].strip() # .split(' ')
    print(patterns)

    mapping = solve_patterns(patterns)
    print(mapping)

    digits = list(map(lambda p: sort_segments(p), input_line.split('|')[1].strip().split(' ')))
    print(digits)

    result = ''
    for digit in digits:
        result = result + str(mapping[digit])
        print(result)
      
    total += int(result)

# Overall total
print('Total:', total)
