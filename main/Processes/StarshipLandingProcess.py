from flyers.Starship import Starship
from utils.MusicPlayer import MusicPlayer
import view
from utils.Assets import loadImage, loadSound, loadAnimation
from view.AnimatedSprite import AnimatedSprite
from view.Sprite import Sprite
from .. import Constants
from .GameProcess import GameProcess
from utils.Vectors import Vec3


class StarshipLandingProcess(GameProcess):

    def __init__(self, main, starship):
        super().__init__(main)
        self.starship: Starship = starship
        self.landing_speed = 0.6
        self.landing_tile = (
            self.main.terrain.width // 2,
            self.main.terrain.height // 2,
        )

    def start(self):
        view = self.main.view

        self.starship.setLocation(
            Vec3(self.landing_tile[0], self.landing_tile[1], 40)
        )  # was z 40
        self.starship.toggleThrusters(True)
        view.addSprite(self.starship)

        shadow_image = loadImage("assets/starship_shadow.png")
        self.starship_shadow = Sprite(shadow_image)
        self.starship_shadow.setLocation(
            Vec3(self.landing_tile[0], self.landing_tile[1] + 0.18, 0)
        )  # was z 40

        self.starship_shadow.setLayer(Constants.L2_OVERLAYS_LAYER)
        view.addSprite(self.starship_shadow)

        landing_sound = loadSound("assets/sounds/rocket.wav")
        landing_sound.play()

    def update(self, clock):
        """Update - Make the starship land"""
        starship_loc: Vec3 = self.starship.getLocation()
        self.landing_speed -= 0.00465

        if self.landing_speed < 0.011:
            self.landing_speed = 0.011
            self.starship.setImage(loadImage("assets/starship_thrusters2.png"))

        if starship_loc.z < 0.32:
            self.starship.setImage(loadImage("assets/starship.png"))
            self.landing_speed = 0.00295

        starship_loc.z -= self.landing_speed

        self.starship.setLocation(starship_loc)
        self.main.view.setCenter(starship_loc)

        if starship_loc.z < 0:
            starship_loc.z = 0
            self.starship.setLocation(starship_loc)
            self.main.removeProcess(self)

    def end(self):
        """End - cleanup and final animations - the starship has landed."""
        view = self.main.view

        # Toggle the thrusters off:
        self.starship.toggleThrusters(False)

        hit_sound = loadSound("assets/hit.mp3")
        hit_sound.play()  # <-- Play hit ground sound.

        ## Show smoke from under the thrusters:
        landing_smoke_anim = loadAnimation("assets/landing_smoke")
        landing_smoke_spr = AnimatedSprite(landing_smoke_anim, False)
        landing_smoke_spr.layer = Constants.L2_OVERLAYS_LAYER
        landing_smoke_spr.setLocation(
            Vec3(self.landing_tile[0], self.landing_tile[1], 0)
        )
        view.addSprite(landing_smoke_spr)

        # Add Starship to the terrain so we can build.
        terrain = self.main.terrain
        tile = terrain.getTile(self.landing_tile[0], self.landing_tile[1])
        tile.addObject(self.starship)

        # Enable the scrolling of view:
        self.main.scroller.enable()

        MusicPlayer.getInstance().start()

        # advisor = self.main.advisor
        # advisor.communicate(
        #     "Hello Commander, welcome to Mars, this is our first colony, which you are designed to supervise.",
        #     lambda: advisor.communicate(
        #         "Start building green domes to establish a food providing base for colonists. \nDue to our technological advances - a single green dome can provide food for one segment of quarters",
        #         lambda: advisor.communicate(
        #             "Then for the sake of unexpected needs, build a supply station. \nA supply ship will arrive every now and then to support your base with additional resouoces.",
        #             lambda: advisor.communicate(
        #                 "When need arises - build a coal miner and a power plant, since the spaceship built-in power generators \ncan't supply enough power for growing colony",
        #                 lambda: advisor.communicate(
        #                     "And remember! Every construction costs you steel, so keep in mind the costs! \nIf something in the way I'll call you back later. Anna."
        #                 ),
        #             ),
        #         ),
        #     ),
        # )
