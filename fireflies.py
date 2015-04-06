import random
import math
import itertools
import operator

def cartesian_distance(a, b):
	"a and b should be tuples, computes distance between two points"
	return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def compute_distances_matrix(locations):
	"returns array with distances for given points"
	return [[cartesian_distance(a, b) for a in locations] for b in locations]

def random_permutation(iterable, r=None):
	"returns new tuple with random permutation of iterable"
	pool = tuple(iterable)
	r = len(pool) if r is None else r
	return tuple(random.sample(pool, r))

def single_path_cost(path, distances):
	"returns total distance of path"
	path = list(path)
	path = path + path[:1]
	return sum(distances[ path[i] ][ path[i + 1] ] for i in range(len(path) - 1))

def hamming_distance(a, b):
	"return number of places and places where two sequences differ"
	assert len(a) == len(b)
	ne = operator.ne
	differ = list(map(ne, a, b))
	return sum(differ), differ

# def hamming_distance(a, b):
# 	"return number of places where two sequences differ"
# 	return sum(sequences_differ(a, b))


class TSPSolver():
	def __init__(self, points):
		self.weights = compute_distances_matrix(points)
		self.indexes = range(len(points))
		self.population = []
		self.light_intensities = []
		self.best_solution = None

	def f(self, individual): # our objective function? lightness?
		return 1 / single_path_cost(individual, self.weights)

	# def lightness_function(self, gamma):  # ?
	# 	def f(i, r):
	# 		return i * math.exp(-gamma * r**2)
	# 	return f

	def determine_initial_light_intensities(self):
		self.light_intensities = [self.f(x) for x in self.population]

	def generate_initial_population(self, number_of_individuals):
		"generates population of permutation of individuals"
		self.population = [random_permutation(self.indexes) for i in range(number_of_individuals)]

	def find_global_optimum(self):
		index = self.light_intensities.index(max(self.light_intensities))
		self.best_solution = self.population[index]


	def move_individual(self, a, b):
		"moving a solution to b solution"
		# UGLY :(
		# will rewrite later
		distance, diff_info = hamming_distance(self.population[a], self.population[b])
		subset_to_change = lambda seq: [seq[i] for i in self.indexes if diff_info[i]]
		
		subset_of_a = subset_to_change(self.population[a])
		subset_of_b = subset_to_change(self.population[b])
		random.shuffle(subset_of_a) # shuffles subset of a in place
		new_distance, new_info = hamming_distance(subset_of_a, subset_of_b)
		if new_distance < 2 or new_distance > distance:
			random.shuffle(subset_of_a) # shuffles subset of a in place
			new_distance, new_info = hamming_distance(subset_of_a, subset_of_b)

		changed_individual = []
		for i in self.indexes:
			if not diff_info[i]:
				el = self.population[a][i]  
			else:
				el = subset_of_a.pop(0)
			changed_individual.append(el)
		# print(numbers_to_schuffle)
		# changed_individual = [ for i in self.indexes if not diff_info[i] else ]
		
		self.population[a] = changed_individual

	def run(self, number_of_individuals=25, alfa=random.random(), beta=1, gamma=1, iterations=200):
		"http://ijrsat.org/IJRSAT-Vol2-Issue2-0002.pdf"
		# alfa, beta, gamma - ?
		# I = self.lightness_function(gamma) ?
		self.generate_initial_population(number_of_individuals)
		self.determine_initial_light_intensities()

		print('Population of {0} individuals:'.format(number_of_individuals))

		self.find_global_optimum()
		print(self.best_solution)
		print(single_path_cost(self.best_solution, self.weights))
		
		individuals_indexes = range(number_of_individuals)
		n = 0
		while n < iterations:  # other stop conditions?
			for i in individuals_indexes:
				for j in individuals_indexes:
					if self.light_intensities[i] < self.light_intensities[j]:
						self.move_individual(i, j) # move i to j
						self.light_intensities[i] = self.f(self.population[i])
			self.find_global_optimum()
			n += 1

		print(self.best_solution)
		print(single_path_cost(self.best_solution, self.weights))
		return self.best_solution