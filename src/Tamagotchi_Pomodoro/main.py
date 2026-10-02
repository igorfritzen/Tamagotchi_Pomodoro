import pygame

from . import config
from .assets import load_sprites
from .character import Character
from .timer import Phase, PomodoroTimer
from .ui import Interface

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.WINDOW_TITLE)
    clock = pygame.time.Clock()

    sprites = load_sprites()
    timer = PomodoroTimer()
    character = Character()
    ui = Interface()

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    timer.toggle()
                elif event.key == pygame.K_r:
                    timer.reset()
                elif event.key == pygame.K_s:
                    timer.skip()

        finished = timer.update(dt)
        if finished == Phase.FOCUS:
            character.celebrate()

        character.update(dt, timer.phase)

        sprite = sprites[character.mood][character.frame]
        ui.draw(screen, timer, sprite)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()