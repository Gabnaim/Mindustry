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

pixels = np.full((IMAGESIZE, IMAGESIZE, 4),(0.0, 0.0, 1.0, 1.0))

MAXITER = 20
VIEWSIZE = 2
OFFSET = Point(-0.5, 0)
mbStep = VIEWSIZE / IMAGESIZE
colorStep = 1 / MAXITER
slowDown = 1e-4 / MAXITER

def mandel(x0,y0):
	zR = 0
	zI = 0
	for i in range(MAXITER):
		zRSquared = zR * zR
		zISquared = zI * zI
		zI = 2 * zR * zI + y0
		zR = zRSquared - zISquared + x0
		
		if zRSquared + zISquared > 4:
			return i
	return MAXITER
	
def generateBlock(imgX, imgY):
	blockSpiral = Spiral(BLOCKSIZE)
	real = OFFSET.x + imgX * mbStep - VIEWSIZE / 2
	imag = OFFSET.y	+ imgY * mbStep - VIEWSIZE / 2
	while not blockSpiral.atEnd():
		time.sleep(slowDown)
		i, j = blockSpiral.next()
		mb = mandel(real + i * mbStep, imag + j * mbStep)
		if mb == MAXITER:
			pixels[imgX + i, imgY + j] = (0, 0, 0, 1)
		else:
			pixels[imgX + i, imgY + j] = (0, mb * colorStep, 1, 1) 
		
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

