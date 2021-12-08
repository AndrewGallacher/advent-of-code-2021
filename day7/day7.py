import sys 

def get_range(positions):
    range = 0
    for position in positions:
        if position > range:
            range = position
    return range

def get_fuel_consumption(positions, target):
    total_fuel = 0
    for position in positions:
        fuel = 0
        for i in range(abs(target - position) + 1):
            fuel += i

        total_fuel += fuel
    return total_fuel

# ---------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = input.readlines()

#print(input_lines)
#print(input_lines[0])

initial_positions = list(map(lambda item: int(item), input_lines[0].split(','))) 
# initial_positions = [1, 2, 3, 4]
print('Initial positions:', initial_positions)

range_of_positions = get_range(initial_positions)
print('Range:', range_of_positions)

best_fuel = sys.maxsize  # range_of_positions * len(initial_positions)
best_target = None
for target in range(range_of_positions):
    fuel = get_fuel_consumption(initial_positions, target)
    if fuel < best_fuel:
        best_fuel = fuel
        best_target = target
    print('Fuel for', target, 'is', fuel)

print('Optimal position is', best_target, 'at a cost of', best_fuel, 'fuel.')
