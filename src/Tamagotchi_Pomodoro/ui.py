import pygame

from . import config
from .timer import Phase

PHASE_LABELS = {
    Phase.FOCUS: "FOCO",
    Phase.BREAK: "PAUSA"
}


class Button:
    def __init__(self, label, rect):
        self.label = label
        self.rect = pygame.Rect(rect)


    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


    def was_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )    


    def draw(self, screen, font):
        if self.is_hovered():
            color = config.BUTTON_HOVER_COLOR
        else:
            color = config.BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        text = font.render(self.label, True, config.BUTTON_TEXT_COLOR)
        screen.blit(text, text.get_rect(center=self.rect.center))
        

class Interface:
    def __init__(self):
        self.time_font = pygame.font.Font(None, config.TIME_FONT_SIZE)
        self.info_font = pygame.font.Font(None, config.INFO_FONT_SIZE)
        self.buttons = self._create_buttons()

    def _create_buttons(self):
        labels = {"toggle": "Iniciar", "reset": "Resetar", "skip": "Pular"}
        total_width = len(labels) * config.BUTTON_WIDTH + (len(labels) - 1) * config.BUTTON_GAP
        x = (config.WINDOW_WIDTH - total_width) // 2


        buttons = {}
        for action, label in labels.items():
            rect = (x, config.BUTTON_Y, config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
            buttons[action] = Button(label, rect)
            x +=config.BUTTON_WIDTH + config.BUTTON_GAP
        return buttons


    def get_actions(self, event):
        for action, button in self.buttons.items():
            if button.was_clicked(event):
                return action
        return None


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

        self.draw_text(screen, timer.formatted_time(), self.time_font, (center_x, 262))

        status = "rodando" if timer.running else "parado"
        info = "Ciclos: {} | {}".format(timer.completed_cycles, status)
        self.draw_text(screen, info, self.info_font, (center_x, 298))

        if timer.running:
            self.buttons["toggle"].label = "Pausar"
        else:
            self.buttons["toggle"].label = "Iniciar"
        for button in self.buttons.values():
            button.draw(screen, self.info_font)