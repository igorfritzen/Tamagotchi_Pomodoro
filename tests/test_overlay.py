import sys

from Tamagotchi_Pomodoro import overlay


def test_always_on_top_is_not_supported_outside_windows(monkeypatch):
    monkeypatch.setattr(sys, "platform", "linux")
    assert overlay.is_supported() is False
    assert overlay.set_always_on_top(True) is False


def test_support_is_detected_on_windows(monkeypatch):
    monkeypatch.setattr(sys, "platform", "win32")
    assert overlay.is_supported() is True


def test_start_drag_does_nothing_outside_windows(monkeypatch):
    monkeypatch.setattr(sys, "platform", "linux")
    assert overlay.start_drag() is None