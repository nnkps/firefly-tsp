from City import *
import random
import sys
import matplotlib.pyplot as plt

class NearestNeighborHeuristic():
	def __init__(self, cities):
		self.cities = cities
		self.numberOfCities = len(cities)

	def GenerateSolutions(self, numberOfSolutions):
		solutions = []
		for i in range(numberOfSolutions):
			solution = []
			isCityAdded = []
			firstCityIndex = 0
			lastCityAdded = None
			
			self.InitTabWithValue(isCityAdded, self.numberOfCities, False)
				
			firstCityIndex = random.randint(0, self.numberOfCities - 1)
			solution.append(self.cities[firstCityIndex])
			lastCityAdded = self.cities[firstCityIndex]
			isCityAdded[firstCityIndex] = True
			
			while self.AllCitiesAdded(isCityAdded) == False:
				bestDistance = sys.maxsize
				tmpDistance = 0
				bestCityIndex = 0
				
				for i in range(self.numberOfCities):
					if isCityAdded[i] == False:
						tmpDistance = self.cities[i].GetDistanceToCity(lastCityAdded)
						if tmpDistance < bestDistance:
							bestDistance = tmpDistance
							bestCityIndex = i
							
				solution.append(self.cities[bestCityIndex])
				lastCityAdded = self.cities[bestCityIndex]
				isCityAdded[bestCityIndex] = True
				
			#solution.append(self.cities[firstCityIndex])
			solutions.append(solution)
			
		return solutions
			
	def AllCitiesAdded(self, cities):
		for x in cities:
			if(x == False):
				return False
		return True
		
	def InitTabWithValue(self, tab, tabLength, value):
		for i in range(tabLength):
			tab.append(value)
			
if __name__ == '__main__':
	cities = []
	for i in range(10):
		cities.append(City(random.random() * 100, random.random() * 100))
	heuristic = NearestNeighborHeuristic(cities)
	solutions = heuristic.GenerateSolutions(10)
	for i in solutions:
		x = []
		y = []
		for j in i:
			x.append(j.x)
			y.append(j.y)
		plt.scatter(x, y)
		plt.plot(x, y)
		plt.show()