# Day 11

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def parse_input(filename):
    cavern = []

    input = open(filename, 'r')
      
    for line in input.readlines():
        line = line.replace('\n', '').strip()

        row = []
        for char in line:
            row.append(int(char))
        
        cavern.append(row)

    if len(cavern) == 0:
        raise Exception('No input')
 
    standard_length = len(cavern[0])
    for row in cavern:
        if len(row) != standard_length:
            raise Exception('Inconsistent size')

    return cavern

def format_cavern(cavern):
    for row in cavern:
        print("".join(map(lambda i: str(i), row))) 

def get_adjacent_points(cavern, flashing_point):
    adjacent_points = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            x = flashing_point.x + x_offset
            y = flashing_point.y + y_offset
            if (x_offset == 0 and y_offset == 0):
                continue
            if flashing_point.x + x_offset < 0 or flashing_point.x + x_offset > len(cavern) - 1:
                continue
            if flashing_point.y + y_offset < 0 or flashing_point.y + y_offset > len(cavern[flashing_point.x]) - 1:
                continue
            adjacent_points.append(Point(x, y))

    return adjacent_points

def apply_step(cavern):
    flashers = []
    flashing_points = []
    for x in range(len(cavern)):
        flashers_row = []
        for y in range(len(cavern[x])):
            cavern[x][y] += 1
            if cavern[x][y] > 9:
                flashers_row.append(1)
                flashing_points.append(Point(x, y))
            else:
                flashers_row.append(0)
        flashers.append(flashers_row)

    while len(flashing_points) > 0:
        new_flashing_points = []
        for flashing_point in flashing_points:
            for point in get_adjacent_points(cavern, flashing_point):
                # print(point.x, point.y)
                cavern[point.x][point.y] += 1
                if cavern[point.x][point.y] > 9 and flashers[point.x][point.y] == 0:
                    flashers[point.x][point.y] = 1
                    new_flashing_points.append(point)
        flashing_points = new_flashing_points[:]
    
    # Reset energy level to 0 for flashers
    flash_count = 0
    for x in range(len(cavern)):
        for y in range(len(cavern[x])):
            if flashers[x][y] == 1:
                cavern[x][y] = 0
                flash_count += 1

    return flash_count

# ------------------------------------

cavern = parse_input('test.txt')
cavern = parse_input('input.txt')
print('initial')
format_cavern(cavern)
print()

total_flash_count = 0
step = 0
while step < 1000:
    step += 1
    flash_count = apply_step(cavern)
    total_flash_count += flash_count
    print('step', step, flash_count)
    format_cavern(cavern)
    print()
    if flash_count == 100:
        break

print('total energy:', total_flash_count)
