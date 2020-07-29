import pygame as pg
import random

# Intializing pygame
pg.init()


# window display stuff
DISPLAY_WIDTH = DISPLAY_HEIGHT = 650
# DISPLAY_HEIGHT = 700
DP = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A* Visualization")

# Frame
frame = 60
clock = pg.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)     
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 119, 168)

# some variables

# Total number of boxes 
col_no = 35
yes1 = yes2 = False
start = End = None

class Star:
	# A matrix/grid for the window
	matrix = [[0 for _ in range(col_no+1)] for _ in range(col_no+1)]	

	def __init__(self):
		# Main pygame loop
		while True:
			# Checking if someone is quiting the game
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					quit()
			# Filling white color everytime
			DP.fill(WHITE)
			# Running some functions to do stuff
			self.get_pos()
			self.square()
			self.draw_grid()
			# Updating the pygame window
			clock.tick(frame)
			pg.display.update()

	# the function draws a rect/line
	def draw_rect(self, color, x, y, width, height):
        #surface, color, (x, y, width, height)
		line = pg.draw.rect(DP, color, (x, y, width, height))

	# drawing the whole grid
	def draw_grid(self):
		col_dis = DISPLAY_HEIGHT // col_no
		col_dis_cov = DISPLAY_HEIGHT // col_no
		thick = 1

		for i in range(col_no):
			# Draws Horizontal lines
			self.draw_rect(BLACK, 0, col_dis_cov, DISPLAY_WIDTH, 0)

			# Draws Vertical Lines
			self.draw_rect(BLACK, col_dis_cov, 0, thick, DISPLAY_HEIGHT)
			col_dis_cov += col_dis

	# getting position of the selected box
	def get_pos(self):
		global yes1, yes2, start, end
		click = pg.mouse.get_pressed()
		mouse = pg.mouse.get_pos()

		# if there is a click
		if click[0] == 1:
			# X axis of the mouse position
		    x_pos = mouse[0] // (DISPLAY_WIDTH // col_no)
		    # Y axis of the mouse position
		    y_pos = mouse[1] // (DISPLAY_HEIGHT // col_no)

		    print(x_pos, y_pos)

		    # Getting the starting point
		    if yes1 == False:
		    	for i in self.matrix:
		    		if 2 not in i:
		    			# if (x_pos, y_pos) != end:
		    			yes1 = True
		    			start = (x_pos, y_pos)
		    			self.matrix[x_pos][y_pos] = 2

		    # Getting the ending point
		    if yes2 == False:
		    	for i in self.matrix:
		    		if 3 not in i:
		    			if (x_pos, y_pos) != start:
			    			yes2 = True
			    			end = (x_pos, y_pos)
			    			self.matrix[x_pos][y_pos] = 3

			# if starting and ending points are given, the getting the obstacles points
		    if yes1 == yes2 == True:
		    	if (x_pos, y_pos) != start:
		    		if (x_pos, y_pos) != end:
		    			self.matrix[x_pos][y_pos] = 1

		    

	# Draws the square/box wherever it needs to be drawn
	def square(self):
		rect_side = DISPLAY_HEIGHT//col_no
		for i in range(col_no+1):
			for j in range(col_no+1):
				# obstables 
				if self.matrix[i][j] == 1:
					self.draw_rect(BLUE, rect_side*i, rect_side*j, rect_side, rect_side)
				# Green box for the starting point
				elif self.matrix[i][j] == 2:
					self.draw_rect(GREEN, rect_side*i, rect_side*j, rect_side, rect_side)
				# Red box for the ending point
				elif self.matrix[i][j] == 3:
					self.draw_rect(RED, rect_side*i, rect_side*j, rect_side, rect_side)




# Running the program
Star()
