import pygame as pg
import os

"""
This takes the keyboard event loop that was covered in the last example
and makes it into a loop that can be easily traveled as a game class
"""


class Game:
    """Handles the game state loop"""

    def __init__(self):
        """Sets window size, initial position, and game clock"""
        pg.init()
        self.window = pg.display.set_mode((640, 480))
        pg.display.set_caption("Tanks")
        self.clock = pg.time.Clock()
        self.x = 120
        self.y = 120
        self.running = True  # Handles run-state

    def processInput(self):
        """Handles the user input"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                break

            # handling the key press
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.x += 8
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    self.y -= 8
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.y += 8
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.x -= 8

    def update(self):
        pass

    def render(self):
        """Renders the window"""
        self.window.fill("black") # sets window background to black
        # draws a rectangle on the window frame
        # start position is self.x and self.y
        pg.draw.rect(self.window, (0, 255, 0), (self.x, self.y, 400, 200))
        # update display
        pg.display.update()

    def run(self):
        """Handles the process of running the loop"""
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60) # sets updates to framerate

