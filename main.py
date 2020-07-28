import pygame as pg
import random

# Intializing pygame
pg.init()


# window display stuff
DISPLAY_WIDTH = 650
DISPLAY_HEIGHT = 650
DP = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A* - Visualization")

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
col_no = 30
yes1 = yes2 = False
start = End = None

class Star:
	matrix = [[0 for _ in range(col_no+1)] for _ in range(col_no+1)]	

	def __init__(self):
		# Main pygame loop
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					quit()
			DP.fill(WHITE)
			self.get_pos()
			self.square()
			self.draw_grid()
			clock.tick(frame)
			pg.display.update()

	def draw_line(self, color, x, y, width, height):
        #surface, color, (x, y, width, height)
		line = pg.draw.rect(DP, color, (x, y, width, height))

	def draw_grid(self):
		col_dis = DISPLAY_HEIGHT // col_no
		col_dis_cov = DISPLAY_HEIGHT // col_no
		thick = 1

		# Horizontal lines
		for i in range(col_no):
			self.draw_line(BLACK, 0, col_dis_cov, DISPLAY_WIDTH, 0)

			# Vertical Lines
			self.draw_line(BLACK, col_dis_cov, 0, thick, DISPLAY_HEIGHT)
			col_dis_cov += col_dis

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

		    if yes1 == yes2 == True:
		    	if (x_pos, y_pos) != start:
		    		if (x_pos, y_pos) != end:
		    			self.matrix[x_pos][y_pos] = 1

		    if yes1 == False:
		    	for i in self.matrix:
		    		if 2 not in i:
		    			# if (x_pos, y_pos) != end:
		    			yes1 = True
		    			start = (x_pos, y_pos)
		    			self.matrix[x_pos][y_pos] = 2

		    if yes2 == False:
		    	for i in self.matrix:
		    		if 3 not in i:
		    			if (x_pos, y_pos) != start:
			    			yes2 = True
			    			end = (x_pos, y_pos)
			    			self.matrix[x_pos][y_pos] = 3


	def square(self):
		rect_side = DISPLAY_HEIGHT//col_no
		for i in range(col_no+1):
			for j in range(col_no+1):
				if self.matrix[i][j] == 1:
					# Draw a rectangle
					self.draw_line(BLUE, rect_side*i, rect_side*j, rect_side, rect_side)
				elif self.matrix[i][j] == 2:
					self.draw_line(GREEN, rect_side*i, rect_side*j, rect_side, rect_side)
				elif self.matrix[i][j] == 3:
					self.draw_line(RED, rect_side*i, rect_side*j, rect_side, rect_side)




# Running the program
Star()
