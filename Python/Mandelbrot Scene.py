import math
import time
from scene import *
import numpy as np
from threading import Thread


MAXITER = 46
PIXELSIZE = 401
VIEWSIZE = 2.5

step = VIEWSIZE / PIXELSIZE
yPxRange = PIXELSIZE // 2
realStart = -0.5 - VIEWSIZE / 2
imagStart = 0
colorStep = 1 / MAXITER

screenSize = get_screen_size()
leftBounds = (screenSize.x - PIXELSIZE)//2
bottomBounds = (screenSize.y - PIXELSIZE)//2
viewSlow = 0

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
    
pixels = np.zeros((PIXELSIZE, PIXELSIZE))

def calcMandel():
	real = realStart
	imag = imagStart	
	x = 0
	y = 0
	while x < PIXELSIZE: 
		for y in range(yPxRange):    
			mb = mandel(real, imag)
			time.sleep(viewSlow)
			pixels[x,y + yPxRange ] = mb
			pixels[x,yPxRange - y] = mb
			imag += step
		imag = imagStart
		real += step
		x += 1

    
class ImageRender(Scene):
	def setup(self):
		self.x = leftBounds
		self.y = bottomBounds
		
	def draw(self):
		background('white')
		px = 0
		py = 0
		for px in range(PIXELSIZE): 
			for py in range(PIXELSIZE):    
				iter = pixels[px,py]
				if iter == MAXITER:
					fill(0,0,0,1)
				else:
					fill(0,iter/MAXITER, 1, 1)
				rect(px,py,1,1)
				
def displayImage():
	run(ImageRender())
	
t1 = Thread(target=calcMandel)
t2 = Thread(target=displayImage)
t1.start()
t2.start()

