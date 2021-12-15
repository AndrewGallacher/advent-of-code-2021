# Day 14 

def read_input(filename):
    input = open(filename, 'r')
    input_lines = []
      
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

filename = 'test.txt'
filename = 'input.txt'
input_lines = read_input(filename)
print(input_lines)

# Parse the polymer template
polymer_template = input_lines.pop(0)
print('polymer template: ', polymer_template)

# Count the pairs
pair_count = {}
for i in range(len(polymer_template) - 1):
    pair = polymer_template[i : i + 2]
    print(pair)
    if not pair in pair_count:
        pair_count[pair] = 0
    pair_count[pair] += 1
    
print('Initial pair count:', pair_count)

# Parse the rules
rules = {}
for line in input_lines:
    if line.strip() != '':
        data = line.split('->')
        source = data[0].strip()
        target = data[1].strip()
        rules[source] = target

print('Rules:', rules)

step = 0
while step < 40:
    step += 1

    # Clone the pair count
    new_pair_count = {}
    for pair in pair_count:
        new_pair_count[pair] = pair_count[pair]  

    for pair in pair_count:
        if pair in rules:
            # Work out the two pairs that this pair will result in
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]

            # Ensure the new pairs are in the collection
            if not new_pair_1 in new_pair_count:
                new_pair_count[new_pair_1] = 0
            if not new_pair_2 in new_pair_count:
                new_pair_count[new_pair_2] = 0
                
            # Update the new counts
            new_pair_count[pair] -= pair_count[pair]
            new_pair_count[new_pair_1] += pair_count[pair]
            new_pair_count[new_pair_2] += pair_count[pair]
      
    pair_count = {}
    for pair in new_pair_count:
        pair_count[pair] = new_pair_count[pair]

print('Pair counts:', pair_count)

# Since all pairs overlap this will double count
# Except for the first and last 
# So set those to one and half the final results
letter_count = {}
letter_count[polymer_template[0]] = 1
letter_count[polymer_template[len(polymer_template) - 1]] = 1
for pair in pair_count:
    letter_1 = pair[0]
    letter_2 = pair[1]

    if not letter_1 in letter_count:
        letter_count[letter_1] = 0
    if not letter_2 in letter_count:
        letter_count[letter_2] = 0

    letter_count[letter_1] += pair_count[pair]
    letter_count[letter_2] += pair_count[pair]
        
# define the most and least common - they will be set to values that exist
most_common = 0
least_common = 0
 
# Now halve the results
for letter in letter_count:
    count = int(letter_count[letter] / 2) 
    letter_count[letter] = count
    most_common = count
    least_common = count

print(letter_count)
  
for key in letter_count:
    print(letter_count[key])
    if letter_count[key] > most_common:
        most_common = letter_count[key] 
    if letter_count[key] < least_common:
        least_common = letter_count[key] 

print('Answer:', most_common - least_common, (most_common - least_common) == 2188189693529)
