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

class Star:
	row_no = 30
	col_no = 30
	matrix = [[0 for _ in range(31)] for _ in range(31)]	

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
		row_dis = DISPLAY_WIDTH // self.row_no
		col_dis = DISPLAY_HEIGHT // self.col_no
		col_dis_cov = DISPLAY_HEIGHT // self.col_no
		row_dis_cov = DISPLAY_WIDTH // self.row_no
		thick = 1

		# Vertical lines
		for i in range(self.row_no):
			self.draw_line(BLACK, row_dis_cov, 0, thick, DISPLAY_HEIGHT)
			row_dis_cov+=row_dis

		# Horizontal lines
		for i in range(self.col_no):
			self.draw_line(BLACK, 0, col_dis_cov, DISPLAY_WIDTH, 0)
			col_dis_cov += col_dis

	def get_pos(self):
		click = pg.mouse.get_pressed()
		mouse = pg.mouse.get_pos()

		# if there is a click
		if click[0] == 1:
			# X axis of the mouse position
		    x_pos = mouse[0] // (DISPLAY_WIDTH // self.row_no)
		    # Y axis of the mouse position
		    y_pos = mouse[1] // (DISPLAY_HEIGHT // self.col_no)
		    
		    self.pos = (x_pos, y_pos)
		    print(self.pos)
		    self.matrix[x_pos][y_pos] = 1

	def square(self):
		rect_height = DISPLAY_HEIGHT//self.col_no
		rect_width = DISPLAY_WIDTH//self.row_no
		for i in range(self.col_no):
			for j in range(self.row_no):
				if self.matrix[i][j] == 1:
					# Draw a rectangle
					self.draw_line(RED, rect_width*i, rect_width*j, rect_width, rect_height)


# Running the program
Star()
