import random
from BaseAnimal import BaseAnimal
from Point import Point


class Animal(BaseAnimal):
	def __init__(self, map, point, destination = None, hunger = 1, speed = 1, fullness = 30, char = "a"):
		super().__init__(map = map, point=point, speed=speed, char=char)
		self.destination = destination
		self.hunger = hunger
		self.speed = speed
		self.fullness = fullness
		self.char = char
	
	def tick(self):
		self.fullness -= self.hunger
		if self.fullness < 1:
			self.deleteMe = True
			return
		
		self.moveRandom()
		
	def moveRandom(self):
		possibleMoves = self.map.getOpenNeighbourPoints(self.coord)
		if len(possibleMoves) > 0:
			self.moveTo(random.choice(possibleMoves))
		
		'''
		reachableFood = world.getReachableFood(self.coord)
		if reachableFood is not None:
			reachableFood.reduce()
			fullness += 5
		else:
			nearestFood = world.getNearestFood(self.coord)
			self.moveTowards(nearestFood)
		'''