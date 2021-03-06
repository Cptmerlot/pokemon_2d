from __future__ import annotations
from typing import TYPE_CHECKING
import pygame as pg
from pygame.surface import Surface


if TYPE_CHECKING:
    from .loop import GameLoop


class MainScreen():
    def __init__(self, screen: Surface, game_loop: GameLoop):
        self._screen = screen
        self._game_loop = game_loop

    def welcome_render(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._game_loop.StopRunning()
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_RETURN, pg.K_SPACE):
                    self._game_loop.EnterCombat()
                if event.key == pg.K_ESCAPE:
                    self._game_loop.StopRunning()

        self._screen.fill((0, 0, 0))
        wf = self._game_loop.display_info.welcome_font.render("Welcome to Pokemon 2d", False, (255, 255, 255))
        wf_rect = wf.get_rect(center=(self._screen.get_width() / 2, self._screen.get_height() / 2))
        self._screen.blit(wf, wf_rect)

    def game_over_render(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._game_loop.StopRunning()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._game_loop.StopRunning()

        self._screen.fill((0, 0, 0))
        wf = self._game_loop.display_info.welcome_font.render("Game Over", False, (255, 255, 255))
        wf_rect = wf.get_rect(center=(self._screen.get_width() / 2, self._screen.get_height() / 2))
        self._screen.blit(wf, wf_rect)
