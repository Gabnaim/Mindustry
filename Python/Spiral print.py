import numpy as np
import math

size = 4
array = np.arange(size * size, dtype=np.int32).reshape(size,size)
print(array)

def processBlock(x, y):
	print(f"({x}:{y}:{array[x,y]}) ")
	
def spiralPrint():
	midX = size // 2
	midY = math.ceil(size / 2 - 1)
	x = midX
	y = midY
	yDir = 0
	xDir = 1 if (size % 2 == 1) else -1
	print(f"Start from: {midX} {midY}")
	while 0 <= x < size and 0 <= y < size:
		processBlock(x, y)
		x += xDir
		y += yDir
		# direction changes
		if x == y and y <= midY: # up
			xDir, yDir = 0, 1
		elif x == y + 1 and y >= midY: #down
			xDir, yDir = 0, -1
		elif x + y == size - 1:
			if y >= midY: #right
				xDir, yDir = 1, 0
			else: # left
				xDir, yDir = -1, 0
	
	
spiralPrint()

