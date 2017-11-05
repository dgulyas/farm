import random
from BaseThing import BaseThing

class Animal(BaseThing):
	def __init__(self, map, point, hunger = 1, speed = 1, fullness = 30, char = "a"):
		super().__init__(map = map, point=point)
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
		possibleLocations = self.map.getOpenNeighbourPoints(self.coord)
		if len(possibleLocations) == 0:
			return
		
		self.map.get(self.coord).value = None
		self.coord = random.choice(possibleLocations)
		self.map.get(self.coord).value = self
		
		
		'''
		reachableFood = world.getReachableFood(self.coord)
		if reachableFood is not None:
			reachableFood.reduce()
			fullness += 5
		else:
			nearestFood = world.getNearestFood(self.coord)
			self.moveTowards(nearestFood)
		
		
	def moveTowards(point):
		xDiff = self.coord.x - point.x
		yDiff = self.coord.y - point.y
		if abs(xDiff) > abs(yDiff):
			if xDiff < 0:
				self.coord.x += 1
			else:
				self.coord.x -= 1
		else:
			if yDiff < 0:
				self.coord.y += 1
			else:
				self.coord.y -= 1
		map.cell(self.coord).value = self
		#how to remove it from the map if it's dead.
		#if I was fancy there would be collision detection here, or some kind of random path logic
		'''