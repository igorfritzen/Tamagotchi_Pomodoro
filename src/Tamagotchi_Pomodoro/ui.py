import pygame

from . import config
from .timer import Phase

PHASE_LABELS = {
    Phase.FOCUS: "FOCO",
    Phase.BREAK: "PAUSA"
}


class Interface:
    def __init__(self):
        self.time_font = pygame.font.Font(None, config.TIME_FONT_SIZE)
        self.info_font = pygame.font.Font(None, config.INFO_FONT_SIZE)
        self.hint_font = pygame.font.Font(None, config.HINT_FONT_SIZE)


    def draw_text(self, screen, text, font, center):
        surface = font.render(text, True, config.TEXT_COLOR)
        rect = surface.get_rect(center=center)
        screen.blit(surface, rect)


    def draw(self, screen, timer, sprite):
        screen.fill(config.BACKGROUND_COLOR)
        center_x = config.WINDOW_WIDTH // 2

        self.draw_text(screen, PHASE_LABELS[timer.phase], self.info_font, (center_x, 28))

        sprite_rect = sprite.get_rect(center=(center_x, 150))
        screen.blit(sprite, sprite_rect)

        self.draw_text(screen, timer.formatted_time(), self.time_font, (center_x, 275))

        status = "rodando" if timer.running else "parado"
        info = "Ciclos: {} | {}".format(timer.completed_cycles, status)
        self.draw_text(screen, info, self.info_font, (center_x, 322))

        hint = "ESPAÇO iniciar/pausar   R resetar   S pular"
        self.draw_text(screen, hint, self.hint_font, (center_x, 347))