# Day 8

def get_status(stage, patterns, possible_patterns, possible_digits):
    print('*****', stage, '*****')
    
    print()
    print('Possible patterns for each digit:')
    for i in range(10):
        print(i, possible_patterns[i])

    print()
    print('Possible digits for each pattern:')
    for pattern in patterns:
        print(pattern, possible_digits[pattern])    

def sort_segments(unsorted):
    chars = []
    for char in unsorted:
        chars.append(char)
    chars.sort()
    return "".join(chars)
 
def contains_segments(source, target):
    """ Returns true if target contains source """

    for segment in source:
        if not (segment in target):
            return False

    return True

def locate_three(patterns, possible_patterns, possible_digits):
    """ Digit 3 is the only 5-segment digit that contains all of 1 """

    pattern_for_one = possible_patterns[1][0]

    for pattern in patterns:
        if len(pattern) == 5:
            for segment in pattern_for_one:
                if not (segment in pattern):
                    # This can't be three
                    if pattern in possible_patterns[3]:
                        possible_patterns[3].remove(pattern)

    if len(possible_patterns[3]) != 1:
        raise Exception('Failed to find pattern for 3')
    pattern_for_three = possible_patterns[3][0]

    for i in range(10):
        if i == 3:
            possible_patterns[i] = [pattern_for_three]
        else:
            if pattern_for_three in possible_patterns[i]:
                possible_patterns[i].remove(pattern_for_three)

    for pattern in patterns:
        if pattern == pattern_for_three:
            possible_digits[pattern] = [3]
        else:
            if 3 in possible_digits[pattern]:
                possible_digits[pattern].remove(3)

def locate_nine(patterns, possible_patterns, possible_digits):
    """ Digit 9 is the only 6-segment digit that contains all of 3 """

    pattern_for_three = possible_patterns[3][0]

    for pattern in patterns:
        if len(pattern) == 6:
            for segment in pattern_for_three:
                if not (segment in pattern):
                    # This can't be nine
                    if pattern in possible_patterns[9]:
                        possible_patterns[9].remove(pattern)

    if len(possible_patterns[9]) != 1:
        raise Exception('Failed to find pattern for 9')
    pattern_for_nine = possible_patterns[9][0]

    for i in range(10):
        if i == 9:
            possible_patterns[i] = [pattern_for_nine]
        else:
            if pattern_for_nine in possible_patterns[i]:
                possible_patterns[i].remove(pattern_for_nine)

    for pattern in patterns:
        if pattern == pattern_for_nine:
            possible_digits[pattern] = [9]
        else:
            if 9 in possible_digits[pattern]:
                possible_digits[pattern].remove(9)

def locate_five_and_six(patterns, possible_patterns, possible_digits):
    """ Six is the only 6-segment digit that contains one of the 5-segment digits - and that is five """

    for five_segment_pattern in possible_patterns[5]:
        for six_segment_pattern in possible_patterns[6]:
            if contains_segments(five_segment_pattern, six_segment_pattern):
                possible_patterns[5] = [five_segment_pattern]
                possible_digits[five_segment_pattern] = [5]
                possible_patterns[2].remove(five_segment_pattern)    
                possible_patterns[6] = [six_segment_pattern]
                possible_digits[six_segment_pattern] = [6]
                possible_patterns[0].remove(six_segment_pattern)

                for pattern in patterns:
                    if len(possible_digits[pattern]) > 1:
                        if 5 in possible_digits[pattern]:
                            possible_digits[pattern].remove(5)
                        elif 6 in possible_digits[pattern]:
                            possible_digits[pattern].remove(6)
                        else:
                            raise Exception('Unexpected combination involving 5 & 6')  

                return

    raise Exception('Cannot find 5 and 6')

# -------------------------

def solve_patterns(patterns_input):

    patterns = patterns_input.split(' ')

    possible_patterns = []
    for i in range(10):
        possible_patterns.append([])
        patterns[i] = sort_segments(patterns[i]) 

    possible_digits = {}
    for pattern in patterns:
        possible_digits[pattern] = []
        
        if len(pattern) == 2:
            possible_patterns[1].append(pattern)
            possible_digits[pattern].append(1)
        elif len(pattern) == 3:
            possible_patterns[7].append(pattern)
            possible_digits[pattern].append(7)
        elif len(pattern) == 4:
            possible_patterns[4].append(pattern)
            possible_digits[pattern].append(4)
        elif len(pattern) == 5:
            possible_patterns[2].append(pattern)
            possible_patterns[3].append(pattern)
            possible_patterns[5].append(pattern)
            possible_digits[pattern].append(2)
            possible_digits[pattern].append(3)
            possible_digits[pattern].append(5)
        elif len(pattern) == 6:
            possible_patterns[0].append(pattern)
            possible_patterns[6].append(pattern)
            possible_patterns[9].append(pattern)
            possible_digits[pattern].append(0)
            possible_digits[pattern].append(6)
            possible_digits[pattern].append(9)
        elif len(pattern) == 7:
            possible_patterns[8].append(pattern)
            possible_digits[pattern].append(8)
        else:
            raise Exception('Invalid')

    # Initial state
    get_status('Initial', patterns, possible_patterns, possible_digits)
    
    # Locate 3: Only 5-segment that contains all of 1
    locate_three(patterns, possible_patterns, possible_digits)
    get_status('After we locate 3', patterns, possible_patterns, possible_digits)

    # Locate 9: Only 6-segment that contains all of 3
    locate_nine(patterns, possible_patterns, possible_digits)
    get_status('After we locate 9', patterns, possible_patterns, possible_digits)

    # 6 includes 5 (but we don't know what 5 is yet)
    locate_five_and_six(patterns, possible_patterns, possible_digits)
    get_status('After we locate 5 & 6', patterns, possible_patterns, possible_digits)

    # We now know what each pattern of segments means
    solution = {}
    for pattern in patterns:
        solution[pattern] = possible_digits[pattern][0]

    return solution
