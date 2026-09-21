import funct


def test_play_again_resets_game_state(monkeypatch):
    responses = iter(["y"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    result = funct.play_again(2, 1, 10, 3, 2)

    assert result == (1, 1, 5, 0, 1)


def test_check_guess_incorrect_guess_reduces_attempts():
    result = funct.check_guess(4, 7, 1, 1, 10, 0, 1)

    assert result == (1, 0, 10, 0, 1)


def test_check_guess_correct_guess_advances_difficulty():
    result = funct.check_guess(7, 7, 1, 1, 10, 0, 1)

    assert result == (2, 1, 10, 1, 1)
