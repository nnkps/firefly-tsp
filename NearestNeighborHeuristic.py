from City import *
import random
import sys

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
			# solution.append(self.cities[firstCityIndex])
			solution.append(firstCityIndex)
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
							
				# solution.append(self.cities[bestCityIndex])
				solution.append(bestCityIndex)
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