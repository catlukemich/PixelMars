import pygame


class Player:

    def __init__(self, main) -> None:
        from main.Game import Game
        self.main: Game = main
        self.power = 10
        self.food = 10
        self.coal = 10
        self.steel = 10
        self.population = 100

    def update(self, clock: pygame.time.Clock):
        pass


    def setFood(self, food):
        self.food = food
        self.main.toolbar.food_indicator_label.


    def addFood(self, food):
        self.setFood(self.food + food)