class Food(BaseThing):
	def __inti__(amount = 100, char = "f"):
		self.amount = amount
		self.char = char
	
	def reduce(): #called when something takes a bite of it
		self.amount -= 1
		if self.amount < 1:
			self.deleteMe = True
	
	def tick():
		pass