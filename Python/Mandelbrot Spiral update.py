import math
import time
from scene import *
import numpy as np
from threading import Thread

IMAGESIZE = 176
BLOCKSIZE = 16

MAXITER = 200
VIEWSIZE = 2
OFFSET = (-0.5, 0)

pixels = np.full((IMAGESIZE, IMAGESIZE, 4),(0.0, 0.0, 1.0, 1.0))

class Mandel:
	def __init__(self, viewSize, offset, maxIter, imageSize):
		self.viewSize = viewSize
		self.offsetX = offset[0] - viewSize / 2
		self.offsetY = offset[1] - viewSize / 2
		self.maxIter = maxIter
		self.imageSize = imageSize
		self.step = viewSize / imageSize
		self.colorStep = 1 / maxIter
		self.slowDown = 1e-4 / maxIter

	def mandel(self, x0, y0):
		zR = 0
		zI = 0
		for i in range(self.maxIter):
			zRSquared = zR * zR
			zISquared = zI * zI
			zI = 2 * zR * zI + y0
			zR = zRSquared - zISquared + x0
			
			if zRSquared + zISquared > 4:
				return i
		return self.maxIter
	
	def generateBlock(self, imgX, imgY, blockSize):
		imgX *= blockSize
		imgY *= blockSize
		blockSpiral = Spiral(blockSize)
		real = self.offsetX + imgX * self.step
		imag = self.offsetY + imgY * self.step
		while not blockSpiral.atEnd():
			time.sleep(self.slowDown)
			i, j = blockSpiral.next()
			mb = self.mandel(real + i * self.step, imag + j * self.step)
			if mb == self.maxIter:
				pixels[imgX + i, imgY + j] = (0, 0, 0, 1)
			else:
				pixels[imgX + i, imgY + j] = (0, mb * self.colorStep, 1, 1) 
		
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

def generateFractal():
	numBlocks = IMAGESIZE // BLOCKSIZE
	spiral = Spiral(numBlocks)
	mandel = Mandel(viewSize = VIEWSIZE,
									offset = OFFSET,
									maxIter = MAXITER,
									imageSize = IMAGESIZE)
	while not spiral.atEnd():
		x, y = spiral.next()
		mandel.generateBlock(x, y, BLOCKSIZE)
		
class ImageRender(Scene):
	def setup(self):
		self.imageSize = IMAGESIZE
		self.scale = 4
		self.margin = 30
		self.displaySize = self.imageSize * self.scale
		
	def draw(self):
		background('white')
		fill('blue')
		rect(self.margin, self.margin, self.displaySize, self.displaySize)
		for px in range(self.imageSize):
			for py in range(self.imageSize):
				color = pixels[px, py]
				fill(tuple(color))
				rect(px * self.scale + self.margin, py * self.scale + self.margin, self.scale, self.scale)
				
def showImage():
	run(ImageRender())
	
t1 = Thread(target=generateFractal)
t2 = Thread(target=showImage)

t1.start()
t2.start()

