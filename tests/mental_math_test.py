import importlib
import re
import mental_math

def test_import():
    assert 'random' in importlib.sys.modules

def test_get_random_numbers():
    num1, num2 = mental_math.get_random_numbers(10)
    assert num1 >= 1
    assert num1 <= 10
    assert num2 >= 1
    assert num2 <= 10

def test_addition_correct(capsys, monkeypatch):
    arg1 = 2
    arg2 = 3
    inputs = "5"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_addition(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('correct', captured.out, re.IGNORECASE)

def test_addition_incorrect(capsys, monkeypatch):
    arg1 = 2
    arg2 = 3
    inputs = "10"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_addition(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('[wrong|incorrect]', captured.out, re.IGNORECASE)

def test_subtraction_correct(capsys, monkeypatch):
    arg1 = 5
    arg2 = 2
    inputs = "3"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_subtraction(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('correct', captured.out, re.IGNORECASE)

def test_subtraction_incorrect(capsys, monkeypatch):
    arg1 = 5
    arg2 = 2
    inputs = "10"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_subtraction(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('[wrong|incorrect]', captured.out, re.IGNORECASE)

def test_multiplication_correct(capsys, monkeypatch):
    arg1 = 5
    arg2 = 2
    inputs = "10"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_multiplication(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('correct', captured.out, re.IGNORECASE)

def test_multiplication_incorrect(capsys, monkeypatch):
    arg1 = 5
    arg2 = 2
    inputs = "3"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_multiplication(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('[wrong|incorrect]', captured.out, re.IGNORECASE)

def test_division_correct(capsys, monkeypatch):
    arg1 = 10
    arg2 = 2
    inputs = "5"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_division(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('correct', captured.out, re.IGNORECASE)

def test_division_incorrect(capsys, monkeypatch):
    arg1 = 10
    arg2 = 2
    inputs = "3"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    mental_math.test_division(arg1, arg2)
    captured = capsys.readouterr()
    assert re.search('[wrong|incorrect]', captured.out, re.IGNORECASE)