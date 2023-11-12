import numpy as np
import math

size = 4
array = np.arange(size * size, dtype=np.int32).reshape(size,size)
print(array)
lastx, lasty = -1, -1


def processBlock(x, y):
	global lastx, lasty
	if lastx == x and lasty == y:
		raise Exception(f"Duplicate entry({x}:{y}) ")
	lastx = x
	lasty = y
	
	print(f"({x}:{y}) ")
	
def spiralPrint():
	midX = size // 2
	midY = math.ceil(size / 2 - 1)
	x = midX
	y = midY
	directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
	if size % 2 == 1:
		direction = directions[0]	
	else:
		direction = directions[2]
	print(f"Start from: {midX} {midY}")
	while 0 <= x < size and 0 <= y < size:
		processBlock(x, y)
		x += direction[0]
		y += direction[1]
		# direction changes
		if x == y and y <= midY: # up
			direction = directions[3]
		elif x == y + 1 and y >= midY: #down
			direction = directions[1]
		elif x + y == size - 1:
			if y >= midY: #right
				direction = directions[0]
			else: # left
				direction = directions[2]
	
	
spiralPrint()

