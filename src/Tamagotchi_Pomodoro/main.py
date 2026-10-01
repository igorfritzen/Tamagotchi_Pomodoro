import pygame

from . import config
from .assets import load_sprites
from .character import Character
from .timer import Phase

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.WINDOW_TITLE)
    clock = pygame.time.Clock()

    sprites = load_sprites()
    character = Character()
    phase = Phase.FOCUS

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    character.celebrate()
                elif event.key == pygame.K_b:
                    if phase == Phase.FOCUS:
                        phase = Phase.BREAK
                    else:
                        phase = Phase.FOCUS

        character.update(dt, phase)

        screen.fill(config.BACKGROUND_COLOR)
        image = sprites[character.mood][character.frame]
        rect = image.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2))
        screen.blit(image, rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()