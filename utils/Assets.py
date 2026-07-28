import pygame
import os

from view.Animation import Animation

images = {}

def loadImage(path):
    if path in images:
        return images[path]
    else:
        try:
            images[path] = pygame.image.load(path).convert_alpha()
            return images[path]
        except FileNotFoundError:
            print("Cant load image: " + path)
            raise FileNotFoundError



animations = {}

def loadAnimation(dir_path):
    if dir_path in animations:
        return animations[dir_path]
    else:
        filepaths = os.listdir(dir_path)
        frames = []
        for filepath in filepaths:
            image = loadImage(dir_path + os.sep + filepath)
            frames.append(image)

        animation = Animation(frames)
        animations[dir_path] = animation
        return animation



sounds = {}

def loadSound(path) -> pygame.mixer.Sound:
    if path in sounds:
        return sounds[path]
    else:
        try:
            sounds[path] = pygame.mixer.Sound(path)
            return sounds[path]
        except FileNotFoundError:
            print("Cant load sound: " + path)
            raise FileNotFoundError