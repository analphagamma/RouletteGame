# RouletteGame

An interpretation of Steven F. Lott's Building Skills in Object-Oriented Design in Python.

## Usage

To run in the Terminal run Python with 2 arguments:
* the game's table limit (integer)
* the player's playing strategy
    available strategies: Martingale (doubles the bet with every loss),
                          Passenger57 (always bets $10 on Black),
                          SevenReds (waits for 7 Reds and then bets Black using Martingale),
                          RandomPlayer (bets $10 on a random outcome)

`python RouletteGame.py <table_limit> <strategy>`

## Dependencies

None. Standard Python3.
