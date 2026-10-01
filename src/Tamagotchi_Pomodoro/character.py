from enum import Enum, auto

from . import config
from .timer import Phase


class Mood(Enum):
    CALM = auto()
    SLEEPING = auto()
    HAPPY = auto()

class Character:
    def __init__(self):
        self.mood = Mood.CALM
        self.frame = 0
        self._frame_clock = 0.0
        self._happy_left = 0.0

    def celebrate(self):
        self._happy_left = config.HAPPY_SECONDS

    def update(self, dt, phase):
        self._frame_clock += dt
        if self._frame_clock >= config.FRAME_SECONDS:
            self._frame_clock -= config.FRAME_SECONDS
            self.frame = (self.frame + 1) % config.FRAMES_PER_MOOD

        if self._happy_left > 0:
            self._happy_left -= dt
            self.mood = Mood.HAPPY
        elif phase == Phase.FOCUS:
            self.mood = Mood.CALM
        else:
            self.mood = Mood.SLEEPING