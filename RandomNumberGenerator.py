import math
import random

class RandomNumberGenerator:
	def __init__(self):
		pass
	
	def GetRandomIntWithLimit(self, limit):
		return int(math.floor(random.random() * limit))