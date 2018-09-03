class Outcome:
    ''' The Outcome object holds a bet's name and its odds
        It can return the amount won if the bet was successful '''
        
    def __init__(self, name: str, odds: int):
        self.name = name
        self.odds = odds

    def winAmount(self, amount: int):
        return amount * self.odds

    def __eq__(self, other: object):
        if self.name == other.name:
            return True
        else:
            return False

    def __ne__(self, other: object):
        if self.name != other.name:
            return True
        else:
            return False

    def __str__(self):
        return '{} (odds {}:1)'.format(self.name, self.odds)

    def __hash__(self):
        return 0
