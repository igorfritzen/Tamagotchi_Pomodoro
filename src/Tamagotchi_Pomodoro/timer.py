import math
from enum import Enum, auto


from . import config


class Phase(Enum):
    FOCUS = auto()
    BREAK = auto()


class PomodoroTimer:
    def __init__(self):
        self.phase = Phase.FOCUS
        self.remaining = self._duration_of(self.phase)
        self.running = False
        self.completed_cycles = 0


    def _duration_of(self, phase):
        if phase == Phase.FOCUS:
            return config.FOCUS_MINUTES*60
        return config.BREAK_MINUTES*60


    def start(self):
        self.running = True


    def pause(self):
        self.running = False


    def toggle(self):
        self.running = not self.running


    def reset(self):
        self.remaining = self._duration_of(self.phase)
        self.running = False


    def skip(self):
        self._next_phase()


    def update(self, dt):
        if not self.running:
            return None

        self.remaining -=dt
        if self.remaining >0:
            return None

        finished = self.phase
        if finished == Phase.FOCUS:
            self.completed_cycles += 1
        self._next_phase()
        return finished


    def _next_phase(self):
        if self.phase == Phase.FOCUS:
            self.phase = Phase.BREAK
        else:
            self.phase = Phase.FOCUS
        self.remaining = self._duration_of(self.phase)
        self.running = False


    def formatted_time(self):
        total_seconds = max(0, math.ceil(self.remaining))
        minutes, seconds = divmod(total_seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)