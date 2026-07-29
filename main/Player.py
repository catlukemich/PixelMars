import pygame


class Player:

    def __init__(self, main) -> None:
        from main.Game import Game

        self.main: Game = main

        # fmt: off
        # Five types of resources: food, power, coal, steel, population player can have. Each resource has a quantity associated with it.
        self.food       = 100
        self.power      = 10
        self.coal       = 10
        self.steel      = 10
        self.population = 100
        # fmt: on

    def update(self, clock: pygame.time.Clock):
        pass

    ###### 1.FOOD: ######
    def setFood(self, food):
        self.food = food
        self.main.toolbar.food_indicator_label.setText("food: " + str(self.food) + " t")


    def addFood(self, food):
        self.setFood(self.food + food)

    def subtractFood(self, food):
        if self.food >= food:
            self.setFood(self.food - food)
            return True
        else:
            return False

    ###### 2.ENERGY: ###### 
    def setPower(self, power):
        self.power = power
        self.main.toolbar.energy_indicator_label.setText(
            "energy: " + str(self.power) + " mWh"
        )

    def addEnergy(self, power):
        self.setPower(self.power + power)

    def subtractEnergy(self, power):
        if self.power >= power:
            self.setPower(self.power - power)
            return True
        else:
            return False

    ###### 3.COAL: ######
    def setCoal(self, coal):
        self.coal = coal
        # assume toolbar has a coal_indicator_label
        self.main.toolbar.coal_indicator_label.setText("coal: " + str(self.coal) + " t")

    def addCoal(self, coal):
        self.setCoal(self.coal + coal)

    def subtractCoal(self, coal):
        if self.coal >= coal:
            self.setCoal(self.coal - coal)
            return True
        else:
            return False

    ###### 4.STEEL: ######
    def getSteel(self):
        return self.steel

    def setSteel(self, steel):
        self.steel = steel
        # assume toolbar has a steel_indicator_label
        self.main.toolbar.steel_indicator_label.setText(
            "steel: " + str(self.steel) + " t"
        )

    def addSteel(self, steel):
        self.setSteel(self.steel + steel)

    def subtractSteel(self, steel):
        self.setSteel(self.steel - steel)

    ###### 5.POPULATION: ######
    def setPopulation(self, population):
        self.population = population
        # assume toolbar has a population_indicator_label
        self.main.toolbar.population_indicator_label.setText(
            "pop: " + str(self.population)
        )

    def addPopulation(self, population):
        self.setPopulation(self.population + population)

    def subtractPopulation(self, population):
        self.setPopulation(self.population - population)
