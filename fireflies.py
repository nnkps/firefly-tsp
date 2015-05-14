import random
import math
import itertools
import operator
from heuristics import NearestInsertion, NearestNeighbour
import collections

def cartesian_distance(a, b):
	"a and b should be tuples, computes distance between two cities"
	return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def compute_distances_matrix(locations):
	"returns array with distances for given points"
	return [[cartesian_distance(a, b) for a in locations] for b in locations]

def random_permutation(iterable, r=None):
	"returns new tuple with random permutation of iterable"
	pool = tuple(iterable)
	r = len(pool) if r is None else r
	return list(random.sample(pool, r))

def single_path_cost(path, distances):
	"returns total distance of path"
	path = list(path)
	path = path + path[:1]
	return sum(distances[ path[i] ][ path[i + 1] ] for i in range(len(path) - 1))

def hamming_distance_with_info(a, b):
	"return number of places and places where two sequences differ"
	assert len(a) == len(b)
	ne = operator.ne
	differ = list(map(ne, a, b))
	return sum(differ), differ

def hamming_distance(a, b):
	dist, info = hamming_distance_with_info(a, b)
	return dist

# def hamming_distance(a, b):
# 	"return number of places where two sequences differ"
# 	return sum(sequences_differ(a, b))


class TSPSolver():
	def __init__(self, points):
		"points is list of objects of type City"
		self.weights = compute_distances_matrix(points)
		self.indexes = range(len(points))
		self.population = []
		self.light_intensities = []
		self.best_solution = None
		self.best_solution_cost = None
		self.n = None

		self.first_heuristic = NearestNeighbour(points)
		self.second_heuristic = NearestInsertion(points)

	def f(self, individual): # our objective function? lightness?
		"objective function - describes lightness of firefly"
		return single_path_cost(individual, self.weights)

	def determine_initial_light_intensities(self):
		"initializes light intensities"
		self.light_intensities = [self.f(x) for x in self.population]

	def generate_initial_population(self, number_of_individuals, heuristics_percents,):
		"generates population of permutation of individuals"
		# TODO: this part is wrong!
		# heuristics return solutions, while we need list of permutations of indexes

		first_heuristic_part_limit = int(heuristics_percents[0] * number_of_individuals)
		second_heuristic_part_limit = int(heuristics_percents[1] * number_of_individuals)
		random_part_limit = number_of_individuals - first_heuristic_part_limit - second_heuristic_part_limit

		first_heuristic_part = self.first_heuristic.generate_population(first_heuristic_part_limit)
		second_heuristic_part = self.second_heuristic.generate_population(second_heuristic_part_limit)
		random_part = [random_permutation(self.indexes) for i in range(random_part_limit)]

		self.population = random_part + first_heuristic_part + second_heuristic_part

	def find_global_optimum(self):
		"finds the brightest firefly"
		index = self.light_intensities.index(min(self.light_intensities))
		self.best_solution = self.population[index]
		self.best_solution_cost = single_path_cost(self.best_solution, self.weights)

	def move_individual(self, a, b):
		"moving a solution to b solution"
		# UGLY :(
		# will rewrite later
		distance, diff_info = hamming_distance_with_info(self.population[a], self.population[b])
		subset_to_change = lambda seq: [seq[i] for i in self.indexes if diff_info[i]]

		subset_of_a = subset_to_change(self.population[a])
		subset_of_b = subset_to_change(self.population[b])

		def shuffle_subset():
			random_index = random.randint(0, len(subset_of_b) - 1)
			value_to_copy = subset_of_b[random_index]

			index_to_move = subset_of_a.index(value_to_copy)
			subset_of_a[random_index] = value_to_copy
			subset_of_a[index_to_move], subset_of_a[random_index] = subset_of_a[random_index], subset_of_a[index_to_move]
#			random.shuffle(subset_of_a) # shuffles subset of a in place
			return hamming_distance_with_info(subset_of_a, subset_of_b)

		new_distance, new_info = shuffle_subset()
		while new_distance < 2 or new_distance > distance:
			new_distance, new_info = shuffle_subset()

		changed_individual = []
		for i in self.indexes:
			if not diff_info[i]:
				el = self.population[a][i]
			else:
				el = subset_of_a.pop(0)
			changed_individual.append(el)

		self.population[a] = changed_individual

	def move_firefly(self, a, r):
		number_of_swaps = random.randint(2, r)
		for i in range(number_of_swaps):
			random_index = lambda: random.randint(0, len(self.population[a]) - 1) 
			index1 = random_index()
			index2 = random_index()
			self.population[a][index1], self.population[a][index2] = self.population[a][index2], self.population[a][index1]

	def rotate_single_solution(self, i, value_of_reference):
		point_of_reference = self.population[i].index(value_of_reference)
		self.population[i] = collections.deque(self.population[i])
		self.population[i].rotate(point_of_reference + 1)
		self.population[i] = list(self.population[i])

	def rotate_solutions(self, value_of_reference):
		# TODO 
		for i in range(1, len(self.population)):
			self.rotate_single_solution(i, value_of_reference)

	def I(self, index, gamma, r):
		return self.light_intensities[index] * math.exp(gamma * r**2)

	def run(self, number_of_individuals=25, iterations=200, heuristics_percents=(0.2, 0.7, 0.1), beta=20, gamma=0.1):
		"gamma is parameter for light intensities, beta is size of neighbourhood according to hamming distance"
		# hotfix, will rewrite later
		self.best_solution = random_permutation(self.indexes)
		self.best_solution_cost = single_path_cost(self.best_solution, self.weights)

		self.generate_initial_population(number_of_individuals, heuristics_percents)
		value_of_reference = self.population[0][0]
		self.rotate_solutions(value_of_reference)
		self.determine_initial_light_intensities()

		# print('Population of {0} individuals:'.format(number_of_individuals))

		self.find_global_optimum()
		# print(self.best_solution)
		# print(single_path_cost(self.best_solution, self.weights))

		individuals_indexes = range(number_of_individuals)
		self.n = 0
		while self.n < iterations:  # other stop conditions?
			for i in individuals_indexes:
				for j in individuals_indexes:
					r = hamming_distance(self.population[i], self.population[j])
					# if self.I(i, r) < self.I(j, r) and r < beta:
					if self.I(i, gamma, r) > self.I(j, gamma, r) and r < beta:
						self.move_individual(i, j) # move i to j
						# self.move_firefly(i, r)
						self.rotate_single_solution(i, value_of_reference)
						self.light_intensities[i] = self.f(self.population[i])
			self.find_global_optimum()
			self.n += 1

		# print(self.best_solution)
		# print(single_path_cost(self.best_solution, self.weights))
		return self.best_solution
