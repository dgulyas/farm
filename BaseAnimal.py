from BaseThing import BaseThing

class BaseAnimal(BaseThing):
	def __init__(self, map, point, speed = 1, char = "a"):
		super().__init__(map = map, point=point)
		self.speed = speed
		self.char = char
	
	def moveTo(self, point):
		self.map.get(self.coord).value = None
		self.coord = point
		self.map.get(self.coord).value = self