from pygame import Surface

import math
from typing import Optional
import random
from VDebugger.vdebugger import vd
from flyers.Rot60Flyer import Rot60Flyer
from main import Constants
from utils.Assets import loadImage, loadSound
from utils.Vectors import Vec3
from view.Sprite import Sprite

## Supply ship states:
APPROACHING = 1  
TURNING_IN  = 2
LANDING     = 3
WAITING     = 4
STARTING    = 5
TURNING_OUT = 6
LEAVING     = 7


class SupplyShip(Rot60Flyer):

    @staticmethod
    def call(supply_station, main):
        # fmt: off
        new_supply_ship = SupplyShip(main) # <-- Create a new supply ship that will come to supply station.
        station_location : Vec3 = supply_station.getLocation()    # <-- The location of the destination supply station.
        ship_location           = None                            # <-- Will be calculated later to animate ship comming from some place.
        random_rotation         = random.randint(0,359)           # <-- Needed in order to determine where the ship will come from.
        # fmt: on

        new_supply_ship.setInitialRotation(random_rotation)
        new_supply_ship.setRotation(random_rotation) # <-- Rotate the ship.

        ## Find the offset for the ship location:
        station_to_ship = Vec3(0, 30, 0) 
        station_to_ship.rotate(random_rotation)
        ship_location = station_location + station_to_ship + Vec3(0,0,4)  # <-- The start location of supply ship (4 units above the ground).
        new_supply_ship.setLocation(ship_location)
        new_supply_ship.setDestination(supply_station)

        return new_supply_ship
        
    def __init__(self, main):
        super().__init__(loadImage("assets/supply_ship_atlas.png"))
        from main.Game import Game
        self.main: Game = main
        self.destination : Optional[Sprite] = None
        self.setLayer(Constants.L4_FLYERS_LAYER)

        self.initial_rotation = 0
        self.state = APPROACHING # <-- Always a new supply ship is constructed it is meant to approach some supply station at the beginning.
        self.waiting_time = 0 # <-- Waiting time when started the 3. phase - WAITING for unload.

    def setInitialRotation(self, rotation):
        self.initial_rotation = rotation

    def setDestination(self, supply_station):
        self.destination = supply_station

    def update(self, clock):
        if self.destination != None:
            landing_start_location = self.destination.getLocation() + Vec3(0,0,4)
            landing_location = self.destination.getLocation() + Vec3(0,0,0.6)
            fly_away_location = self.destination.getLocation() + Vec3(0,0,6)
            dirvector = Vec3(0,0,0)
            speed = 2
            epsilon = 0.1

            if self.state == APPROACHING:
                dirvector = Vec3(0, -1, 0)
                dirvector.rotate(self.rotation)

                if self.location.distance(landing_start_location) < epsilon:

                    self.state = TURNING_IN

            if self.state == TURNING_IN:
                current_rotation = self.getRotation()
                if current_rotation > 93:
                    current_rotation -= 6
                elif current_rotation < 87:
                    current_rotation += 6
                else:
                    current_rotation = 90

                self.setRotation(current_rotation)
                if current_rotation == 90:
                    self.state = LANDING


            if self.state == LANDING:
                dirvector = Vec3(0, 0, -1)
                if self.location.distance(landing_location) < epsilon:
                    self.state = WAITING

            if self.state == WAITING:
                self.waiting_time += clock.get_time()
                if self.waiting_time > 3000:
                    self.waiting_time = 0
                    self.state = STARTING
                    self.main.player.addFood(10)

            if self.state == STARTING:
                dirvector = Vec3(0,0,1)
                speed = 3
                if self.location.distance(fly_away_location) < epsilon:
                    self.state = TURNING_OUT

            if self.state == TURNING_OUT:
                current_rotation = self.getRotation()
                if current_rotation > self.initial_rotation + 3:
                    current_rotation -= 6
                elif current_rotation < self.initial_rotation - 3:
                    current_rotation += 6
                else:
                    current_rotation = self.initial_rotation
                self.setRotation(current_rotation)
                if current_rotation == self.initial_rotation:
                    leaving_sound = loadSound("assets/sounds/supply_ship_leaving.wav")
                    leaving_sound.play()
                    self.state = LEAVING

            if self.state == LEAVING:
                dirvector = Vec3(0, -1, 0)
                dirvector.rotate(self.rotation)
                speed = 25
                if self.location.distance(fly_away_location) > 30:
                    self.main.view.removeSprite(self)

            ###### Actually moving the supply ship: ######
            self.location = self.location + dirvector * clock.get_time() / 1000 * speed

        return super().update(clock)