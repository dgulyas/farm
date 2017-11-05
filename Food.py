from BaseThing import BaseThing

class Food(BaseThing):
	def __init__(self, map, point, amount = 100, char = "f"):
		super().__init__(map = map, point=point)
		self.amount = amount
		self.char = char
	
	def reduce(self): #called when something takes a bite of it
		self.amount -= 1
		if self.amount < 1:
			self.deleteMe = True
	
	def tick(self):
		self.amount += 1