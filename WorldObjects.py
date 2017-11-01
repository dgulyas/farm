class Thing:
	def __init__(self, map, x = 0, y = 0):
		self.map = map
		self.x = x
		self.y = y
		self.char = "x"
		self.deleteMe = False #set to true if an animal dies, food gets depleted. Object will be deleted.

class Animal(Thing):
	def __init__(self, map, hunger = 1, speed = 1, fullness = 30, char = "a", x = 0, y = 0):
		super().__init__(map = map, x=x, y=y)
		self.hunger = hunger
		self.speed = speed
		self.fullness = fullness
		self.char = char
	
	def tick(world):
		self.fullness -= hunger
		if fullness < 1:
			self.deleteMe = True
		
		reachableFood = world.getReachableFood(self.x, self.y)
		if reachableFood is not None:
			reachableFood.reduce()
			fullness += 5
		else:
			nearestFood = world.getNearestFood(self.x, self.y)
			self.moveTowards(nearestFood)
		
	def moveTowards(thing):
		xDiff = self.x - thing.x
		yDiff = self.y - thing.y
		if abs(xDiff) > abs(yDiff):
			if xDiff < 0:
				self.x += 1
			else:
				self.x -= 1
		else:
			if yDiff < 0:
				self.y += 1
			else:
				self.y -= 1
		map[self.y][self.x] = self.char
		#how to remove it from the map if it's dead.
		#if I was fancy there would be collision detection here, or some kind of random path logic
		

class Food(Thing):
	def __inti__(amount = 100, char = "f"):
		self.amount = amount
		self.char = char
	
	def reduce(): #called when something takes a bite of it
		self.amount -= 1
		if self.amount < 1:
			self.deleteMe = True
	
	def tick():
		pass
	