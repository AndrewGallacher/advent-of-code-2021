# Day 5: Hydrothermal Venture
# ---------------------------------------------------
from functions import * 

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = map(lambda line: line.replace('\n', '').strip(), input.readlines())

field_size = 0
vent_lines = []
for line in input_lines:
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
print('field size:', field_size)

field = []
for x in range(field_size + 1):
    row = []
    for y in range(field_size + 1):
        row.append(0)
    field.append(row)

for vent_line in vent_lines:
    # if is_vertical(vent_line) or is_horizontal(vent_line):
    update_field_with_vent_line(field, vent_line)

dangerous_point_count = get_dangerous_point_count(field, 2)
print('dangerous_point_count:', dangerous_point_count)
