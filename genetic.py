# FIRST project
# For solving N-ything problem, a modified version of N-Queens problem
# Genetic Algorithm

from copy import deepcopy
from random import randint
from time import time


# Helpers
def max_cost(population):
    piece_count = len(population[0][0].pieces)
    assert(piece_count > 0)
    return piece_count * (piece_count - 1) if piece_count > 1 else 1


def fitness(cost, population):
    return max_cost(population) - cost


def init_population(board, population_count):
    population = []
    for i in range(population_count):
        new_board = deepcopy(board)
        new_board.randomize_pieces()
        population.append((new_board, new_board.calculate_cost()))
    return population


def select(population):
    total_fitness = sum(fitness(cost, population) for _, cost in population)
    selection_dist = []
    new_population = []
    for sample, cost in population:
        selection_dist.extend([(sample, cost) for i in range(fitness(cost, population))])
    for i in range(len(population)):
        selection_idx = randint(0, total_fitness - 1)
        new_population.append(selection_dist[selection_idx])
    
    # print(len(population))
    # print(len(new_population))
    # print(sum(cost for _, cost in population))
    # print(sum(cost for _, cost in new_population))
    
    return new_population


def combine(population):
    piece_count = len(population[0][0].pieces)
    new_population = []
    for i in range(len(population)):
        new_board = deepcopy(population[i][0])
        parent_1_idx, parent_2_idx = randint(0, len(population) - 1), randint(0, len(population) - 1)
        assert(piece_count > 0)
        combination_boundary_idx = randint(1, piece_count - 1)
        new_board.pieces = population[parent_1_idx][0].pieces[:combination_boundary_idx] + \
                population[parent_2_idx][0].pieces[combination_boundary_idx:]

        # print(combination_boundary_idx)
        # print(population[parent_1_idx][0].pieces)
        # print(population[parent_2_idx][0].pieces)
        # print(new_board.pieces)
        # print('---')

        new_population.append((new_board, new_board.calculate_cost()))

    # print(len(population))
    # print(len(new_population))
    # print(sum(cost for _, cost in population))
    # print(sum(cost for _, cost in new_population))
    
    return new_population


def mutate(population):
    for i in range(len(population)):
        population[i][0].mutate()
        population[i] = (population[i][0], population[i][0].calculate_cost())

    # print(len(population))
    # print(sum(cost for _, cost in population))

    return population


def solution(population):
    for sample, _ in population:
        if sample.diff_color_point() == 0:
            return deepcopy(sample)
    return None


def solve_genetic(board):
    max_num_generations = int(input('enter maximum number of generations: '))
    population_count = int(input('enter number of sample population in every generation: '))
    success_count = 0
    first_success = None
    first_success_found_at = 0
    best_cost = None
    best_avg_cost = None
    start_time = time()

    population = init_population(board, population_count)
    for i in range(max_num_generations):
        population = select(population)
        population = combine(population)
        population = mutate(population)
        
        curr_best_cost = min(cost for _, cost in population)
        curr_best_avg_cost = sum(cost for _, cost in population) / population_count
        print('best cost: {}'.format(curr_best_cost))
        print('average population cost: {}'.format(curr_best_avg_cost))
        
        if best_cost is None:
            best_cost = curr_best_cost
            best_avg_cost = curr_best_avg_cost
        else:
            if curr_best_cost < best_cost:
                best_cost = curr_best_cost
            if curr_best_avg_cost < best_avg_cost:
                best_avg_cost = curr_best_avg_cost

        if solution(population) is not None:
            success_count += 1
            if first_success is None:
                first_success = solution(population)
                first_success_found_at = i + 1
            print('solution found')
        
        print()

    if first_success:
        print('\n')
        first_success.print_board()
        print('\n\n================================================================')
        print('\n---------------------- GENETIC ALGORITHM ----------------------\n')
        print('Generation(s):    {}'.format(max_num_generations))
        print('Solution found:   {} times, first found at generation {}'.format(success_count, first_success_found_at))
        print('\nFINAL RESULT:')
        print('  > best population average cost:   {}'.format(best_avg_cost))
        print('  > best cost:    {}'.format(best_cost))
        print('  > elapsed time: {} ms'.format((time() - start_time) * 1000))
        print('\n================================================================\n')
    else:
        print('\nNO SOLUTION FOUND')
        print('\n================================================================')
        print('\n---------------------- GENETIC ALGORITHM ----------------------\n')
        print('Generation(s):    {}'.format(max_num_generations))
        print('Solution found:   none')
        print('\nFINAL RESULT:')
        print('  > best population average cost:   {}'.format(best_avg_cost))
        print('  > best cost:    {}'.format(best_cost))
        print('  > elapsed time: {} ms'.format((time() - start_time) * 1000))
        print('\n================================================================\n')
