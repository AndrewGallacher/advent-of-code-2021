# Day 5

def get_dangerous_point_count(field, min_overlap_count):
    dangerous_point_count = 0
    for row in field:
        for cell in row:
            if cell >= min_overlap_count:
                dangerous_point_count += 1

    return dangerous_point_count

def is_horizontal(vent_line):
    if vent_line[0][0] == vent_line[1][0]:
        return True

    return False

def is_vertical(vent_line):
    if vent_line[0][1] == vent_line[1][1]:
        return True
    
    return False

def update_field_with_vent_line(field, vent_line):

    # Get co-ordinates of first point
    x = vent_line[0][0]
    y = vent_line[0][1]

    # Get offset to second point
    x_offset = 0
    if vent_line[1][0] > x:
        x_offset = 1
    elif vent_line[1][0] < x:
        x_offset = -1

    y_offset = 0
    if vent_line[1][1] > y:
        y_offset = 1
    elif vent_line[1][1] < y:
        y_offset = -1

    finished = False
    while not finished:
        print('x', x, 'y', y)
        field[x][y] += 1 
        if x == vent_line[1][0] and y == vent_line[1][1]:
            finished = True
        else:
            x += x_offset
            y += y_offset

    return

#---------------------------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = map(lambda line: line.replace('\n', '').strip(), input.readlines())

field_size = 0
vent_lines = []
for line in input_lines:
    print (line)
    
    vent_line = []
    for point in line.split('->'):
        x = int(point.split(',')[0])
        y = int(point.split(',')[1])
        vent_line.append([x, y])

        if x > field_size:
            field_size = x
        if y > field_size:
            field_size = y

    vent_lines.append(vent_line)

print(vent_lines)
print(field_size)

field = []
for x in range(field_size + 1):
    row = []
    for y in range(field_size + 1):
        row.append(0)
    field.append(row)

for vent_line in vent_lines:
    #if is_vertical(vent_line) or is_horizontal(vent_line): 
    update_field_with_vent_line(field, vent_line)

print(field)

dangerous_point_count = get_dangerous_point_count(field, 2)
print('dangerous_point_count:', dangerous_point_count)
