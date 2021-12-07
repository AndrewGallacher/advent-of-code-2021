# Day 6

def load_initial_state(initial_state):
    """ Get count of total number of fish at each stage """
    population = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in initial_state:
        population[fish] += 1

    return population

def apply_generation(population):
    """ Work out how that population changes in 1 day """
    new_population = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # First element is expired fish
    expired_fish = population[0]
    new_population[0] = 0

    for index in range(1, len(population)):
        new_population[index - 1] = population[index]

    new_population[6] += expired_fish
    new_population[8] += expired_fish

    return new_population

def count_population(population):
    count = 0
    for item in population:
        count += item

    return count

# ------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')
input_lines = input.readlines()

print(input_lines)
print(input_lines[0])

initial_state = list(map(lambda item: int(item), input_lines[0].split(',')))
population = load_initial_state(initial_state)

print('Initial state:', population)

count = 0
for generation in range(256):
    count += 1
    population = apply_generation(population)
    print('After', count, 'days:', population, '=', count_population(population))
