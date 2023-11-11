import math
import time
from scene import *
import numpy as np
from threading import Thread


MAXITER = 46
IMGSIZE = 32
DISPLAYSIZE = 760
VIEWSIZE = 2.5
offset = (-0.5, 0)

center = (IMGSIZE // 2, IMGSIZE // 2)
step = VIEWSIZE / IMGSIZE
realStart = offset[0] - VIEWSIZE / 2
imagStart = offset[1] - VIEWSIZE / 2
colorStep = 1 / MAXITER
pixelRange = IMGSIZE // 2
pixelSize = DISPLAYSIZE //IMGSIZE

viewSlowdown = 0.001

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
    
pixels = np.zeros((IMGSIZE, IMGSIZE))

def calcMandel():
	real = realStart
	imag = imagStart	
	
	for x in range(IMGSIZE):
		for y in range(IMGSIZE):   
			time.sleep(viewSlowdown)
			mb = mandel(real, imag)
			pixels[x,y] = mb
			#mb = mandel(real, imag)
			#pixels[x,pixelRange - y] = mb
			imag += step
		imag = imagStart
		real += step

class ImageRender(Scene):
		
	def draw(self):
		background('white')
		px = 0
		py = 0
		
		for px in range(IMGSIZE): 
			for py in range(IMGSIZE):    
				imgX = px * pixelSize
				imgY = py * pixelSize
				iter = pixels[px,py]
				if iter == MAXITER:
					fill(0,0,0,1)
				else:
					fill(0,iter/MAXITER, 1, 1)
				rect(imgX, imgY, pixelSize, pixelSize)
				
def displayImage():
	run(ImageRender())
	
t1 = Thread(target=calcMandel)
t2 = Thread(target=displayImage)
t1.start()
t2.start()

