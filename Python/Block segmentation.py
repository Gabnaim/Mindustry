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

slowDown = 0.05
pixels = np.full((IMAGESIZE, IMAGESIZE, 4),(0.0, 0.0, 1.0, 1.0))

def generateBlock(imgX, imgY):	
	time.sleep(slowDown)
	r = np.random.random()
	g = np.random.random()
	b = np.random.random()
	for i in range(rectSize):
		for j in range(rectSize):
			pixels[imgX + i, imgY + j] = (r, g, b, 1)
	
def spiral(size, process):
	midX = size // 2
	midY = math.ceil(size / 2 - 1)
	x = midX
	y = midY
	yDir = 0
	xDir = 1 if (size % 2 == 1) else -1
	while 0 <= x < size and 0 <= y < size:
		generateBlock(x * BLOCKSIZE, y * BLOCKSIZE)
		x += xDir
		y += yDir
		# direction changes
		if x == y and y <= midY: # up
			xDir, yDir = 0, 1
		elif x == y + 1 and y >= midY: #down
			xDir, yDir = 0, -1
		elif x + y == size - 1:
			if y >= midY: #right
				xDir, yDir = 1, 0
			else: # left
				xDir, yDir = -1, 0
				
def generateImage():
	spiral(size, generateBlock)
			
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

