import os
import sys
import time
from HomingAnimal import HomingAnimal
from Map import Map
from Point import Point


def Draw():
	animals = []
	
	height = 0
	width = 0
	
	with open("C:\\work\\test.txt") as file:
		for line in file:
			height += 1
			if len(line) > width:
				width = len(line)
	
	map = Map(width = width+1, height = height)
	
	with open("C:\\work\\test.txt") as file:
		for lineNum, line in enumerate(file, 1):
			for charNum, char in enumerate(line.rstrip()):
				if char != " ":
					#print(str(charNum) + " " + str(lineNum) + " " + char)
					animal = HomingAnimal(map, map.randPoint(), Point(charNum, lineNum-1), False, char = char)
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