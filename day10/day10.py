# Day 10

def parse_input(filename):
    lines = []

    input = open(filename, 'r')
      
    for line in input.readlines():
        line = line.replace('\n', '').strip()
        lines.append(line)
        
    return lines

def is_opening_delimiter(char):
    return False

def validate(line):
    """ Validate navigation commands """
    parser = []
    for char in line:
        if char == '(':
            parser.append(')')
        elif char == '[':
            parser.append(']')
        elif char == '{':
            parser.append('}')
        elif char == '<':
            parser.append('>')
        else:
            delimiter = parser.pop()
            if char != delimiter:
                return char
        print(parser)

    return None

# ---------- ---------- ---------- ----------

# lines = parse_input('test.txt')
lines = parse_input('input.txt')

score = 0
for line in lines:
    # line = '{([(<{}[<>[]}>{[]{[(<()>'
    print(line)
    invalid_char = validate(line)
    if invalid_char == ')':
        score += 3
    elif invalid_char == ']':
        score += 57
    elif invalid_char == '}':
        score += 1197
    elif invalid_char == '>':
        score += 25137

print('Score:', score)
