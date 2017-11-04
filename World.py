import os
import sys
import time
from Animal import Animal
from Map import Map

'''
class World():
	def __init__(self):
		# Creates the world map, which is printed to the console
		w, h = 8, 5;
		map = [[0 for x in range(w)] for y in range(h)] 
		
	
	def tick():
		for animal in animals:
			animal.Tick()
		for plant in plants:
			plant.Tick()
	
	def display():
		self.map = [[" " for x in range(w)] for y in range(h)]
		for animal in self.animals:
			map[animal.y][animal.x] = animal.char
		for plant in self.plants:
			map[plant.y][plant.x] = plant.char
		
		os.system("clear")
		for row in self.map:
			for char in row:
				print(char)
			print("\n")
	
	def getReachableFood():
		return None
	
	def getNearestFood():
		return None
		
'''

def RunWorld(numAnimals = 10):
	
	#print("test")
	map = Map()
	#print(map)
	
	animals = []
	for i in range(numAnimals):
		openPoint = map.randOpenPoint()
		animal = Animal(map, openPoint)
		animals.append(animal)
		map.get(openPoint).value = animal
	
	os.system('clear')
	sys.stdout.write(map.__str__())
	sys.stdout.flush()
	
	'''
	world = World()
	
	while True:
		#need to tick the animals and then have them write to the map, unless we do collision detection.
		#what if two animals on top of eachother. The second one dies and that square is erased, erasing the second one.
		world.display()
		time.sleep(2)
		world.tick()
	'''
if __name__ == "__main__":
	
	RunWorld()