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

def RunWorld(numAnimals = 80):
	
	#print("test")
	map = Map()
	#print(map)
	
	animals = []
	for i in range(numAnimals):
		openPoint = map.randOpenPoint()
		animal = Animal(map, openPoint)
		animals.append(animal)
		map.get(openPoint).value = animal
	
	tickNumber = 0
	
	while True:
		tickNumber += 1
		os.system('clear')
		sys.stdout.write(map.__str__())
		sys.stdout.write(str(tickNumber) + " " + str(len(animals)))
		sys.stdout.flush()
		
		time.sleep(2)
		
		deadThings = []
		for animal in animals:
			animal.tick()
			if animal.deleteMe:
				deadThings.append(animal)
		
		for thing in deadThings:
			map.get(thing.coord).value = None
			if isinstance(thing, Animal):
				animals.remove(thing)
		
		
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