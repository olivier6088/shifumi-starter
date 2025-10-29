from shifumi.game import determine_winner

def test_win_conditions():
    assert determine_winner("rock", "scissors") == "win"
    assert determine_winner("paper", "rock") == "win"
    assert determine_winner("scissors", "paper") == "win"

def test_tie():
    assert determine_winner("rock", "rock") == "tie"

def test_invalid_input():
    assert determine_winner("banana", "rock") == "invalid"
    assert determine_winner("rock", "banana") == "invalid"

def test_case_insensitivity():
    assert determine_winner("Rock", "Scissors") == "win"
    assert determine_winner(" PAPER ", "rock") == "win"

# =============================================================================

# Tests de validation d'entrées

def test_invalid_player_choice():
    assert determine_winner("banana", "rock") == "invalid"

def test_invalid_computer_choice():
    assert determine_winner("rock", "banana") == "invalid"

def test_both_invalid():
    assert determine_winner("banana", "banana") == "invalid"
    
# Tests de normalisation

def test_normalization_spaces_and_case():
    assert determine_winner(" Rock ", "Scissors") == "win"
    assert determine_winner("PAPER", "rock") == "win"
    assert determine_winner("scissors", "SCISSORS") == "tie"

# Tests de couverture complète des cas de défaite

def test_lose_conditions():
    assert determine_winner("rock", "paper") == "lose"
    assert determine_winner("paper", "scissors") == "lose"
    assert determine_winner("scissors", "rock") == "lose"

# Test de robustesse sur des entrées inattendues

def test_numeric_input():
    assert determine_winner("123", "rock") == "invalid"

def test_empty_string():
    assert determine_winner("", "rock") == "invalid"

