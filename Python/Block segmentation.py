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
rows = cols = IMAGESIZE // BLOCKSIZE

rectSize = math.floor(BLOCKSIZE * 0.75)
blockCenter = math.floor((BLOCKSIZE - rectSize) / 2)
imgCenter = IMAGESIZE // 2

slowDown = 0.05
pixels = np.full((IMAGESIZE, IMAGESIZE, 4),(0, 0, 1, 1))

mid = rows // 2

def generateBlock(imgX, imgY):	
	imgX -= blockCenter
	imgY -= blockCenter
	time.sleep(slowDown)
	for i in range(rectSize):
		for j in range(rectSize):
			pixels[imgX + i, imgY + j] = (1, 0, 0, 1)
	
def generateImage():
	generateBlock(imgCenter, imgCenter)
	for col in range(0, mid, 1):
		colOffset = col * BLOCKSIZE
		for row in range(0, mid, 1):
			rowOffset = row * BLOCKSIZE
			generateBlock(imgCenter + rowOffset, imgCenter + colOffset)
			generateBlock(imgCenter - rowOffset, imgCenter + colOffset)
			generateBlock(imgCenter + rowOffset, imgCenter - colOffset)
			generateBlock(imgCenter - rowOffset, imgCenter - colOffset)
			
			
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

