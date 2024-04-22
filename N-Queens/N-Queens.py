# Name: Jared Schneider 
# Program Description: Genetic Algorithm Solution to the N-Queens problem. 
# Note: At bottom of file can change values board_size, pop_size, mutation_rate, max_generations,and trials
# to experiment with different results. 
# Compile: "python N-Queens.py"
# 

import random

# initialize the population with random solutions
def initialize_population(pop_size, board_size):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, board_size - 1) for _ in range(board_size)]
        population.append(chromosome)
    return population

# calculates the number of pairs of queens that threaten each other in a given solution.
def fitness(chromosome):
    conflicts = 0
    board_size = len(chromosome)
    for i in range(board_size):
        for j in range(i + 1, board_size):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    return conflicts

#selects new parents
def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        selected = random.choice(population)
        parents.append(selected)
        population.remove(selected)
    return parents

#performs crossover operation
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

#swap the positions of two queens in a random column.
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome

#prints the board of the found solution
def print_board(chromosome):
    board_size = len(chromosome)
    for row in range(board_size):
        line = ""
        for col in range(board_size):
            if chromosome[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

#1.Initialize a population of random valid solutions.
#2.Evaluate the fitness of each solution.
#3.Select parents for reproduction based on their fitness
#4.Apply crossover and mutation to create a new population.
#5.Repeat steps 2-4 for a fixed number of generations or until a solution with fitness 0 is found.
def genetic_algorithm(board_size, pop_size, mutation_rate, max_generations):
    population = initialize_population(pop_size, board_size)
    for generation in range(max_generations):
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            print("Solution found in generation", generation)
            print_board(population[0])
            return population[0], generation
        parents = select_parents(population, pop_size // 2)
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        population = next_generation

    return None, max_generations

if __name__ == "__main__":
    board_size = 8 # Change this for different board sizes
    pop_size = 1000
    mutation_rate = 0.01
    max_generations = 10000

    trials = 100
    total_generations = 0

    for _ in range(trials):
        solution, generations = genetic_algorithm(board_size, pop_size, mutation_rate, max_generations)
        total_generations += generations

    avg_generations = total_generations / trials
    print(f"Average generations to solve {board_size}-queens problem: {avg_generations:.2f}")
