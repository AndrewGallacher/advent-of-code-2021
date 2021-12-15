# Day 13

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def get_points(filename):
    points = []
    
    input = open(filename, 'r')
      
    for line in input.readlines():
        if ',' in line:
            coordinates = line.replace('\n', '').strip().split(',')
            points.append(Point(int(coordinates[0]), int(coordinates[1]))) 

    return points

def get_folds(filename):
    folds = []

    input = open(filename, 'r')
      
    for line in input.readlines():
        if 'fold along' in line:
            data = line.replace('fold along', '').replace('\n', '').strip().split('=') 
            folds.append(data)
            
    return folds    

def count_points(points):
    return len(points)

def fold_along_x(points, x):
    points_to_move = []
    for point in points: 
        if point.x > x:
            points_to_move.append(point)

    for point in points_to_move:
        points.remove(point)
        new_point = Point(2 * x - point.x, point.y)
        if not new_point in points:
            points.append(new_point)

def fold_along_y(points, y):
    points_to_move = []
    for point in points: 
        if point.y > y:
            points_to_move.append(point)

    for point in points_to_move:
        points.remove(point)
        new_point = Point(point.x, 2 * y - point.y)
        if not new_point in points:
            points.append(new_point)

def display_points(points):
    size = 0
    for point in points:
        if point.x > size:
            size = point.x
        if point.y > size:
            size = point.y
            
    for y in range(size + 1):
        line = ''
        for x in range(size + 1):
            point = Point(x, y)
            if point in points:
                line += '#'
            else:
                line += ' '

        if line.strip() != '':
            print(line)

# --------------------------------------

filename = 'test.txt'
filename = 'input.txt'
points = get_points(filename)
print(points)

folds = get_folds(filename)
print(folds)

print('Count before:', len(points))

for fold in folds:
    if fold[0] == 'y':
        fold_along_y(points, int(fold[1]))
    elif fold[0] == 'x':
        fold_along_x(points, int(fold[1]))
    else:
        raise Exception('Invalid instruction')

print('Count after:', len(points))

print()
display_points(points)
print()
