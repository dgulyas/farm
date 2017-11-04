class BaseThing:
	def __init__(self, map, point):
		self.map = map
		self.coord = point
		self.char = "x"
		self.deleteMe = False #set to true if an animal dies, food gets depleted. Object will be deleted.
