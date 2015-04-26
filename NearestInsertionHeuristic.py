from City import *
from RandomNumberGenerator import *
import sys
import matplotlib.pyplot as plt

class NearestInsertionHeuristic():
	def __init__(self, cities):
		self.cities = cities
		self.random = RandomNumberGenerator()
		self.numberOfCities = len(cities)
		
	def GenerateSolutions(self, numberOfSolutions):
		solutions = []
		for i in xrange(numberOfSolutions):
			solution = []
			isCityAdded = []
			numberOfCitiesInSolution = 3
			
			self.InitTabWithValue(isCityAdded, self.numberOfCities, False)
				
			self.PutThreeRandomCitiesToTheBack()
			self.InitSolutionWithThreeCitiesFromTheBack(solution, isCityAdded)
			
			#x = []
			#y = []
			#x2 = []
			#y2 = []
			#for j in solution:
				#x.append(j.x)
				#y.append(j.y)
				
			#for i in xrange(self.numberOfCities):
				#if isCityAdded[i] == False:
					#x2.append(self.cities[i].x)
					#y2.append(self.cities[i].y)
			
			#plt.scatter(x, y)
			#plt.scatter(x2, y2)
			#plt.plot(x, y)
			#plt.plot(x2, y2, 'ro')
			#plt.show()
						
			while self.AllCitiesAdded(isCityAdded) == False:
				bestDistance = sys.maxint
				tmpDistance = 0
				cityToAddIndex = 0
				
				for i in xrange(self.numberOfCities):
					if isCityAdded[i] == False:
						for j in xrange(numberOfCitiesInSolution):
							tmpDistance = self.cities[i].GetDistanceToCity(solution[j])
							if tmpDistance < bestDistance:
								bestDistance = tmpDistance
								cityToAddIndex = i
				
				indexToInsert = 0
				bestGrowth = sys.maxint
				tmpBestGrowth = 0
				
				for i in xrange(numberOfCitiesInSolution):
					tmpBestGrowth = self.cities[cityToAddIndex].GetDistanceToCity(solution[i - 1]) + self.cities[cityToAddIndex].GetDistanceToCity(solution[i]) - solution[i - 1].GetDistanceToCity(solution[i])
					if tmpBestGrowth < bestGrowth:
						indexToInsert = i
						bestGrowth = tmpBestGrowth
					
					
				solution.insert(indexToInsert, self.cities[cityToAddIndex])
				isCityAdded[cityToAddIndex] = True
				numberOfCitiesInSolution = numberOfCitiesInSolution + 1
				
				#x = []
				#y = []
				#x2 = []
				#y2 = []
				#for j in solution:
					#x.append(j.x)
					#y.append(j.y)
					
				#for i in xrange(self.numberOfCities):
					#if isCityAdded[i] == False:
						#x2.append(self.cities[i].x)
						#y2.append(self.cities[i].y)
				
				#plt.scatter(x, y)
				#plt.scatter(x2, y2)
				#plt.plot(x, y)
				#plt.plot(x2, y2, 'ro')
				#plt.show()
							
			#solution.append(solution[0])
			solutions.append(solution)
			
		return solutions
			
	def AllCitiesAdded(self, cities):
		for x in cities:
			if(x == False):
				return False
		return True
		
	def InitTabWithValue(self, tab, tabLength, value):
		for i in xrange(tabLength):
			tab.append(value)
			
	def PutThreeRandomCitiesToTheBack(self):
		firstIndex = self.random.GetRandomIntWithLimit(self.numberOfCities)
		secondIndex = self.random.GetRandomIntWithLimit(self.numberOfCities - 1)
		thirdIndex = self.random.GetRandomIntWithLimit(self.numberOfCities - 2)
		
		self.SwapCitiesUnderIndexes(firstIndex, self.numberOfCities - 1)
		self.SwapCitiesUnderIndexes(secondIndex, self.numberOfCities - 2)
		self.SwapCitiesUnderIndexes(thirdIndex, self.numberOfCities - 3)
	
	def SwapCitiesUnderIndexes(self, firstIndex, secondIndex):
		tmpCity = self.cities[firstIndex]
		self.cities[firstIndex] = self.cities[secondIndex]
		self.cities[secondIndex] = tmpCity
		
	def InitSolutionWithThreeCitiesFromTheBack(self, solution, isCityAdded):
		solution.append(self.cities[self.numberOfCities - 1])
		solution.append(self.cities[self.numberOfCities - 2])
		solution.append(self.cities[self.numberOfCities - 3])
		
		isCityAdded[self.numberOfCities - 1] = True
		isCityAdded[self.numberOfCities - 2] = True
		isCityAdded[self.numberOfCities - 3] = True
		
if __name__ == '__main__':
	cities = []
	for i in xrange(50):
		cities.append(City(random.random() * 100, random.random() * 100))
	heuristic = NearestInsertionHeuristic(cities)
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