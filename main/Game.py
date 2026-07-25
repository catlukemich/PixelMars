import pygame

from VDebugger.vdebugger import vd # <-- Visual debugger

from gui.GUI import GUI
from main.GameLoop import GameLoop
from main.Input import Input
from main.Modes import Modes

# Initially visible world elements:
from constructibles.Starship import Starship
from main.StarshipLandingProcess import StarshipLandingState
from terrain.Terrain import Terrain

# Game logical elements:
from gui.Toolbar import Toolbar
from view.Scroller import Scroller
from view.View import View

#           The Game class 
#                 ____
#                |,--.|
#                ||__||
#                |+  o| hjw
#                |,'o | 
#                `----'


class Game():
    ''' The Game class that is mainly responsible for initializing the game and running the game loop. It also manages the game states. '''

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (800,800), pygame.RESIZABLE
        )

        self.input = Input()
        self.view = View()
        self.gui = GUI(self)
        self.modes = Modes(self)
        self.terrain = Terrain(self)
        self.terrain.generate()
        self.scroller = Scroller(self)

        toolbar = Toolbar(self)
        toolbar.show()
        
        self.states = []  # <-- List of GameState instances.
        self.starship = Starship(self.terrain)

        landing_state = StarshipLandingState(self, self.starship)

        terrain = self.terrain
        tile = terrain.getTile(9, 9)
        tile.addObject(self.starship)
        
        self.addState(landing_state)


    def loop(self):
        game_loop = GameLoop() # <-- The game loop that makes the game work and play, externall class for clarity.
        game_loop.loop(self)


    ## GameState handling ##
    def addState(self, gamestate):
        self.states.append(gamestate)
        gamestate.init() ## Initialize state when it is added.

    def removeState(self, gamestate):
        self.states.remove(gamestate)
        gamestate.final() ## Finalize state when it is removed.

    def setMode(self, new_mode):
        self.modes.current_mode.disable()
        self.modes.current_mode = new_mode
        self.modes.current_mode.enable()

if __name__ == '__main__':
    main = Game()
    main.loop()