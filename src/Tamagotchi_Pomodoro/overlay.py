import ctypes
import sys
from ctypes import wintypes

import pygame

HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
WM_NCLBUTTONDOWN = 0x00A1
HTCAPTION = 2

def is_supported():
    return sys.platform == "win32"


def set_always_on_top(enabled):
    if not is_supported():
        return False

    hwnd = pygame.display.get_wm_info()["window"]
    insert_after = HWND_TOPMOST if enabled else HWND_NOTOPMOST

    set_window_pos = ctypes.windll.user32.SetWindowPos
    set_window_pos.argtypes = [
        wintypes.HWND,
        wintypes.HWND,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        wintypes.UINT,
    ]
    set_window_pos.restype = wintypes.BOOL

    result = set_window_pos(hwnd, insert_after, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    return bool(result)


def start_drag():
    if not is_supported():
        return 

    hwnd = pygame.display.get_wm_info()["window"]
    user32 = ctypes.windll.user32

    send_message = user32.SendMessageW
    send_message.argtypes = [
        wintypes.HWND,
        wintypes.UINT,
        wintypes.WPARAM,
        wintypes.LPARAM,        
    ]
    send_message.restype = wintypes.LPARAM

    user32.ReleaseCapture()
    send_message(hwnd, WM_NCLBUTTONDOWN, HTCAPTION, 0)