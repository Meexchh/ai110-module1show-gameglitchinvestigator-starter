from logic_utils import check_guess

def test_guess_above_secret_says_go_lower():
    outcome, message = check_guess(97, 93)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_below_secret_says_go_higher():
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
