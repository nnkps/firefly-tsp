from NearestNeighborHeuristic import NearestNeighborHeuristic
from NearestInsertionHeuristic import NearestInsertionHeuristic

class NearestInsertion:

	def __init__(self, cities):
		self.oldni = NearestInsertionHeuristic(cities)

	def generate_population(self, limit):
		population_of_solutions = self.oldni.GenerateSolutions(limit)
		return [[city.index for city in solution] for solution in population_of_solutions]


class NearestNeighbour:

	def __init__(self, cities):
		self.oldnn = NearestNeighborHeuristic(cities)

	def generate_population(self, limit):
		return self.oldnn.GenerateSolutions(limit)