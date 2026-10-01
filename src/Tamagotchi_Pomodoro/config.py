from pathlib import Path

#Pastas
BASE_DIR = Path(__file__).resolve().parents[2]
SPRITES_DIR = BASE_DIR / "assets" / "sprites"
SOUND_DIR = BASE_DIR / "assets" / "sounds"

#Tempo em minutos
FOCUS_MINUTES = 25
BREAK_MINUTES = 5

#Janela
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360
WINDOW_TITLE = "Tamagoshi Pomodoro"
FPS = 60

#Pixel_art
SPRITE_SCALE = 8

#Cores
BACKGROUND_COLOR = (10, 26, 47)
TEXT_COLOR = (230, 230, 240)

#Personagem
HAPPY_SECONDS = 3
FRAME_SECONDS = 0.5
FRAMES_PER_MOOD = 2
