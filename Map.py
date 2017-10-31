class Map():

	def __init__(self):
		# Creates the world map, which is printed to the console
		w, h = 8, 5;
		self.map = [[" " for x in range(w)] for y in range(h)]
	
	def __getitem__(self, key):
		return self.map[key]

