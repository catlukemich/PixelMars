from constructibles.GreenDomeDescriber import GreenDomeDescriber
from constructibles.ResearchCenterDescriber import ResearchCenterDescriber
from constructibles.SupplyStationDescriber import SupplyStationDescriber
from utils.Assets import loadImage
from gui.Button import Button
from constructibles.ConnectorPlaceableDescriber import ConnectorPlaceableDescriber


class Toolbar:

    def __init__(self, main):
        self.main = main
        self.connector_button = Button(loadImage("assets/gui/connector.png"))
        self.connector_button.setPosition((10, 610))
        self.connector_button.click_listener = self
        self.connector_button.setTooltipText("Connector to connect starship with other buildings.")


        self.green_dome_button = Button(loadImage("assets/gui/green_dome.png"))
        self.green_dome_button.setPosition((60, 610))
        self.green_dome_button.click_listener = self
        self.green_dome_button.setTooltipText("Green dome to provide food and water for inhabitants.")

        # TODO: Inhabitants quaters. 
        # TODO: Power station.
        
        self.supply_station_button = Button(loadImage("assets/gui/supply_station.png"))
        self.supply_station_button.setPosition((110, 610))
        self.supply_station_button.click_listener = self
        self.supply_station_button.setTooltipText("Supply station for materials which the colony is lacking of.")

        self.research_center_button = Button(loadImage("assets/gui/research_center.png"))
        self.research_center_button.setPosition((160, 610))
        self.research_center_button.click_listener = self
        self.research_center_button.setTooltipText("Research center to discover new technologies.")

        self.clear_button = Button(loadImage("assets/gui/clear.png"))
        self.clear_button.setPosition((210, 610))
        self.clear_button.click_listener = self
        self.clear_button.setTooltipText("Clear button for destructing existing buildings and infrastructure.")

    def show(self):
        self.main.gui.addWidget(self.connector_button)
        self.main.gui.addWidget(self.green_dome_button)
        self.main.gui.addWidget(self.supply_station_button)
        self.main.gui.addWidget(self.research_center_button)
        self.main.gui.addWidget(self.clear_button)

    def onClick(self, event, widget):
        if widget == self.connector_button:
            placement_mode = self.main.modes.placement_mode
            placement_mode.setPlaceableDescriber(ConnectorPlaceableDescriber(self.main))
            self.main.setMode(placement_mode)

        if widget == self.green_dome_button:
            placement_mode = self.main.modes.placement_mode
            placement_mode.setPlaceableDescriber(GreenDomeDescriber(self.main))
            self.main.setMode(placement_mode)

        if widget == self.supply_station_button:
            placement_mode = self.main.modes.placement_mode
            placement_mode.setPlaceableDescriber(SupplyStationDescriber(self.main))
            self.main.setMode(placement_mode)

        if widget == self.research_center_button:
            placement_mode = self.main.modes.placement_mode
            placement_mode.setPlaceableDescriber(ResearchCenterDescriber(self.main))
            self.main.setMode(placement_mode)

        if widget == self.clear_button:
            clear_mode = self.main.modes.clear_mode
            self.main.setMode(clear_mode)