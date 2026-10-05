from Tamagotchi_Pomodoro import config
from Tamagotchi_Pomodoro.character import Character, Mood
from Tamagotchi_Pomodoro.timer import Phase
from pytest import approx

from Tamagotchi_Pomodoro.character import Character, Mood, energy_level


def test_starts_calm_on_first_frame():
    character = Character()
    assert character.mood == Mood.CALM
    assert character.frame == 0


def test_mood_is_calm_during_focus():
    character = Character()
    character.update(0.1, Phase.FOCUS)
    assert character.mood == Mood.CALM


def test_mood_is_sleeping_during_break():
    character = Character()
    character.update(0.1, Phase.BREAK)
    assert character.mood == Mood.SLEEPING


def test_celebrate_makes_character_happy():
    character = Character()
    character.celebrate()
    character.update(0.1, Phase.BREAK)
    assert character.mood == Mood.HAPPY


def test_happiness_wears_off_and_phase_mood_returns():
    character = Character()
    character.celebrate()
    character.update(config.HAPPY_SECONDS, Phase.BREAK)
    assert character.mood == Mood.HAPPY
    character.update(0.1, Phase.BREAK)
    assert character.mood == Mood.SLEEPING


def test_frame_does_not_change_before_frame_time():
    character = Character()
    character.update(config.FRAME_SECONDS / 2, Phase.FOCUS)
    assert character.frame == 0


def test_frame_alternates_after_frame_time():
    character = Character()
    character.update(config.FRAME_SECONDS, Phase.FOCUS)
    assert character.frame == 1
    character.update(config.FRAME_SECONDS, Phase.FOCUS)
    assert character.frame == 0


def test_energy_is_full_at_start_of_focus():
    assert energy_level(Phase.FOCUS, 0) == 1


def test_energy_is_empty_at_end_of_focus():
    assert energy_level(Phase.FOCUS, 1) == 0


def test_energy_is_empty_at_start_of_break():
    assert energy_level(Phase.BREAK, 0) == 0


def test_energy_is_full_at_end_of_break():
    assert energy_level(Phase.BREAK, 1) == 1


def test_energy_drops_in_focus_and_recovers_in_break():
    assert energy_level(Phase.FOCUS, 0.25) == approx(0.75)
    assert energy_level(Phase.BREAK, 0.25) == approx(0.25)