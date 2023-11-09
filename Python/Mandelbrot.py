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

def mandel(x,y):
    real = 0
    imag = 0
    for i in range(ITERATIONS):
        realSquared = real * real
        imagSquared = imag * imag
        tempReal = realSquared - imagSquared + x
        imag = 2 * real * imag + y
        real = tempReal

        if realSquared + realSquared >= 4:
            return i     
    return ITERATIONS
    
img = Image.new( 'RGB', (SIZE, SIZE), "black") # create a new black image
pixels = img.load() # create the pixel map

x = xStart
y = yStart

for x in range(SIZE):    # for every col:
    for y in range(yRange):    # For every row
        i = mandel(x, y)
        color = math.floor(i * colorStep)
        pixels[x,y + yRange ] = (color, 0, 0)
        pixels[x,yRange - y] = (color, 0, 0)
        y += step
    y = yStart
    x += step

img.show()