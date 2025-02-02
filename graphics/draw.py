import pygame as pg
import constants as config

from graphics import projection
from states.modes import Modes

class Draw:
    def __init__(self, window):
        self.window = window
        self.pj = projection.Projection()

    def draw(self, vertices):
        self.window.fill(config.BG_COLOR)

        if config.MODE is Modes.DotBased:
            for vertice in vertices:
                for point in vertice:
                    projected = self.pj.project(point)
                    if projected is not None:
                        pg.draw.circle(self.window, config.LINE_COLOR, (int(projected[0] + config.WIDTH / 2), int(projected[1] + config.HEIGHT / 2)), 5)

        if config.MODE is Modes.QuadBased:
            for vertice in vertices:
                projected = []
                for vertex in vertice:
                    projected.append(self.pj.project(vertex))
                if None not in projected:
                    pg.draw.polygon(self.window, config.LINE_COLOR, [(projected[0][0] + config.WIDTH / 2, projected[0][1] + config.HEIGHT / 2), (projected[1][0] + config.WIDTH / 2, projected[1][1] + config.HEIGHT / 2), (projected[2][0] + config.WIDTH / 2, projected[2][1] + config.HEIGHT / 2), (projected[3][0] + config.WIDTH / 2, projected[3][1] + config.HEIGHT / 2)], 5)

    def endscreen(self):
        self.window.fill(config.BG_COLOR)
        title_font = pg.font.Font(None, 40)
        title = title_font.render("Process ended, please reload page to restart.", True, config.LINE_COLOR)
        window_rect = pg.display.get_surface().get_rect()
        title_rect = title.get_rect(center=window_rect.center)
        self.window.fill(config.BG_COLOR)
        self.window.blit(title, title_rect)