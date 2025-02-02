import asyncio

import pygame
import constants as config

from graphics import renderEngine as re

# initializing pygame and setting the screen resolution
pygame.init()
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Pygame 3D Engine")
clock = pygame.time.Clock()

# Vertices of a cube
vertices = [[(-2,2,2),(2,2,2),(2,-2,2),(-2,-2,2)],[(-2,-2,-2),(2,-2,-2),(2,2,-2),(-2,2,-2)],[(-2,-2,2),(2,-2,2),(2,-2,-2),(-2,-2,-2)],[(2,2,2),(-2,2,2),(-2,2,-2),(2,2,-2)],[(2,-2,2),(2,2,2),(2,2,-2),(2,-2,-2)],[(-2,2,2),(-2,-2,2),(-2,-2,-2),(-2,2,-2)]]

# Engine class instance
engine = re.RenderEngine(window, clock, vertices)
engine.cam.set((0,0,-5))

asyncio.run(engine.main())
