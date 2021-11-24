"""
This file is an iteration of the classes in which the game
and user interface are separated out into different classes
"""

import pygame as pg


class GameState:
    """
    Handles moving position of the gameState and updates the position
    of the object
    """
    def __init__(self):
        self.x = 120
        self.y = 120

    def update(self, move_command_x, move_command_y):
        self.x += move_command_x
        self.y += move_command_y


class UserInterface:
    """Handles all interaction with the GameState"""

    def __init__(self):
        """Sets window size, initial position, and game clock"""
        pg.init()
        # sets window size
        self.window = pg.display.set_mode((640, 480))
        # sets display text of window
        pg.display.set_caption("Tanks")
        # defines a clock instance for the interface
        self.clock = pg.time.Clock()
        # defining the GameState object
        # this holds the position of the object and
        # handles updates
        self.gameState = GameState()
        # establishes an still state for the movement props
        self.moveX = 0
        self.moveY = 0
        self.running = True  # Handles run-state

    def process_input(self):
        """Handles the user input"""
        # Resetting the movement of the object
        self.moveX, self.moveY = 0, 0

        # responding to keypress
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
                    self.moveX += 8
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    self.moveY -= 8
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.moveY += 8
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.moveX -= 8

    def update(self):
        """Takes in the keypress and updates the x,y position when called"""
        self.gameState.update(self.moveX, self.moveY)

    def render(self):
        """Renders the window"""
        self.window.fill("black")  # sets window background to black
        # draws a rectangle on the window frame
        # renders the rectangle at the new position every update
        x = self.gameState.x
        y = self.gameState.y
        pg.draw.rect(self.window, (0, 255, 0), (x, y, 400, 200))
        # update display
        pg.display.update()

    def run(self):
        """Handles the process of running the loop"""
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)  # sets updates to frame-rate
