import pygame


class GameProcess:

    def __init__(self, main) -> None:
        from main.Game import Game
        self.main: Game = main
        pass

    def start(self):
        pass

    def update(self, clock: pygame.time.Clock):
        return None

    def draw(self, surface):
        pass

    def end(self):
        pass