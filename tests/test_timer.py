from Tamagotchi_Pomodoro import config
from Tamagotchi_Pomodoro.timer import Phase, PomodoroTimer


def test_start_in_focus_and_paused():
    timer = PomodoroTimer()
    assert timer.phase == Phase.FOCUS
    assert timer.running is False
    assert timer.remaining == config.FOCUS_MINUTES * 60


def test_update_does_nothing_while_paused():
    timer = PomodoroTimer()
    before = timer.remaining
    timer.update(10)
    assert timer.remaining == before


def test_update_counts_down_while_running():
    timer = PomodoroTimer()
    before = timer.remaining
    timer.start()
    timer.update(10)
    assert timer.remaining == before -10


def test_finishing_focus_goes_to_break():
    timer = PomodoroTimer()
    timer.start()
    finished = timer.update(config.FOCUS_MINUTES * 60)
    assert finished == Phase.FOCUS
    assert timer.phase == Phase.BREAK
    assert timer.running is False
    assert timer.completed_cycles == 1


def test_skip_does_not_count_as_completed_cycle():
    timer = PomodoroTimer()
    timer.skip()
    assert timer.phase == Phase.BREAK
    assert timer.completed_cycles == 0


def test_formatted_time():
    timer = PomodoroTimer()
    timer.remaining = 65
    assert timer.formatted_time() == "01:05"
    timer.remaining = 0.2
    assert timer.formatted_time() == "00:01"


def test_reset_restores_time_and_pauses():
    timer = PomodoroTimer()
    timer.start()
    timer.update(10)
    assert timer.remaining == (config.FOCUS_MINUTES * 60) - 10
    assert timer.running is True
    timer.reset()
    assert timer.remaining == config.FOCUS_MINUTES * 60
    assert timer.running is False


def test_toggle_inverts_running_state():
    timer = PomodoroTimer()
    assert timer.running is False
    timer.toggle()
    assert timer.running is True
    timer.toggle()
    assert timer.running is False