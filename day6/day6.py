# Day 6


from typing import ItemsView


def apply_generation(population):
    new_population = []
    for fish in population:
        if fish == 0:
            new_population.append(6)
            new_population.append(8)
        else:
            new_population.append(fish - 1)

    return new_population

# ------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = input.readlines()

print(input_lines)
print(input_lines[0])

initial_state = list(map(lambda item: int(item), input_lines[0].split(',')))

print('Initial state:', initial_state)

count = 0
population = initial_state
for generation in range(80):
    count += 1
    population = apply_generation(population)
    print('After', count, 'days:', population, len(population))
