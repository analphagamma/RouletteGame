from modules.outcome import Outcome

class Bet:
    ''' Constructed by the Player class
        It contains an Outcome and the amount '''

    def __init__(self, amountBet: int, outcome: Outcome):
        self.amountBet = amountBet
        self.outcome = outcome

    def winAmount(self):
        ''' Returns the amount won:
            the amount bet multiplied by the outcome odds '''
        return self.outcome.winAmount(self.amountBet)

    def loseAmount(self):
        ''' Returns the amount lose '''
        return -(self.amountBet)

    def __str__(self):
        return '${} on {}'.format(self.amountBet, self.outcome)

    def __eq__(self, other: object):
        if self.amountBet == other.amountBet and self.outcome == other.outcome:
            return True
        else:
            return False
