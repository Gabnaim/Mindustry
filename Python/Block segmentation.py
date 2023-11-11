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
blockOffset = BLOCKSIZE * SCALE

slowDown = 0.05
pixels = np.zeros((IMAGESIZE, IMAGESIZE))

def generateImage():
	imgX = imgY = 0
	for col in range(cols):
		for row in range(rows):
			time.sleep(slowDown)
			pixels[imgX, imgY] = 1
			imgY += BLOCKSIZE
		imgX += BLOCKSIZE
		imgY = 0
			
			
class ImageRender(Scene):
	def draw(self):
		background('white')
		fill('blue')
		rect(MARGIN, MARGIN, displaySize, displaySize)
		for px in range(IMAGESIZE):
			for py in range(IMAGESIZE):
				colorValue = pixels[px, py]
				fill(0, colorValue, 1)
				rect(px * SCALE + MARGIN, py * SCALE + MARGIN, pixelSize, pixelSize)
				
def showImage():
	run(ImageRender())
	
t1 = Thread(target=generateImage)
t2 = Thread(target=showImage)

t1.start()
t2.start()

