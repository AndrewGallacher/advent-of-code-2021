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

    min_x = min(vent_line[0][0], vent_line[1][0])
    max_x = max(vent_line[0][0], vent_line[1][0])
    min_y = min(vent_line[0][1], vent_line[1][1])
    max_y = max(vent_line[0][1], vent_line[1][1])
    
    print(min_x, max_x, min_y, max_y)

    for x in range(min_x - 1, max_x):
        for y in range(min_y - 1, max_y):
            print(x, y)
            field[x][y] += 1

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
for x in range(field_size):
    row = []
    for y in range(field_size):
        row.append(0)
    field.append(row)

for vent_line in vent_lines:
    if is_vertical(vent_line) or is_horizontal(vent_line): 
        update_field_with_vent_line(field, vent_line)

print(field)

dangerous_point_count = get_dangerous_point_count(field, 2)
print('dangerous_point_count:', dangerous_point_count)


 
