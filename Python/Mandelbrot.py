import math
import numpy as np
from PIL import Image

ITERATIONS = 46
SIZE = 1000
DIAMETER = 2.5

step = DIAMETER / SIZE
yRange = SIZE // 2
xStart = -0.5 - DIAMETER / 2
yStart = 0
colorStep = 255 / ITERATIONS

def mandel(x0,y0):
    zR = 0
    zI = 0
    for i in range(ITERATIONS):
        zRSquared = zR * zR
        zISquared = zI * zI
        zI = 2 * zR * zI + y0
        zR = zRSquared - zISquared + x0

        if zRSquared + zISquared > 4:
            return i     
    return ITERATIONS
    
img = Image.new( 'RGB', (SIZE, SIZE), "black") # create a new black image
pixels = img.load() # create the pixel map

real = xStart
imag = yStart

for x in range(SIZE):    # for every col:
    for y in range(yRange):    # For every row
        i = mandel(real, imag)
        color = math.floor(i * colorStep)
        pixels[x,y + yRange ] = (color, 0, 0)
        pixels[x,yRange - y] = (color, 0, 0)
        imag += step
    imag = yStart
    real += step

img.show()