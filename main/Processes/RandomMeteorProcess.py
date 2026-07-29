import random

import pygame

from main.processes.GameProcess import GameProcess


MINIMAL_METEOR_TIMEOUT = 60000 # <-- Minimal time between meteor falls.

class RandomMeteorProcess(GameProcess):

    def __init__(self, main) -> None:
        super().__init__(main)

        self.meteor_time = 0
        self.next_fall_time = self.calculateFallInterval()

    def calculateFallInterval(self):
        ''' Calculate time that's passes between two meteor falls. '''
        return MINIMAL_METEOR_TIMEOUT + random.randint(5000, 30000)
    
    def update(self, clock: pygame.time.Clock):
        self.meteor_time += clock.get_time()

        if self.meteor_time > self.next_fall_time:
            self.meteor_time = 0
            self.next_fall_time = self.calculateFallInterval()
            self.dropMeteor()

    def dropMeteor(self):
        pass # <-- TODO meteor drops.
        

        
