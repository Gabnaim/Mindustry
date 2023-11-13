import math
import time
from scene import *
import numpy as np
from threading import Thread

IMAGESIZE = 176
SCALE = 4
BLOCKSIZE = 16
DISPLAYMARGIN = 30
displaySize = IMAGESIZE * SCALE
pixelSize = SCALE
size = IMAGESIZE // BLOCKSIZE

rectSize = math.floor(BLOCKSIZE * 1)
blockCenter = math.floor((BLOCKSIZE - rectSize) / 2)

slowDown = 1e-4
pixels = np.full((IMAGESIZE, IMAGESIZE, 4),(0.0, 0.0, 1.0, 1.0))

def generateBlock(imgX, imgY):	
	r = np.random.random()
	g = np.random.random()
	b = np.random.random()
	blockSpiral = Spiral(BLOCKSIZE)
	while not blockSpiral.atEnd():
		time.sleep(slowDown)
		i, j = blockSpiral.next()
		pixels[imgX + i, imgY + j] = (r, g, b, 1)
	
class Spiral:
	def __init__(self, size):
		self.size = size
		self.midX = size // 2
		self.midY = math.ceil(size / 2 - 1)
		self.x = self.midX
		self.y = self.midY
		self.yDir = 0
		self.xDir = 1 if (size % 2 == 1) else -1
		
	def atEnd(self):
		return self.x >= self.size or self.y >= self.size
		
	def getDirection(self):
		# direction changes
		if self.x == self.y and self.y <= self.midY: # up
			self.xDir, self.yDir = 0, 1
		elif self.x == (self.y + 1) and self.y >= self.midY: #down
			self.xDir, self.yDir = 0, -1
		elif (self.x + self.y) == (self.size - 1):
			if self.y >= self.midY: #right
				self.xDir, self.yDir = 1, 0
			else: # left
				self.xDir, self.yDir = -1, 0
		
	def next(self):
		if self.atEnd():
		 return None
		value = self.x, self.y
		self.x += self.xDir
		self.y += self.yDir
		self.getDirection()
		return value

spiral = Spiral(size)	
def generateImage():
	while not spiral.atEnd():
		x, y = spiral.next()
		generateBlock(x * BLOCKSIZE, y * BLOCKSIZE)
			
class ImageRender(Scene):
	def draw(self):
		background('white')
		fill('blue')
		rect(DISPLAYMARGIN, DISPLAYMARGIN, displaySize, displaySize)
		for px in range(IMAGESIZE):
			for py in range(IMAGESIZE):
				color = pixels[px, py]
				fill(tuple(color))
				rect(px * SCALE + DISPLAYMARGIN, py * SCALE + DISPLAYMARGIN, pixelSize, pixelSize)
				
def showImage():
	run(ImageRender())
	
t1 = Thread(target=generateImage)
t2 = Thread(target=showImage)

t1.start()
t2.start()

