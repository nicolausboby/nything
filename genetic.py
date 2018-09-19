# FIRST project
# For solving N-ything problem, a modified version of N-Queens problem
# Genetic Algorithm

from copy import deepcopy
from random import randint, uniform
from time import time, sleep
from math import exp
from operator import itemgetter

from board import Board


# Helpers
def max_cost(board):
    piece_count = len(board.pieces)
    assert(piece_count > 0)
    return piece_count * (piece_count - 1) if piece_count > 1 else 1


def fitness(board):
    return max_cost(board) - board.calculate_cost()


def init_population(board, population_count):
    population = []
    for i in range(population_count):
        new_board = deepcopy(board)
        new_board.randomize_pieces()
        population.append((new_board, fitness(new_board)))
    return population


def select(population):
    total_fitness = sum(fitness for _, fitness in population)
    parent_selection_dist = []
    for sample, fitness in population:
        selection_probability = round((fitness ** 2) / max_cost(population[0][0]))
        parent_selection_dist.extend([sample for i in range(selection_probability)])
    return parent_selection_dist


def combine(parent_selection_dist, population_count):
    new_population = []
    piece_count = len(parent_selection_dist[0].pieces)
    assert(piece_count > 0)
    for i in range(population_count):
        parent_1_idx, parent_2_idx = randint(0, len(parent_selection_dist) - 1), \
                randint(0, len(parent_selection_dist) - 1)
        parent_1_pieces = deepcopy(parent_selection_dist[parent_1_idx].pieces)
        parent_2_pieces = deepcopy(parent_selection_dist[parent_2_idx].pieces)
        combination_boundary_idx = randint(0, piece_count)
        new_board = deepcopy(parent_selection_dist[parent_1_idx])
        new_board.pieces = parent_1_pieces[:combination_boundary_idx] + \
                parent_2_pieces[combination_boundary_idx:]
        
        while new_board.have_conflicts():
            combination_boundary_idx = (combination_boundary_idx - 1) % (piece_count + 1)
            new_board.pieces = parent_1_pieces[:combination_boundary_idx] + \
                    parent_2_pieces[combination_boundary_idx:]
        new_population.append((new_board, fitness(new_board)))
    
    return new_population


def mutate(population, probability):
    for i in range(len(population)):
        if uniform(0.0, 1.0) < probability:
            population[i][0].mutate()
            population[i] = (population[i][0], fitness(population[i][0]))
    return population


def solution(population):
    for sample, _ in population:
        if sample.same_color_cost() == 0:
            return deepcopy(sample)
    return None


def solve_genetic(board):
    max_num_generations = int(input('Enter maximum number of generations: '))
    population_count = int(input('Enter number of sample population in every generation: '))
    mutation_probability = float(input('Enter sample mutation probability: '))
    
    best_config = None
    best_fitness = None
    best_avg_fitness = None
    start_time = time()

    population = init_population(board, population_count)
    for i in range(max_num_generations):
        print('Generation {}:'.format(i))
        
        parent_selection_dist = select(population)
        population = combine(parent_selection_dist, population_count)
        population = mutate(population, mutation_probability)
        
        curr_best_config, curr_best_fitness = max((config for config in population), key=itemgetter(1))
        curr_best_avg_fitness = sum(fitness for _, fitness in population) / population_count
        print(' - Average population fitness: {}'.format(curr_best_avg_fitness))
        print(' - Best fitness: {}'.format(curr_best_fitness))
        print(' - Best board configuration:')
        print()
        
        if best_config is None:
            best_config = curr_best_config
            best_fitness = curr_best_fitness
            best_avg_fitness = curr_best_avg_fitness
        else:
            if curr_best_fitness > best_fitness:
                best_config = curr_best_config
                best_fitness = curr_best_fitness
            if curr_best_avg_fitness > best_avg_fitness:
                best_avg_fitness = curr_best_avg_fitness

    print('\nBEST SOLUTION:\n')
    best_config.print_board()
    print('\n================================================================')
    print('\n---------------------- GENETIC ALGORITHM -----------------------\n')
    print('Generation(s):    {}'.format(max_num_generations))
    print('\nRESULT:')
    print('  > best population average fitness:   {}'.format(best_avg_fitness))
    print('  > best fitness:    {}'.format(best_fitness))
    print('  > elapsed time:    {} ms'.format((time() - start_time) * 1000))
    print('\n================================================================\n')
