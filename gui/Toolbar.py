from constructibles.CoalMinerDescriber import CoalMinerDescriber
from constructibles.CoalProcessorDescriber import CoalProcessorDescriber
from constructibles.GreenDomeDescriber import GreenDomeDescriber
from constructibles.PopulationQuartersDescriber import PopulationQuartersDescriber
from constructibles.PowerStationDescriber import PowerStationDescriber
from constructibles.ResearchCenterDescriber import ResearchCenterDescriber
from constructibles.SupplyStationDescriber import SupplyStationDescriber
from gui.Icon import Icon
from gui.Label import Label
from gui.Panel import Panel
from gui.Widget import Widget
from utils.Assets import loadImage
from gui.Button import Button
from constructibles.ConnectorPlaceableDescriber import ConnectorPlaceableDescriber

# fmt: off

class Toolbar:
    """
    Toolbar at the bottom of the screen, it includes:
    - buttons for constructions
    - resources and population indicators
    - Informations about events in the colony
    """

    def __init__(self, main):
        from main.Game import Game
        self.main: Game = main

        ###### Construction buttons: ######
        self.panel_upper = Panel(800, 155)
        self.panel_upper.setPosition((0, 600))

        self.connector_button = Button(loadImage("assets/gui/connector.png"))
        self.connector_button.setPosition((10, 610))
        self.connector_button.click_listener = self
        self.connector_button.setTooltipText("Connector to connect starship with other buildings.")

        self.green_dome_button = Button(loadImage("assets/gui/green_dome.png"))
        self.green_dome_button.setPosition((70, 610))
        self.green_dome_button.click_listener = self
        self.green_dome_button.setTooltipText("Green dome to provide food and water for inhabitants.")

        self.population_quarters_button = Button(loadImage("assets/gui/population_quarters.png"))
        self.population_quarters_button.setPosition((130, 610))
        self.population_quarters_button.click_listener = self
        self.population_quarters_button.setTooltipText("Populations quarters provide living room for colonists.")

        self.coal_miner_button = Button(loadImage("assets/gui/coal_miner.png"))
        self.coal_miner_button.setPosition((190, 610))
        self.coal_miner_button.click_listener = self
        self.coal_miner_button.setTooltipText("Supply station for materials which the colony is lacking of.")

        self.coal_processor_button = Button(loadImage("assets/gui/coal_processor.png"))
        self.coal_processor_button.setPosition((250, 610))
        self.coal_processor_button.click_listener = self
        self.coal_processor_button.setTooltipText("Coal processor - processes coal into steel.")
        
        self.power_station_button = Button(loadImage("assets/gui/power_station.png"))
        self.power_station_button.setPosition((310, 610))
        self.power_station_button.click_listener = self
        self.power_station_button.setTooltipText("Power station for energy generation. Uses solar energy.")
        
        self.supply_station_button = Button(loadImage("assets/gui/supply_station.png"))
        self.supply_station_button.setPosition((370, 610))
        self.supply_station_button.click_listener = self
        self.supply_station_button.setTooltipText("Supply station for materials which the colony is lacking of.")

        self.research_center_button = Button(loadImage("assets/gui/research_center.png"))
        self.research_center_button.setPosition((430, 610))
        self.research_center_button.click_listener = self
        self.research_center_button.setTooltipText("Research center to discover new technologies.")

        self.clear_button = Button(loadImage("assets/gui/clear.png"))
        self.clear_button.setPosition((590, 610))
        self.clear_button.click_listener = self
        self.clear_button.setTooltipText("Clear button for destructing existing buildings and infrastructure.")

        ###### Resources and population indicators: ######
        self.panel_lower = Panel(800, 40)
        self.panel_lower.setPosition((0, 760))

        top_offset = 24
        left_offset = 10
        left_step = 140

        self.food_indicator_icon = Icon(loadImage("assets/gui/food_icon.png"))
        self.food_indicator_icon.setPosition((left_offset, 740 + top_offset))
        self.food_indicator_label = Label("food: 100 t", 12)
        self.food_indicator_label.setPosition((left_offset + 40, 748 + top_offset))

        self.steel_indicator_icon = Icon(loadImage("assets/gui/steel_icon.png"))
        self.steel_indicator_icon.setPosition((left_offset + left_step, 740 + top_offset))
        self.steel_indicator_label = Label("steel: 10 t", 12)
        self.steel_indicator_label.setPosition((left_offset + left_step + 40, 748 + top_offset))

        self.energy_indicator_icon = Icon(loadImage("assets/gui/energy_icon.png"))
        self.energy_indicator_icon.setPosition((left_offset + left_step * 2, 740 + top_offset))
        self.energy_indicator_label = Label("power: 10 mWh", 12)
        self.energy_indicator_label.setPosition((left_offset + left_step * 2 + 40, 748 + top_offset))

        self.coal_indicator_icon = Icon(loadImage("assets/gui/coal_icon.png"))
        self.coal_indicator_icon.setPosition((left_offset + left_step * 3 + 30, 740 + top_offset))
        self.coal_indicator_label = Label("coal: 10 t", 12)
        self.coal_indicator_label.setPosition((left_offset + left_step * 3 + 40  + 30, 748 + top_offset))

        self.population_indicator_icon = Icon(loadImage("assets/gui/population_icon.png"))
        self.population_indicator_icon.setPosition((left_offset + left_step * 4 + 30,  740 + top_offset))
        self.population_indicator_label = Label("pop: 100", 12)
        self.population_indicator_label.setPosition((left_offset + left_step * 4 + 40 + 30, 748 + top_offset))

    def show(self):
        self.main.gui.addWidget(self.panel_upper)
        self.main.gui.addWidget(self.connector_button)
        self.main.gui.addWidget(self.green_dome_button)
        self.main.gui.addWidget(self.population_quarters_button)
        self.main.gui.addWidget(self.coal_miner_button)
        self.main.gui.addWidget(self.coal_processor_button)
        self.main.gui.addWidget(self.power_station_button)
        self.main.gui.addWidget(self.supply_station_button)
        # self.main.gui.addWidget(self.research_center_button)
        self.main.gui.addWidget(self.clear_button)

        self.main.gui.addWidget(self.panel_lower)
        self.main.gui.addWidget(self.food_indicator_icon)
        self.main.gui.addWidget(self.food_indicator_label)
        self.main.gui.addWidget(self.steel_indicator_icon)
        self.main.gui.addWidget(self.steel_indicator_label)
        self.main.gui.addWidget(self.energy_indicator_icon)
        self.main.gui.addWidget(self.energy_indicator_label)
        self.main.gui.addWidget(self.coal_indicator_icon)
        self.main.gui.addWidget(self.coal_indicator_label)
        self.main.gui.addWidget(self.population_indicator_icon)
        self.main.gui.addWidget(self.population_indicator_label)

    def onClick(self, event, widget):
        if widget == self.clear_button:
            clear_mode = self.main.modes.clear_mode
            self.main.setMode(clear_mode)
        else:
            placement_mode = self.main.modes.placement_mode
                
            if widget == self.connector_button:
                placement_mode.setPlaceableDescriber(ConnectorPlaceableDescriber(self.main))
            elif widget == self.green_dome_button:
                placement_mode.setPlaceableDescriber(GreenDomeDescriber(self.main))
            elif widget == self.population_quarters_button:
                placement_mode.setPlaceableDescriber(PopulationQuartersDescriber(self.main))
            elif widget == self.supply_station_button:
                placement_mode.setPlaceableDescriber(SupplyStationDescriber(self.main))
            elif widget == self.research_center_button:
                placement_mode.setPlaceableDescriber(ResearchCenterDescriber(self.main))
            elif widget == self.coal_miner_button:
                placement_mode.setPlaceableDescriber(CoalMinerDescriber(self.main))
            elif widget == self.power_station_button:
                placement_mode.setPlaceableDescriber(PowerStationDescriber(self.main))
            elif widget == self.coal_processor_button:
                placement_mode.setPlaceableDescriber(CoalProcessorDescriber(self.main))


            self.main.setMode(placement_mode)

    def onResize(self, delta_width, delta_height):
        attrs = dir(self)
        for key in attrs:
            attribute = getattr(self, key)
            if isinstance(attribute, Widget):
                old_x, old_y = attribute.getPosition()
                new_y = old_y + delta_height
                attribute.setPosition((old_x, new_y))
            if isinstance(attribute, Panel):
                old_w, old_h = attribute.getSize()
                new_w = old_w + delta_width
                attribute.setSize((new_w, old_h))

# fmt: on
