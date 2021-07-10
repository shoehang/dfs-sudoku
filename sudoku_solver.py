from sudoku_gui import *
import sys

# function to create and prepopulate a list
# representing a sudoku problem
# *change values to accomodate different puzzles
def sudoku_setup():
	lst = [[] for _ in range(9)]
	lst = [[3,4,0,0,0,7,0,2,6],
		   [0,2,0,0,0,4,8,0,1],
		   [0,0,1,2,0,5,0,0,0],
		   [2,5,0,6,0,0,0,0,0],
		   [6,8,0,9,0,0,3,4,0],
		   [0,1,0,4,0,2,0,0,8],
		   [1,6,0,0,8,9,0,3,0],
		   [4,0,9,0,2,0,6,0,0],
		   [0,0,8,7,4,6,2,0,0]]
	boxes = [[] for _ in range(9)]
	for i in range(len(lst)):
		for j in range(len(lst)):
			#dynamic spacing between boxes
			num = box(10 + (i * 30), 10 + (j * 30), 28, 28, (255,255,255), lst[i][j])
			boxes[i].append(num)
	return boxes

# function to check the next empty position
# on the sudoku puzzle represented by a '0'
# sets current row and col to pos if found
def next_empty_pos(lst, pos):
	for row in range(9):
		for col in range(9):
			currBox = lst[row][col]
			if (currBox.getText() == 0):
				pos[0] = row
				pos[1] = col
				return True
	return False

# function to check if numeber exist in
# all rows of the sudoku board
def row_check(lst, row, x):
	for i in range(9):
		currBox = lst[row][i]
		if (currBox.getText() == x):
			return True
	return False

# function to check if number exist in
# all columns of the sudoku board
def col_check(lst, col, y):
	for i in range(9):
		currBox = lst[i][col]
		if (currBox.getText() == y):
			return True
	return False

# function to check if number exist in
# 3x3 sudoku box
def box_check(lst, row, col, num):
	for i in range(3):
		for j in range(3):
			currBox = lst[i+row][i+col]
			if (currBox.getText() == num):
				return True
	return False

# function that solves a given sudoku puzzle
def solve(lst, canvas):
	# current position on board
	pos = [0,0]
	# gets next empty pos, if no next empty pos, we are done
	if (not next_empty_pos(lst,pos)):
		return True
	# update current row / pos
	row = pos[0]
	col = pos[1]
	# try numbers 1-9 on current pos of board
	for i in range(1,10):
		# check for i occurence in row, col, and box
		if (not row_check(lst, row, i) and not col_check(lst, col, i) and not box_check(lst, row - row%3, col - col%3, i)):
			# make tenative assignment on current pos 
			currBox = lst[row][col]
			currBox.setText(i)
			currBox.draw(canvas)
			# recurse step to traverse the puzzle
			if (solve(lst, canvas)):
				return True
			# on back track, when failed, assign 0
			currBox.setText(0)
			currBox.draw(canvas)
	# back tracking step
	return False

if __name__ == "__main__":
	pygame.init()

	WHITE = (255, 255, 255)
	GRAY = (190, 190, 190)
	LIGHTGRAY = (225, 225, 225)
	BLACK = (0, 0, 0)
	WIDTH = 288
	HEIGHT = 400

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Sudoku')
	CANVAS.fill(GRAY)

	SOLVEBUTTON = box(10, 290, 90, 60, WHITE, 'Solve')
	RESETBUTTON = box(110, 290, 90, 60, WHITE, 'Reset')
	TEXTBOX = box(10, 360, 268, 30, WHITE, '')
	problem = sudoku_setup()

	while True:
		# drawing grid lines
		pygame.draw.line(CANVAS, BLACK, (98, 10), (98, 278), 2)
		pygame.draw.line(CANVAS, BLACK, (188, 10), (188, 278), 2)
		pygame.draw.line(CANVAS, BLACK, (10, 98), (278, 98), 2)
		pygame.draw.line(CANVAS, BLACK, (10, 188), (278, 188), 2)
		# drwaing number boxes
		for row in problem:
			for col in row:
				col.draw(CANVAS)
		# drawing buttons
		SOLVEBUTTON.draw(CANVAS)
		RESETBUTTON.draw(CANVAS)
		TEXTBOX.draw(CANVAS)

		# event fetching
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			# mouse hovers over:
			if (event.type == pygame.MOUSEMOTION):
				# number boxes
				for row in problem:
					for NUMBOX in row:
						if (NUMBOX.hover(pos)):
							NUMBOX.color = LIGHTGRAY
						else:
							NUMBOX.color = WHITE
				# solve button
				if (SOLVEBUTTON.hover(pos)):
					SOLVEBUTTON.color = LIGHTGRAY
				else:
					SOLVEBUTTON.color = WHITE
				# reset button
				if (RESETBUTTON.hover(pos)):
					RESETBUTTON.color = LIGHTGRAY
				else:
					RESETBUTTON.color = WHITE
			# mouse click over:		
			if (event.type == pygame.MOUSEBUTTONDOWN):
				# number boxes
				for row in problem:
					for NUMBOX in row:
						if (NUMBOX.hover(pos)):
							NUMBOX.setNext()
				# solve button
				if (SOLVEBUTTON.hover(pos)):
					if (solve(problem, CANVAS)):
						TEXTBOX.setText('Solution Found')
					else:
						TEXTBOX.setText('No Solution Found')
				# reset button
				if (RESETBUTTON.hover(pos)):
					problem = sudoku_setup()
					TEXTBOX.setText(' ')
		pygame.display.update()