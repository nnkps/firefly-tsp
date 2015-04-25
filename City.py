import math

class City:
	def __init__(self, x, y):
		self.x = x
		self.y = y
				
	def GetDistanceToCity(self, city):
		return math.sqrt(math.pow(self.x - city.x, 2) + math.pow(self.y - city.y, 2))
		