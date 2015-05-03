from City import *
import sys
import random
# import matplotlib.pyplot as plt

class NearestInsertionHeuristic():
	def __init__(self, cities):
		self.cities = [city for city in cities]
		self.numberOfCities = len(cities)
		for i in range(self.numberOfCities):
			self.cities[i].index = i

	def GenerateSolutions(self, numberOfSolutions):
		solutions = []
		for i in range(numberOfSolutions):
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
				
			#for i in range(self.numberOfCities):
				#if isCityAdded[i] == False:
					#x2.append(self.cities[i].x)
					#y2.append(self.cities[i].y)
			
			#plt.scatter(x, y)
			#plt.scatter(x2, y2)
			#plt.plot(x, y)
			#plt.plot(x2, y2, 'ro')
			#plt.show()
						
			while self.AllCitiesAdded(isCityAdded) == False:
				bestDistance = sys.maxsize
				tmpDistance = 0
				cityToAddIndex = 0
				
				for i in range(self.numberOfCities):
					if isCityAdded[i] == False:
						for j in range(numberOfCitiesInSolution):
							tmpDistance = self.cities[i].GetDistanceToCity(solution[j])
							if tmpDistance < bestDistance:
								bestDistance = tmpDistance
								cityToAddIndex = i
				
				indexToInsert = 0
				bestGrowth = sys.maxsize
				tmpBestGrowth = 0
				
				for i in range(numberOfCitiesInSolution):
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
					
				#for i in range(self.numberOfCities):
					#if isCityAdded[i] == False:
						#x2.append(self.cities[i].x)
						#y2.append(self.cities[i].y)
				
				#plt.scatter(x, y)
				#plt.scatter(x2, y2)
				#plt.plot(x, y)
				#plt.plot(x2, y2, 'ro')
				#plt.show()
							
			#solution.append(solution[0])
			# solutions.append([elem.index for elem in solution])
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
			
	def PutThreeRandomCitiesToTheBack(self):
		firstIndex = random.randint(0, self.numberOfCities - 1)
		secondIndex = random.randint(0, self.numberOfCities - 2)
		thirdIndex = random.randint(0, self.numberOfCities - 3)
		
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