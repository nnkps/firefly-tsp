from NearestNeighborHeuristic import NearestNeighborHeuristic
from NearestInsertionHeuristic import NearestInsertionHeuristic

class NearestInsertion:

	def __init__(self, cities):
		self.oldni = NearestInsertionHeuristic(cities)

	def generate_population(self, limit):
		return self.oldni.GenerateSolutions(limit)


class NearestNeighbour:

	def __init__(self, cities):
		self.oldnn = NearestNeighborHeuristic(cities)

	def generate_population(self, limit):
		return self.oldnn.GenerateSolutions(limit)