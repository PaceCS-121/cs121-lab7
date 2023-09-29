import importlib
import re
import generate_password

def test_import():
    assert 'random' in importlib.sys.modules

def test_generate_password_12():
    pw = generate_password.generate_password(12)
    assert len(pw) == 12
    assert re.search('[A-Z]', pw)
    assert re.search('[a-z]', pw)
    assert re.search('[0-9]', pw)
    assert re.search('[!@#$%^&*()_+-=]', pw)

def test_generate_password_20():
    pw = generate_password.generate_password(20)
    assert len(pw) == 20
    assert re.search('[A-Z]', pw)
    assert re.search('[a-z]', pw)
    assert re.search('[0-9]', pw)
    assert re.search('[!@#$%^&*()_+-=]', pw)

def test_inputs_14(capsys, monkeypatch):
    inputs = "14"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    generate_password.main()
    captured = capsys.readouterr()
    assert re.search('[A-Z]', captured.out)
    assert re.search('[a-z]', captured.out)
    assert re.search('[0-9]', captured.out)
    assert re.search('[!@#$%^&*()_+-=]', captured.out)

def test_inputs_8(capsys, monkeypatch):
    inputs = "8"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    generate_password.main()
    captured = capsys.readouterr()
    assert re.search('10 char', captured.out, re.IGNORECASE)
    