import rock_paper_scissors

def test_rock_paper_scissors():
    plays = [("rock", "rock"), ("rock", "paper"), ("rock", "scissors"), 
            ("paper", "rock"), ("paper", "paper"), ("paper", "scissors"), 
            ("scissors", "rock"), ("scissors", "paper"), ("scissors", "scissors")]
    for p in plays:
        assert rock_paper_scissors.rock_paper_scissors(p[0], p[1]) in [0, 1, 2]

def test_get_player_choice(capsys, monkeypatch):
    inputs = ["rock", "paper", "scissors"]
    for i in inputs:
        monkeypatch.setattr('builtins.input', lambda _: i)
        assert rock_paper_scissors.get_player_choice() == i

def test_get_player_choice_invalid(capsys, monkeypatch):
    inputs = iter(["blue", "rock"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert rock_paper_scissors.get_player_choice() == False

def test_get_computer_choice():
    assert rock_paper_scissors.get_computer_choice() in ["rock", "paper", "scissors"]