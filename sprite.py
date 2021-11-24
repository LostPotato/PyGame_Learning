"""
This file is an iteration of the Command in which the game
and user interface are separated out into different classes
"""
from abc import ABC

import pygame as pg
from pygame.math import Vector2


class Unit:
    """
    Parent class for units in the game
    """

    def __init__(self, state, position, tile, name = None):
        self.state = state  # takes in game state
        self.position = position
        self.tile = tile
        self.name = name

    def move(self, move_vector):
        """Unit movement -- Error if not implemented on child level"""
        raise NotImplementedError()


class Tank(Unit):
    def move(self, move_vector):
        newTankPos = self.position + move_vector
        if newTankPos.x < 0 or newTankPos.x >= self.state.worldSize.x \
                or newTankPos.y < 0 or newTankPos.y >= self.state.worldSize.y:
            return
        # handling collisions with other units
        for unit in self.state.units:
            if newTankPos == unit.position:
                return
        self.position = newTankPos


class Tower(Unit):
    def move(self, move_vector):
        pass


class GameState:
    """
    Handles moving position of the gameState and updates the position
    of the object
    """

    def __init__(self):
        self.worldSize = Vector2(15, 8)
        self.units = [
            Tank(self, Vector2(5, 4), Vector2(0, 0), 'Tank'),
            Tower(self, Vector2(10, 3), Vector2(0, 1), 'Tower'),
            Tower(self, Vector2(10, 5), Vector2(0, 1), 'Tower')
        ]

    def update(self, moveTankCommand):
        for unit in self.units:
            unit.move(moveTankCommand)


class UserInterface:
    """Handles all interaction with the GameState"""

    def __init__(self):
        """Sets window size, initial position, and game clock"""

        """ initializing the user interface """
        pg.init()
        self.gameState = GameState()

        """Render settings"""
        # Defining the cell size of the tiles in the game
        self.cellSize = Vector2(128, 128)
        # grabbing the tank png
        self.tankTexture = pg.image.load("sprites/body_tracks.png")
        self.towerTexture = pg.image.load("sprites/Blue/Towers/towers_walls_blank.png")
        self.gunTexture = pg.image.load("sprites/Blue/Weapons/turret_01_mk1.png")

        """ Window """
        # sets display text of window
        pg.display.set_caption("Tanks")
        # window size is determined to equal a 2d array * the cell sizes
        window_size = self.gameState.worldSize.elementwise() * self.cellSize
        # takes the input of the window size and makes it int
        self.window = pg.display.set_mode((int(window_size.x), int(window_size.y)))
        # Generating a vector for tank movement
        self.moveTankCommand = Vector2(0, 0)

        """ Controls the game loop """
        # defines a clock instance for the interface
        self.clock = pg.time.Clock()
        # establishes an still state for the movement props
        self.running = True  # Handles run-state

    def process_input(self):
        """Handles the user input"""
        # Resetting the movement of the object
        self.moveTankCommand = Vector2(0, 0)

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

    def renderUnit(self, unit):
        """Renders the units that exist"""
        # sets the position of the sprite to the tank position
        spritePoint = unit.position.elementwise() * self.cellSize

        """Unit textures"""
        # link texture to sprite
        texturePoint = unit.tile.elementwise() * self.cellSize
        # Wrapping the texture around a rectangle
        textureRect = pg.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))

        # Handles texture selection
        if unit.name == "Tank":
            # Having the window draw the the tank
            self.window.blit(self.tankTexture, spritePoint, textureRect)

        if unit.name == "Tower":
            self.window.blit(self.towerTexture, spritePoint, textureRect)

        """Gun Texture"""
        texturePoint = Vector2(0, 0).elementwise()*self.cellSize
        textureRect = pg.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.gunTexture, spritePoint, textureRect)

    def render(self):
        """ Renders window and units to the display """
        self.window.fill("Green")

        # loops through units
        for unit in self.gameState.units:
            self.renderUnit(unit)

        pg.display.update()

    def run(self):
        """Handles the process of running the loop"""
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)  # sets updates to frame-rate
