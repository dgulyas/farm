import os
import sys
import time
from Animal import Animal
from Food import Food
from Map import Map

def RunWorld(numAnimals = 100, numFood = 15):
	
	#print("test")
	map = Map()
	#print(map)
	
	animals = []
	for i in range(numAnimals):
		openPoint = map.randOpenPoint()
		animal = Animal(map, openPoint)
		animals.append(animal)
		map.get(openPoint).value = animal
	
	foods = []
	for i in range(numFood):
		openPoint = map.randOpenPoint()
		food = Food(map, openPoint)
		foods.append(food)
		map.get(openPoint).value = food
		
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
		for food in foods:
			food.tick()
			if food.deleteMe:
				deadThings.append(food)
		
		for thing in deadThings:
			map.get(thing.coord).value = None
			if isinstance(thing, Animal):
				animals.remove(thing)
			if isinstance(thing, Food):
				foods.remove(thing)
		
if __name__ == "__main__":
	
	RunWorld()