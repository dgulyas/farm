import random
from MapCell import MapCell
from Point import Point

class Map():

	def __init__(self):
		self.width, self.height = 60, 30
		self.map = [[MapCell(Point(x,y), None) for x in range(self.width)] for y in range(self.height)]
	
	#This doesn't work because you can't pass objects into [] :(
	#def __getitem__(self, point):
	#	return self.map[point.y][point.x]
	
	def get(self, point):
		return self.map[point.y][point.x]
	
	def __str__(self):
		string = ""
		for row in self.map:
			for cell in row:
				#string += "(" + str(cell.point.x) + "," + str(cell.point.y) + ")"
				string += " " if cell.value is None else str(cell.value.char)
			string += "\n"
		return string
	
	def randOpenPoint(self):
	#This doesn't scale well past ~85% full
		point = self.randPoint()
		while self.get(point).value != None:
			point = self.randPoint()
		return point
	
	def randPoint(self):
		return Point(random.randint(0,self.width-1), random.randint(0,self.height-1))
	
	def getOpenNeighbourPoints(self, point):
		openNeighbourPoints = []
		for neighbourPoint in point.surroundingPoints(point):
			if self.pointInsideMap(neighbourPoint) and self.get(neighbourPoint).value is None:
				openNeighbourPoints.append(neighbourPoint)
		return openNeighbourPoints
		
			
	def pointInsideMap(self, point):
		return point.x > 0 and point.x < self.width and point.y > 0 and point.y < self.height
	
	def numOpenCells(self):
		result = 0
		for row in self.map:
			for cell in row:
				if cell.value is None:
					result += 1
		return result