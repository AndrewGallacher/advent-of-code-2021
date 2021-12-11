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

    return None

def complete(line):
    """ Auto-complete """
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
                raise Exception('Invalid delimiter')

    return parser

def get_auto_complete_increment(score, char):
    
    increment = 0
    if char == ')':
        increment = 1
    elif char == ']':
        increment = 2
    elif char == '}':
        increment = 3
    elif char == '>':
        increment = 4
    else:
        raise Exception('Invalid character ' + char)

    return score * 5 + increment

# ---------- ---------- ---------- ----------

lines = parse_input('test.txt')
lines = parse_input('input.txt')

syntax_error_score = 0
incomplete_lines = []
for line in lines:
    invalid_char = validate(line)
    if invalid_char == ')':
        syntax_error_score += 3
    elif invalid_char == ']':
        syntax_error_score += 57
    elif invalid_char == '}':
        syntax_error_score += 1197
    elif invalid_char == '>':
        syntax_error_score += 25137
    else:
        incomplete_lines.append(line)

print('Syntax error score:', syntax_error_score)

auto_complete_scores = []
for incomplete_line in incomplete_lines:
    auto_complete_score = 0
    tail = complete(incomplete_line)
    print(tail)

    while len(tail) > 0:
        char = tail.pop()
        incomplete_line += char

        auto_complete_score = get_auto_complete_increment(auto_complete_score, char)
       
    print('Auto-complete score:', auto_complete_score)
    auto_complete_scores.append(auto_complete_score)

auto_complete_scores.sort()

while len(auto_complete_scores) > 2:
    auto_complete_scores.pop()
    auto_complete_scores.pop(0)
    
if len(auto_complete_scores) > 1:
    raise Exception('Failed to find middle score')

print('Middle score:', auto_complete_scores[0])
