import pygame as pg
import random

# Intializing pygame
pg.init()


# window display stuff
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
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


# Main loop
def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        DP.fill(WHITE)
        clock.tick(frame)
        pg.display.update()

main()

