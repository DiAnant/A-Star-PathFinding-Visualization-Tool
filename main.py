import pygame as pg
import random

pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

DP = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A* - Visualization")

# Frame
frame = 60
clock = pg.time.Clock()

# Colors
white = (255, 255, 255)
green = (0, 255, 0)     
black = (0, 0, 0)
red = (255, 0, 0)


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        DP.fill(black)
        clock.tick(frame)
        pg.display.update()

main()

