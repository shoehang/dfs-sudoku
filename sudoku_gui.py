import pygame

class box():
	def __init__(self, x, y, width, height, color, text):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text = text

	def getText(self):
		return self.text

	def setText(self, newText):
		self.text = newText

	def setNext(self):
		if (self.text == 0):
			self.text = 1
		elif (self.text == 1):
			self.text = 2
		elif (self.text == 2):
			self.text = 3
		elif (self.text == 3):
			self.text = 4
		elif (self.text == 4):
			self.text = 5
		elif (self.text == 5):
			self.text = 6
		elif (self.text == 6):
			self.text = 7
		elif (self.text == 7):
			self.text = 8
		elif (self.text == 8):
			self.text = 9
		elif (self.text == 9):
			self.text = 0				

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))
		font = pygame.font.SysFont('comicsans', 30)
		text = font.render(str(self.text), 1, (0,0,0))
		canvas.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))

	def hover(self, pos):
		if (pos[0] > self.x and pos[0] < self.x + self.width):
			if (pos[1] > self.y and pos[1] < self.y + self.height):
				return True
		return False