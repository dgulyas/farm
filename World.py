import os
import sys
import time
from Animal import Animal
from Map import Map

def RunWorld(numAnimals = 100):
	
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
		sys.stdout.write("time:" + str(tickNumber) + " open space:" + str(map.numOpenCells()))
		sys.stdout.flush()
		
		time.sleep(0.2)
		
		deadThings = []
		for animal in animals:
			animal.tick()
			if animal.deleteMe:
				deadThings.append(animal)
		
		for thing in deadThings:
			map.get(thing.coord).value = None
			if isinstance(thing, Animal):
				animals.remove(thing)
		
if __name__ == "__main__":
	
	RunWorld()