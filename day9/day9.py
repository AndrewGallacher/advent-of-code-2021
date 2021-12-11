# Day 9 
 
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def parse_input(filename):
    heightmap = []

    input = open(filename, 'r')
      
    for line in input.readlines():
        line = line.replace('\n', '').strip()
        line_array = []
        for char in line:
            line_array.append(int(char))    
        heightmap.append(line_array)    

    # Make sure we have some data
    if len(heightmap) == 0:
        raise Exception('No input')

    # Make sure the map is consistent
    standard_row_size = len(heightmap[0])
    for row in heightmap:
        if len(row) != standard_row_size:
            raise Exception('Inconsistent row size')

    return heightmap

def format_heightmap(heightmap):
    for row in heightmap:
        print("".join(map(lambda i: str(i), row))) 
   
def is_low_point(heightmap, point):

    height = heightmap[point.x][point.y]

    for adjacent_point in get_adjacent_points(heightmap, point):
        if heightmap[adjacent_point.x][adjacent_point.y] <= height:
            return False

    return True

def get_adjacent_points(heightmap, point):
    points = []

    if point.x > 0:
        points.append(Point(point.x - 1, point.y))
        
    if point.y > 0:
        points.append(Point(point.x, point.y - 1))
         
    if point.x < len(heightmap) - 1:
        points.append(Point(point.x + 1, point.y))
         
    if point.y < len(heightmap[0]) - 1:
        points.append(Point(point.x, point.y + 1))
         
    return points

def get_basin(heightmap, basin, point):
 
    for adjacent_point in get_adjacent_points(heightmap, point):
        if heightmap[adjacent_point.x][adjacent_point.y] < 9 and not (adjacent_point in basin):
            basin.append(adjacent_point)
            basin = get_basin(heightmap, basin, adjacent_point)
             
    return basin

# -------------------

#heightmap = parse_input('test.txt')
heightmap = parse_input('input.txt')
format_heightmap(heightmap)

total_risk = 0
basin_sizes = []

for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        if is_low_point(heightmap, Point(x, y)):
            print(x, y, 'is a lowpoint:', heightmap[x][y])
            total_risk += heightmap[x][y] + 1

            basin = []
            basin.append(Point(x, y))
            basin = get_basin(heightmap, basin, Point(x, y))
            basin_sizes.append(len(basin))

print('total risk:', total_risk)

basin_sizes.sort()
print('Basin sizes:', basin_sizes)
 
# Find largest 3
while len(basin_sizes) > 3:
    basin_sizes.pop(0)
 
product = 1
for basin_size in basin_sizes:
    product *= basin_size

print(product)
