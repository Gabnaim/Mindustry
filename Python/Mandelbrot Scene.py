import math
import time
from scene import *
import numpy as np
from threading import Thread


MAXITER = 200
IMAGE_PIXELS = 176
DISPLAYSIZE = 704
VIEWSIZE = 2
OFFSET = Point(-0.5, 0)
PIXEL_SIZE = 4
BLOCK_SIZE = 16

imgCenter = (IMAGE_PIXELS // 2, IMAGE_PIXELS // 2)
mbStep = VIEWSIZE / IMAGE_PIXELS
#realStart = OFFSET.x - VIEWSIZE / 2
#imagStart = OFFSET.y - VIEWSIZE / 2
colorStep = 1 / MAXITER
pixelRange = IMAGE_PIXELS // 2
rows = cols = IMAGE_PIXELS // BLOCK_SIZE

viewSlowdown = 0



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
    
pixels = np.zeros((IMAGE_PIXELS, IMAGE_PIXELS))

def calcMandel():
	real = OFFSET.x
	imag = OFFSET.y	
	
	for i in range(pixelRange):
		for j in range(pixelRange):   
			time.sleep(viewSlowdown)
			mb = mandel(real, imag)
			pixels[imgCenter[0] + i, imgCenter[1] + j] = mb
			imag += mbStep		
		imag = OFFSET.y
		real += mbStep

class ImageRender(Scene):	
	def draw(self):
		background('white')
		px = 0
		py = 0
		
		for px in range(IMAGE_PIXELS): 
			for py in range(IMAGE_PIXELS):    
				imgX = px * PIXEL_SIZE - PIXEL_SIZE // 2
				imgY = py * PIXEL_SIZE - PIXEL_SIZE // 2
				iter = pixels[px,py]
				if iter == MAXITER:
					fill(0,0,0,1)
				else:
					fill(0,iter/MAXITER, 1, 1)
				rect(imgX, imgY, PIXEL_SIZE, PIXEL_SIZE)
				
def displayImage():
	run(ImageRender())
	
t1 = Thread(target=calcMandel)
t2 = Thread(target=displayImage)
t1.start()
t2.start()

