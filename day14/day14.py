# Day 14 

def read_input(filename):
    input_lines = []
    
    input = open(filename, 'r')
      
    for line in input.readlines():    
        input_lines.append(line.replace('\n', '').strip())

    return input_lines

def get_counts(polymer):
    counts = {}
    
    for char in polymer:
        if not char in counts:
            counts[char] = 0
        counts[char] += 1

    return counts

# ------------------------------------

filename = 'input.txt'
filename = 'test.txt'
input_lines = read_input(filename)
print(input_lines)

polymer_template = input_lines.pop(0)
print('polymer template: ', polymer_template)

# Parse the rules
rules = {}
for line in input_lines:
    if line.strip() != '':
        data = line.split('->')
        source = data[0].strip()
        target = source[0] + data[1].strip() + source[1]
        print(line, source, target)
        rules[source] = target

print(rules)

step = 0
while step < 10:
    step += 1
    result = 'X'
    for i in range(len(polymer_template) - 1):
        result = result[0 : len(result) - 1]
        pair = polymer_template[i:(i + 2)]
        if pair in rules:
            result += rules[pair]
        else:
            result += pair
    polymer_template = result
    print('After step', step, len(polymer_template))

print(len(polymer_template))
counts = get_counts(polymer_template)
print(counts)
 
most_common = 0
least_common = len(polymer_template)
for key in counts:
    print(counts[key])
    if counts[key] > most_common:
        most_common = counts[key] 
    if counts[key] < least_common:
        least_common = counts[key] 

print('Answer:', most_common - least_common)
