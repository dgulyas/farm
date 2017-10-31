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
		w, h = 40, 15;
		self.map = [[" " for x in range(w)] for y in range(h)]
	
	def __getitem__(self, key):
		return self.map[key]
		
	def __str__(self):
		str = ""
		for row in self.map:
			for cell in row:
				str += cell
			str += "\n"
		return str
		
def RunWorld():
	
	map = Map()
	#print(map)
	
	animals = []
	for i in range(10):
		animals.append(wo.Animal(x=2*i, y=2*y)
		
	world = World()
	animal = wo.Animal(x=10, y=8, char="a")
	world.animals.append()
	
	while True:
		#need to tick the animals and then have them write to the map, unless we do collision detection.
		#what if two animals on top of eachother. The second one dies and that square is erased, erasing the second one.
		world.display()
		time.sleep(2)
		world.tick()
		
if __name__ == "__main__":
    RunWorld()