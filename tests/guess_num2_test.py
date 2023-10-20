import random
import re
import guess_the_number2

inputs = iter(random.sample(range(1, 101), 50))

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
    assert re.search(r"high|low", captured.out, re.IGNORECASE)

def test_play(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    guess_the_number2.main()
    captured = capsys.readouterr()
    assert re.search(r"congrat|win|sorry|lose", captured.out, re.IGNORECASE)
    assert re.search(r"\d+ guesses", captured.out, re.IGNORECASE)