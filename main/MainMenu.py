import sys

import pygame

from gui.Icon import Icon
from gui.Label import Label
from gui.Button import Button
from gui.GUI import GUI
from gui.Panel import Panel
from main.Input import Input
from utils.Assets import loadImage


class MainMenu():

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))

        self.credits_visible = False
        self.credits_panel = None
        self.credits_header = None
        self.credits_text  = None
        self.createCredits()

        self.input = Input()
        self.gui = GUI(self)

        self.new_game_button  = Icon(loadImage("assets/gui/main_menu/new_game.png"))
        self.load_game_button = Icon(loadImage("assets/gui/main_menu/load_game.png"))
        self.credits_button   = Icon(loadImage("assets/gui/main_menu/credits.png"))

        self.new_game_button.setPosition((150, 100))
        self.load_game_button.setPosition((150, 300))
        self.credits_button.setPosition((380, 770))

        self.new_game_button.click_listener = self
        self.load_game_button.click_listener = self
        self.credits_button.click_listener = self

        self.gui.addWidget(self.new_game_button)
        self.gui.addWidget(self.load_game_button)
        self.gui.addWidget(self.credits_button)

        self.looping = True

        while self.looping:
            for event in pygame.event.get():
                self.gui.onEvent(event)

                if event.type == pygame.QUIT:
                    self.looping = False
                    sys.exit(0)

            self.window.fill((255,255,255))
            self.gui.draw()
            pygame.display.update()


        self.gui.removeWidget(self.new_game_button)
        self.gui.removeWidget(self.load_game_button)
        self.gui.removeWidget(self.credits_button)

    def createCredits(self):
        self.credits_panel = Panel(780, 700)
        self.credits_panel.setPosition((10,50))

        self.credits_header = Label("Credits", 32)
        self.credits_header.setPosition((20, 20))

        with open("credits.txt") as f:
            contents = f.read()

        credits_font = pygame.font.Font("assets/fonts/ArchivoNarrow-Regular.ttf", 14)
        self.credits_text = Label(contents, 14, credits_font)
        self.credits_text.setPosition((20,80))


    def onClick(self, event, widget):
        if widget == self.new_game_button:
            self.looping = False

        if widget == self.credits_button:
            if not self.credits_visible:
                self.gui.addWidget(self.credits_panel)
                self.gui.addWidget(self.credits_header)
                self.gui.addWidget(self.credits_text)
                self.credits_visible = True
            else:
                self.gui.removeWidget(self.credits_panel)
                self.gui.removeWidget(self.credits_header)
                self.gui.removeWidget(self.credits_text)
                self.credits_visible = False
