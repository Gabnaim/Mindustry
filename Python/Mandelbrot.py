import numpy as np
from PIL import Image

ITERATIONS = 46
SIZE = 176
DIAMETER = 2.5

step = DIAMETER / SIZE
yRange = SIZE // 2
xStart = -0.5 - DIAMETER / 2
yStart = 0

colors = ("#0000AA", "#88DDFF", "#FF8800", "#000000")
ncolors = len(colors)

def mandel(real,imag):
    z_r = 0
    z_i = 0
    z_r_squared = 0
    z_i_squared = 0
    for i in range(ITERATIONS):
        z_r_squared = z_r * z_r
        z_i_squared = z_i * z_i
        z_r = z_r_squared - z_i_squared + real
        z_i = 2 * z_r * z_i + imag

        if z_r_squared + z_r_squared > 4:
            return i     
    return ITERATIONS
    
img = Image.new( 'RGB', (SIZE, SIZE), "black") # create a new black image
pixels = img.load() # create the pixel map

real = xStart
imag = yStart

for x in range(SIZE):    # for every col:
    for y in range(yRange):    # For every row
        i = mandel(real, imag)
        color = colors[i//2 % ncolors] 
        
        pixels[x,y] = (x,y, color) # set the colour accordingly
        pixels[x, SIZE - y] = (x, SIZE - y, color)
        imag += step
    imag = yStart
    real += step

img.show()