import pygame

from . import config
from .character import Mood

MOOD_FILE_NAMES = {
    Mood.CALM : "calmo",
    Mood.SLEEPING : "dormindo",
    Mood.HAPPY : "feliz",
}


def load_sprites():
    sprites = {}
    for mood, name in MOOD_FILE_NAMES.items():
        frames = []
        for number in range(1, config.FRAMES_PER_MOOD + 1):
            path =  config.SPRITES_DIR / "slime_{}_{}.png".format(name, number)
            image = pygame.image.load(path).convert_alpha()
            size = (
                image.get_width() * config.SPRITE_SCALE,
                image.get_height() * config.SPRITE_SCALE, 
            )
            frames.append(pygame.transform.scale(image, size))
        sprites[mood] = frames
    return sprites
