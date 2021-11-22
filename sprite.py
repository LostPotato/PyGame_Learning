"""
This file is an iteration of the Command in which the game
and user interface are separated out into different classes
"""

import pygame as pg
from pygame.math import Vector2


class GameState:
    """
    Handles moving position of the gameState and updates the position
    of the object
    """
    def __init__(self):
        self.worldSize = Vector2(16,11)
        self.tankPos = Vector2(0,0)

    def update(self, moveTankCommand):
        """On update grabs the new tank position"""
        self.tankPos += moveTankCommand

        # controlling for the edge of the window
        if self.tankPos.x < 0:
            self.tankPos = 0
        elif self.tankPos.x >= self.worldSize.x:
            self.tankPos.x = self.worldSize.x - 1
        if self.tankPos.y < 0:
            self.tankPos.y = 0
        elif self.tankPos.y >= self.worldSize.y:
            self.tankPos.y = self.worldSize.y - 1


class UserInterface:
    """Handles all interaction with the GameState"""

    def __init__(self):
        """Sets window size, initial position, and game clock"""

        pg.init()
        # defining the GameState object
        # this holds the position of the object and
        self.gameState = GameState()
        # sets display text of window
        pg.display.set_caption("Tanks")

        # Defining the cell size of the tiles in the game
        self.cellSize = Vector2(64, 64)
        # grabbing the tank png
        self.tankTexture = pg.image.load("body_tracks.png")

        # window size is determined to equal a 2d array * the cell sizes
        window_size = self.gameState.worldSize.elementwise() * self.cellSize

        # takes the input of the window size and makes it int
        self.window = pg.display.set_mode((int(window_size.x), int(window_size.y)))
        # Generating a vector for tank movement
        self.moveTankCommand = Vector2(0,0)

        # defines a clock instance for the interface
        self.clock = pg.time.Clock()
        # establishes an still state for the movement props
        self.running = True  # Handles run-state

    def process_input(self):
        """Handles the user input"""
        # Resetting the movement of the object
        self.moveTankCommand = Vector2(0,0)

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
                    self.moveTankCommand.x += 1
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    self.moveTankCommand.y -= 1
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.moveTankCommand.y += 1
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.moveTankCommand.x -= 1

    def update(self):
        """Takes in the keypress and updates the x,y position when called"""
        self.gameState.update(self.moveTankCommand)

    def render(self):
        """Renders the window"""
        self.window.fill("black")  # sets window background to black
        # sets the position of the sprite to the tank position
        spritePoint = self.gameState.tankPos.elementwise()*self.cellSize
        # link texture to sprite
        texturePoint = Vector2(0,0).elementwise()*self.cellSize
        # Wrapping the texture around a rectangle
        textureRect = pg.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        # Having the window draw the the tank
        self.window.blit(self.tankTexture, spritePoint,textureRect)

        pg.display.update()

    def run(self):
        """Handles the process of running the loop"""
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)  # sets updates to frame-rate
