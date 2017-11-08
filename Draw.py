import os
import sys
import time
from HomingAnimal import HomingAnimal
from Map import Map
from Point import Point


def Draw():
	map = Map()

	animals = []
	
	for i in range(10):
		animal = HomingAnimal(map, Point(1,1), Point(map.width-1,map.height-1), False)
		map.get(animal.coord).value = animal
		animals.append(animal)
	
	tickNumber = 0
	
	while True:
		tickNumber += 1
		os.system('clear')
		sys.stdout.write(map.__str__())
		sys.stdout.write("time:" + str(tickNumber) + " open space:" + str(map.numOpenCells()))
		sys.stdout.flush()
		
		time.sleep(0.2)
		
		for animal in animals:
			animal.tick()
			
			
if __name__ == "__main__":
	Draw()