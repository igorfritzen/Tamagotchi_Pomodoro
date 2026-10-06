import pygame

from . import config
from .assets import load_sprites, load_sounds
from .character import Character
from .timer import Phase, PomodoroTimer
from .ui import Interface
from . import config, overlay

KEY_ACTIONS = {
    pygame.K_SPACE: "toggle",
    pygame.K_r: "reset",
    pygame.K_s: "skip",
    pygame.K_m: "mute",
    pygame.K_t: "pin",
    pygame.K_ESCAPE: "quit",
}


def apply_action(timer, action):
    if action == "toggle":
        timer.toggle()
    elif action == "reset":
        timer.reset()
    elif action == "skip":
        timer.skip()

def main():
    pygame.init()
    flags = pygame.NOFRAME if config.WINDOW_BORDERLESS else 0
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), flags)
    pygame.display.set_caption(config.WINDOW_TITLE)
    clock = pygame.time.Clock()

    sprites = load_sprites()
    sounds = load_sounds()
    timer = PomodoroTimer()
    character = Character()
    ui = Interface()
    muted = False
    pinned = False

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                action = KEY_ACTIONS.get(event.key)
                if action == "mute":
                    muted = not muted
                elif action == "pin":
                    wanted = not pinned
                    if overlay.set_always_on_top(wanted):
                        pinned = wanted
                elif action == "quit":
                    running = False
                else:
                    apply_action(timer, action)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                action = ui.get_actions(event)
                if action == "quit":
                    running = False
                elif action is None:
                    if event.button == 1 and config.WINDOW_BORDERLESS:
                        overlay.start_drag()
                else:
                    apply_action(timer, action)

        finished = timer.update(dt)
        if finished == Phase.FOCUS:
            character.celebrate()
            sound = sounds.get(finished)
            if sound is not None and not muted:
                sound.play()

        if finished == Phase.BREAK:
            character.celebrate()
            sound = sounds.get(finished)
            if sound is not None and not muted:
                sound.play()

        character.update(dt, timer.phase)

        sprite = sprites[character.mood][character.frame]
        ui.draw(screen, timer, sprite, muted)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()