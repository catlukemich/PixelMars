import pygame


class EnergyConsumer():

    def __init__(self, main, amount = 1) -> None:
        from main.Game import Game
        self.main : Game = main
        self.amount = amount
        self.time = 0

    def update(self, clock: pygame.time.Clock):
        self.time += clock.get_time()
        got_energy = self.main.player.subtractEnergy(self.amount)
        return got_energy