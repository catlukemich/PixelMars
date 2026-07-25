import view
from utils.Assets import loadSound, loadAnimation
from view.AnimatedSprite import AnimatedSprite
from . import Constants
from .GameProcess import GameState
from utils.Vectors import Vec3

class StarshipLandingState(GameState):

    def __init__(self, main, starship):
        self.main = main
        self.starship = starship
        self.landing_speed = 0.6

    def init(self):
        view = self.main.view

        self.starship.setLocation(Vec3(9, 9, 40)) # was z 40
        self.starship.toggleThrusters(True)
        view.addSprite(self.starship)

        landing_sound = loadSound("assets/rocket.mp3")
        landing_sound.play()


    def update(self, clock):
        ''' Update - Make the starship land'''
        starship_loc = self.starship.getLocation()
        self.landing_speed -= 0.005

        if self.landing_speed < 0.02:
            self.landing_speed = 0.02

        starship_loc.z -= self.landing_speed

        self.starship.setLocation(starship_loc)
        self.main.view.setCenter(starship_loc)

        if starship_loc.z < 0:
            starship_loc.z = 0
            self.starship.setLocation(starship_loc)
            self.main.removeState(self)

    def final(self):
        ''' End - cleanup and final animations - the starship has landed. '''
        view = self.main.view

        # Toggle the thrusters off:
        self.starship.toggleThrusters(False)

        hit_sound = loadSound("assets/hit.mp3")
        hit_sound.play() # <-- Play hit ground sound.

        ## Show smoke from under the thrusters:
        landing_smoke_anim = loadAnimation("assets/landing_smoke")
        landing_smoke_spr = AnimatedSprite(landing_smoke_anim, False)
        landing_smoke_spr.layer = Constants.OVERLAYS_LAYER
        landing_smoke_spr.setLocation(Vec3(9, 9, 0))
        view.addSprite(landing_smoke_spr)

        # Add Starship to the terrain so we can build.
        terrain = self.main.terrain
        tile = terrain.getTile(9, 9)
        tile.addObject(self.starship)

        # Enable the scrolling of view:
        self.main.scroller.enable()
