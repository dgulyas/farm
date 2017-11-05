class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	#these next functions assume that 0,0 is in the upper left corner and
	#down is positive y and right is positive x
	def down(self):
		return Point(self.x, self.y + 1)
	
	def up(self):
		return Point(self.x, self.y - 1)
	
	def right(self):
		return Point(self.x + 1, self.y)
	
	def left(self):
		return Point(self.x - 1, self.y)
	
	def surroundingPoints(self, point):
		return [self.down(), self.up(), self.right(), self.left()]
	