import math
import random

class RandomNumberGenerator:
	def __init__(self):
		pass
	
	def GetRandomIntWithLimit(self, limit):
		return math.floor(random.random() * limit)