# FIRST project
# For solving N-ything problem, a modified version of N-Queens problem
# Genetic Algorithm

from copy import deepcopy
from random import randint, uniform
from time import time, sleep
from math import exp
from operator import itemgetter
from typing import List, Tuple

from board import Board


# Type aliases
Population = List[Tuple[Board, int]]


def calculate_fitness(board: Board, max_cost: int) -> int:
    """Calculate the fitness of a board configuration."""
    return (max_cost - board.calculate_cost()) ** 3


def init_population(board: Board, population_count: int, max_cost: int) -> Population:
    """Initialize populiation with <population_count> random boards."""
    population = []
    for i in range(population_count):
        new_board = deepcopy(board)
        new_board.randomize_pieces()
        population.append((new_board, calculate_fitness(new_board, max_cost)))
    return population


def select_from_dist(prob_dist: List[float]) -> int:
    """Select an index randomly from a probability distribution."""
    x = uniform(0.0, 1.0)
    assert(x <= 1.0 and prob_dist[-1] == 1.0)
    for i in range(len(prob_dist)):
        if x < prob_dist[i]:
            return i


def combine(population: Population, max_cost: int) -> Population:
    """Generate the next generation of population by cross-over."""
    new_population = []
    piece_count = len(population[0][0].pieces)
    total_fitness = sum(fitness for _, fitness in population)
    selection_prob_dist = []
    
    for idx, (sample, fitness) in enumerate(population):
        selection_prob_dist.append((fitness / total_fitness) + \
                (selection_prob_dist[idx - 1] if idx > 0 else 0))
    selection_prob_dist[-1] = 1.0
    
    for i in range(len(population)):
        parent_1_idx, parent_2_idx = select_from_dist(selection_prob_dist), \
                select_from_dist(selection_prob_dist)
        parent_1_pieces = deepcopy(population[parent_1_idx][0].pieces)
        parent_2_pieces = deepcopy(population[parent_2_idx][0].pieces)
        combination_boundary_idx = randint(0, piece_count)
        new_board = deepcopy(population[parent_1_idx][0])
        new_board.pieces = parent_1_pieces[:combination_boundary_idx] + \
                parent_2_pieces[combination_boundary_idx:]
        
        while new_board.have_conflicts():
            combination_boundary_idx = (combination_boundary_idx - 1) % (piece_count + 1)
            new_board.pieces = parent_1_pieces[:combination_boundary_idx] + \
                    parent_2_pieces[combination_boundary_idx:]
        new_population.append((new_board, calculate_fitness(new_board, max_cost)))
    
    return new_population


def mutate(population: Population, probability: float, max_cost: int) -> Population:
    """Randomly change the location of one chess piece from <probability> of the population."""
    for i in range(len(population)):
        if uniform(0.0, 1.0) < probability:
            population[i][0].mutate()
            population[i] = (population[i][0], calculate_fitness(population[i][0], max_cost))
    return population


def solve_genetic(board: Board) -> None:
    """Solve the N-ything problem with genetic algorithm."""
    max_num_generations = int(input('Enter maximum number of generations: '))
    population_count = int(input('Enter number of sample population in every generation: '))
    mutation_probability = float(input('Enter sample mutation probability: '))
    
    best_config = None
    best_fitness = None
    best_avg_fitness = None
    start_time = time()

    max_cost = board.calculate_max_cost()
    population = init_population(board, population_count, max_cost)

    for i in range(max_num_generations):
        print('Generation {}:'.format(i))
        
        population = combine(population, max_cost)
        population = mutate(population, mutation_probability, max_cost)
        
        curr_best_config, curr_best_fitness = max((config for config in population), key=itemgetter(1))
        curr_best_avg_fitness = sum(fitness for _, fitness in population) / population_count
        print(' - Average population fitness: {}'.format(curr_best_avg_fitness))
        print(' - Best fitness: {}'.format(curr_best_fitness))
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
    print('  > Best average population fitness:   {}'.format(best_avg_fitness))
    print('  > Best fitness:    {}'.format(best_fitness))
    print('  > Elapsed time:    {} ms'.format((time() - start_time) * 1000))
    print('\n================================================================\n')
