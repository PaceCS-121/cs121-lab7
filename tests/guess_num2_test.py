import re
import guess_the_number2

def test_generate_random_number():
    num = guess_the_number2.generate_random_number(1, 100)
    assert num >= 1 and num <= 100

def test_get_user_guess(capsys, monkeypatch):
    inputs = "10"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    assert guess_the_number2.get_user_guess() == 10

def test_check_guess(capsys):
    assert guess_the_number2.check_guess(10, 10) == True
    assert guess_the_number2.check_guess(10, 9) == False
    captured = capsys.readouterr()
    assert "Too high!" in captured.out or "Too low!" in captured.out