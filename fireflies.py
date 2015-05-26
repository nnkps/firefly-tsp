import random
import math
import itertools
import operator
from heuristics import NearestInsertion, NearestNeighbour
import collections
import copy

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
		first_heuristic_part_limit = int(heuristics_percents[0] * number_of_individuals)
		second_heuristic_part_limit = int(heuristics_percents[1] * number_of_individuals)
		random_part_limit = number_of_individuals - first_heuristic_part_limit - second_heuristic_part_limit

		first_heuristic_part = self.first_heuristic.generate_population(first_heuristic_part_limit)
		second_heuristic_part = self.second_heuristic.generate_population(second_heuristic_part_limit)
		random_part = [random_permutation(self.indexes) for i in range(random_part_limit)]

		self.population = random_part + first_heuristic_part + second_heuristic_part
		self.absorptions = [1] * len(self.population)
		# for i in range(len(self.population)):
		# 	self.absorptions.append(random.random() * 0.9 + 0.1)

	def check_if_best_solution(self, index):
		new_cost = self.light_intensities[index]
		if new_cost < self.best_solution_cost: 
			self.best_solution = copy.deepcopy(self.population[index])
			self.best_solution_cost = new_cost

	def find_global_optimum(self):
		"finds the brightest firefly"
		index = self.light_intensities.index(min(self.light_intensities))
		self.check_if_best_solution(index)

	def move_firefly(self, a, b, r):
		"moving firefly a to b in less than r swaps"
		number_of_swaps = random.randint(0, r - 2)
		distance, diff_info = hamming_distance_with_info(self.population[a], self.population[b])

		while number_of_swaps > 0:
			distance, diff_info = hamming_distance_with_info(self.population[a], self.population[b])
			random_index = random.choice([i for i in range(len(diff_info)) if diff_info[i]])
			value_to_copy = self.population[b][random_index]
			index_to_move = self.population[a].index(value_to_copy)

			if number_of_swaps == 1 and self.population[a][index_to_move] == self.population[b][random_index] and self.population[a][random_index] == self.population[b][index_to_move]:
				break

			self.population[a][random_index], self.population[a][index_to_move] = self.population[a][index_to_move], self.population[a][random_index]
			if self.population[a][index_to_move] == self.population[b][index_to_move]:
				number_of_swaps -= 1
			number_of_swaps -= 1

		self.light_intensities[a] = self.f(self.population[a])

	def rotate_single_solution(self, i, value_of_reference):
		point_of_reference = self.population[i].index(value_of_reference)
		self.population[i] = collections.deque(self.population[i])
		l = len(self.population[i])
		number_of_rotations = (l - point_of_reference) % l
		self.population[i].rotate(number_of_rotations)
		self.population[i] = list(self.population[i])

	def rotate_solutions(self, value_of_reference):
		for i in range(1, len(self.population)):
			self.rotate_single_solution(i, value_of_reference)

	def I(self, index, r):
		return self.light_intensities[index] * math.exp(-1.0 * self.absorptions[index] * r**2)

	def run(self, number_of_individuals=100, iterations=300, heuristics_percents=(0.0, 0.0, 1.0), beta=0.7):
		"gamma is parameter for light intensities, beta is size of neighbourhood according to hamming distance"
		# hotfix, will rewrite later
		self.best_solution = random_permutation(self.indexes)
		self.best_solution_cost = single_path_cost(self.best_solution, self.weights)

		self.generate_initial_population(number_of_individuals, heuristics_percents)
		value_of_reference = self.population[0][0]
		self.rotate_solutions(value_of_reference)
		self.determine_initial_light_intensities()

		self.find_global_optimum()
		print(self.best_solution_cost)

		individuals_indexes = range(number_of_individuals)
		self.n = 0
		neighbourhood = beta * len(individuals_indexes)
		while self.n < iterations: 
			for j in individuals_indexes:
				intensities = []
				for i in individuals_indexes:
					r = hamming_distance(self.population[i], self.population[j])
					if r < neighbourhood and i != j:
						intensities.append((self.I(i, r), i, r))
				if intensities:
					best_firefly = min(intensities, key=lambda x: x[0])
					self.move_firefly(j, best_firefly[1], best_firefly[2])				
					self.check_if_best_solution(j)

			self.n += 1
			if self.n % 100 == 0:
				print(self.n)
				print(self.best_solution_cost)
		

		print(self.best_solution_cost)
		return self.best_solution
