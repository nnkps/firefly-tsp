#!/usr/bin/python3

from fireflies import *
import random
import matplotlib.pyplot as plt

def draw(points):
	points = list(points)
	points = points + points[:1]
	(x, y) = zip(*points)
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.show()

if __name__ == '__main__':
	number_of_points = int(input('Number of points: '))
	next_random = lambda: random.random() * 100
	locations = [ (next_random(), next_random()) for i in range(number_of_points) ]
	draw(locations)
	
	solver = TSPSolver(locations)
	new_order = solver.run()
	
	new_locations = [locations[i] for i in new_order]
	draw(new_locations)
	# solver.run(number_of_individuals=30)