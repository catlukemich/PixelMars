import pygame
import pyttsx3

from main.MainMenu import MainMenu
from main.Game import Game
from utils.Speech import Speech



if __name__ == '__main__':
    pygame.init()
    engine = pyttsx3.init()
    main_menu = MainMenu()

    main = Game()
    main.loop()



