import math
from PIL import Image

MAXITER = 46
PIXELSIZE = 1001
VIEWSIZE = 2.5

step = VIEWSIZE / PIXELSIZE
yPxRange = PIXELSIZE // 2
realStart = -0.5 - VIEWSIZE / 2
imagStart = 0
colorStep = 255 / MAXITER

def mandel(x0,y0):
    zR = 0
    zI = 0
    for i in range(MAXITER):
        zRSquared = zR * zR
        zISquared = zI * zI
        zI = 2 * zR * zI + y0
        zR = zRSquared - zISquared + x0

        if zRSquared + zISquared > 4:
            return (0, math.floor(i * colorStep), 255)
    return (0,0,0)
    
img = Image.new( 'RGB', (PIXELSIZE, PIXELSIZE), "black") # create a new black image
pixels = img.load() # create the pixel map

real = realStart
imag = imagStart
x = 0
y = 0

while x < PIXELSIZE: # for every col:
    for y in range(yPxRange):    # For every row
        color = mandel(real, imag)
        pixels[x,y + yPxRange ] = color
        pixels[x,yPxRange - y] = color
        imag += step
    imag = imagStart
    real += step
    x += 1

img.show()
