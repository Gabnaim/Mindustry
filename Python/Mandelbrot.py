import math
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
            return (0, math.floor(i * colorStep), 255)
    return (0,0,0)
    
img = Image.new( 'RGB', (SIZE, SIZE), "black") # create a new black image
pixels = img.load() # create the pixel map

real = xStart
imag = yStart

for x in range(SIZE):    # for every col:
    for y in range(yRange):    # For every row
        color = mandel(real, imag)
        pixels[x,y + yRange ] = color
        pixels[x,yRange - y] = color
        imag += step
    imag = yStart
    real += step

img.show()