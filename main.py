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
	# Main pygame loop
	def __init__(self):
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					quit()
			DP.fill(WHITE)
			self.draw_grid()
			clock.tick(frame)
			pg.display.update()

	def draw_line(self, color, x, y, width, height):
        #surface, color, (x, y, width, height)
		line = pg.draw.rect(DP, color, (x, y, width, height))

	def draw_grid(self):
		row_no = 30
		col_no = 30
		row_dis = DISPLAY_WIDTH // row_no
		col_dis = DISPLAY_HEIGHT // col_no
		col_dis_cov = DISPLAY_HEIGHT // col_no
		row_dis_cov = DISPLAY_WIDTH // row_no
		col_dis = DISPLAY_HEIGHT // col_no
		thick = 1

		# Vertical lines
		for i in range(row_no):
			self.draw_line(BLACK, row_dis_cov, 0, thick, DISPLAY_HEIGHT)
			row_dis_cov+=row_dis

		# Horizontal lines
		for i in range(col_no):
			self.draw_line(BLACK, 0, col_dis_cov, DISPLAY_WIDTH, 0)
			col_dis_cov += col_dis



# Running the program
Star()
