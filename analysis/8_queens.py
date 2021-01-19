import random

max_bounds = 8

def show_board(locations):
    max_x = max(locations, key=lambda x_y: x_y[0])[0]
    max_y = max(locations, key=lambda x_y: x_y[1])[1]
    board = [['.' for x in range(0, max_y + 1)] for y in range(0, max_x + 1)]
    for index, locations in enumerate(locations):
        board[locations[0]][locations[1]] = str(index)
    row_strings = ['  '.join(row) for row in board]
    for row in row_strings:
        print(row)

def calc_cost(locations):
    cost = []
    for index_1, location_1 in enumerate(locations): 
        for index_2, location_2 in enumerate(locations):
            if index_1 != index_2:
                if location_1[0] == location_2[0] or location_1[1] == location_2[1] or abs((location_2[0]-location_1[0])/(location_2[1]-location_1[1])) == 1:
                    if (index_2, index_1) not in cost:
                        cost.append((index_1, index_2))
            else:
                continue
    return len(cost)

def random_optimizer(number_of_iterations):
    random_locations = []
    for _ in range(0, number_of_iterations):
        random_n_locations = []
        for _ in range(0,9):
            random_n_locations.append((random.randint(0,max_bounds), random.randint(0,max_bounds)))
        random_locations.append(random_n_locations)
    costs_of_random_locations = [(locations, calc_cost(locations)) for locations in random_locations]
    minimum_locations = min(costs_of_random_locations, key=lambda x: x[1])
    return {'locations': minimum_locations[0], 'cost': minimum_locations[1]}

def steepest_descent_optimizer_2(number_of_iterations):
    optimized_locations = random_optimizer(number_of_iterations)
    translations = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]
    for _ in range(number_of_iterations):
        random_locations = random_optimizer(number_of_iterations)
        for translation in translations:
            for random_index_1 in range(len(random_locations['locations'])):
                new_locations = [location if random_index_2 != random_index_1 and in_bounds(location, translation) else (location[0]+translation[0], location[1]+translation[1]) for random_index_2, location in enumerate(random_locations['locations'])]
                cost = calc_cost(new_locations)
                if (cost < optimized_locations['cost']):
                    optimized_locations['locations'] = new_locations
                    optimized_locations['cost'] = cost
    return optimized_locations

def in_bounds(location, translation):
    return location[0]+translation[0] >= 0 and location[1]+translation[1] >= 0 and location[0]+translation[0] >= max_bounds and location[1]+translation[1] >= max_bounds
 
locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
show_board(locations)
print('\ncalc_cost(locations)', calc_cost(locations))
print('\nrandom_optimizer(10)', random_optimizer(10))
print('\nrandom_optimizer(50)', random_optimizer(50))
print('\nrandom_optimizer(100)', random_optimizer(100))
print('\nrandom_optimizer(500)', random_optimizer(500))
print('\nrandom_optimizer(1000)', random_optimizer(1000))
print('\nsteepest_descent_optimizer(10)', steepest_descent_optimizer_2(10))
print('\nsteepest_descent_optimizer(50)', steepest_descent_optimizer_2(50))
print('\nsteepest_descent_optimizer(100)', steepest_descent_optimizer_2(100))
print('\nsteepest_descent_optimizer(500)', steepest_descent_optimizer_2(500))
print('\nsteepest_descent_optimizer(1000)', steepest_descent_optimizer_2(1000))
