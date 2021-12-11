# Day 9 

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
   
def is_low_point(heightmap, row, column):

    height = heightmap[row][column]

    if row > 0:
        if heightmap[row - 1][column] <= height:
            return False

    if column > 0:
        if heightmap[row][column - 1] <= height:
            return False

    if row < len(heightmap) - 1:
         if heightmap[row + 1][column] <= height:
            return False       

    if column < len(heightmap[0]) - 1:
         if heightmap[row][column + 1] <= height:
            return False  

    return True

def get_basin(heightmap, row, column):
    return []

# -------------------

heightmap = parse_input('input.txt')
heightmap = parse_input('test.txt')
format_heightmap(heightmap)

total_risk = 0

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if is_low_point(heightmap, i, j):
            print(i, j, 'is a lowpoint:', heightmap[i][j])
            total_risk += heightmap[i][j] + 1

print('total risk:', total_risk)


