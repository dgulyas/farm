import random
import os
import time
import WorldObjects as wo
#import Map as Map

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

class Map():

	def __init__(self):
		# Creates the world map, which is printed to the console
		self.w, self.h = 40, 15; #width, height
		self.map = [[None for x in range(self.w)] for y in range(self.h)]
	
	def __getitem__(self, key):
		return self.map[key]
		
	def __str__(self):
		str = ""
		for row in self.map:
			for cell in row:
				str += " " if cell is None else cell.char
			str += "\n"
		return str
	
	def randOpenCellCoords(self):
	#This doesn't scale well past ~85% full
		h, w = self.randCellCoords()
		while self.map[h][w] != None:
			h, w = self.randCellCoords()
		return h, w
	
	def randCellCoords(self):
		return random.randint(0,self.h-1), random.randint(0,self.w-1)
		
def RunWorld(numAnimals = 10):
	
	map = Map()
	#print(map)
	
	animals = []
	for i in range(numAnimals):
		height, width = map.randOpenCellCoords()
		animal = wo.Animal(map, x=height, y=width)
		animals.append(animal)
		map[height][width] = animal #I'm not happy with storing the coords of the animal in two places.
	
	print(map)
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