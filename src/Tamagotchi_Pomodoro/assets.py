import pygame

from . import config
from .character import Mood
from .timer import Phase

MOOD_FILE_NAMES = {
    Mood.CALM : "calmo",
    Mood.SLEEPING : "dormindo",
    Mood.HAPPY : "feliz",
}


SOUND_FILE_NAMES = {
    Phase.FOCUS: "fim_foco.wav",
    Phase.BREAK: "fim_pausa.wav",
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


def load_sounds():
    sounds = {}
    if pygame.mixer.get_init() is None:
        return sounds

    for phase, file_name in SOUND_FILE_NAMES.items():
        sound = pygame.mixer.Sound(config.SOUND_DIR / file_name)
        sound.set_volume(config.SOUND_VOLUME)
        sounds[phase] = sound
    return sounds
