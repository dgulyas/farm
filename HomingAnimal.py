import random
from BaseAnimal import BaseAnimal
from Point import Point

class HomingAnimal(BaseAnimal):
	def __init__(self, map, point, destination = None, collision = True, speed = 1, char = "a"):
		super().__init__(map = map, point=point, speed=speed, char=char)
		self.destination = destination
		self.collision = collision
		self.speed = speed
		self.char = char
	
	def tick(self):
		if self.coord != self.destination:
			self.moveTowards(self.destination)
		
	def moveTowards(self, point):
		possibleMoves = []
		xDiff = point.x - self.coord.x
		yDiff = point.y - self.coord.y
		
		if xDiff != 0:
			xChange = xDiff//abs(xDiff) #xChange is -/+ 1
			possibleMove = Point.add(self.coord, Point(x = xChange))
			if self.map.get(possibleMove).value is None or not self.collision:
				possibleMoves.append(possibleMove)
		
		if yDiff != 0:
			yChange = yDiff//abs(yDiff)
			possibleMove = Point.add(self.coord, Point(y = yChange))
			if self.map.get(possibleMove).value is None  or not self.collision:
				possibleMoves.append(possibleMove)
		
		if len(possibleMoves) > 0:
			self.moveTo(random.choice(possibleMoves))