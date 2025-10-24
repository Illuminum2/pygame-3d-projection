import asyncio
import sys

import pygame as pg
import constants as config

from graphics import draw

class RenderEngine:
    def __init__(self, window, clock, vertices):
        self.window = window
        self.clock = clock
        self.done = False

        self.dw = draw.Draw(window)
        self.cam = self.dw.pj.cam

        self.vertices = vertices

    def checkKeys(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.cam.move((0, 0, 1), self.dw.pj.R)
        elif key[pg.K_s]:
            self.cam.move((0, 0, -1), self.dw.pj.R)
        if key[pg.K_a]:
            self.cam.move((-1, 0, 0), self.dw.pj.R)
        elif key[pg.K_d]:
            self.cam.move((1, 0, 0), self.dw.pj.R)
        if key[pg.K_q]:
            self.cam.move((0, -1, 0), self.dw.pj.R)
        elif key[pg.K_e]:
            self.cam.move((0, 1, 0), self.dw.pj.R)

        if key[pg.K_LEFT]:
            self.cam.rotate(-5, self.dw.pj.R[1], self.dw.pj.R)
            self.dw.pj.updateR()
        elif key[pg.K_RIGHT]:
            self.cam.rotate(5, self.dw.pj.R[1], self.dw.pj.R)
            self.dw.pj.updateR()
        if key[pg.K_UP]:
            self.cam.rotate(-5, self.dw.pj.R[0], self.dw.pj.R)
            self.dw.pj.updateR()
        elif key[pg.K_DOWN]:
            self.cam.rotate(5, self.dw.pj.R[0], self.dw.pj.R)
            self.dw.pj.updateR()

        elif key[pg.K_ESCAPE]:
            self.done = True

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    async def main(self):
        while not self.done:
            self.checkKeys()
            self.checkEvents()

            self.dw.draw(self.vertices)
            pg.display.update()

            self.clock.tick(config.FPS)
            await asyncio.sleep(0)

        self.dw.endscreen()
        pg.display.update()

        pg.quit()
        sys.exit()