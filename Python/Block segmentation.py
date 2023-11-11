import math
import time
from scene import *
import numpy as np
from threading import Thread

IMAGESIZE = 176
SCALE = 4
BLOCKSIZE = 16
MARGIN = 30
displaySize = IMAGESIZE * SCALE
pixelSize = SCALE
rows = cols = IMAGESIZE // BLOCKSIZE
rectSize = 14
blockCenter = math.floor((BLOCKSIZE - rectSize) / 2)


slowDown = 0.05
pixels = np.full((IMAGESIZE, IMAGESIZE, 4), (0, 0, 1, 1))

def generateImage():
	imgX = imgY = blockCenter
	for col in range(cols):
		for row in range(rows):
			time.sleep(slowDown)
			for i in range(rectSize):
				for j in range(rectSize):
					pixels[imgX + i, imgY + j] = (1, 0, 0, 1)
			imgY += BLOCKSIZE
		imgX += BLOCKSIZE
		imgY = blockCenter
			
			
class ImageRender(Scene):
	def draw(self):
		background('white')
		fill('blue')
		rect(MARGIN, MARGIN, displaySize, displaySize)
		for px in range(IMAGESIZE):
			for py in range(IMAGESIZE):
				color = pixels[px, py]
				fill(tuple(color))
				rect(px * SCALE + MARGIN, py * SCALE + MARGIN, pixelSize, pixelSize)
				
def showImage():
	run(ImageRender())
	
t1 = Thread(target=generateImage)
t2 = Thread(target=showImage)

t1.start()
t2.start()

