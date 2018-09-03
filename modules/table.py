from modules.bet import Bet

class Table:
    ''' Contains all the Bets created by the Player object
        It is defined by the betting limit '''

    def __init__(self, limit: int):
        self.limit = limit
        self.bets = []

    def isValid(self, bet: Bet):
        ''' Checks whether the sum of all bets including the added Bet
            is under the bet limit '''
            
        if sum(bet.amountBet for bet in self.bets) + bet.amountBet <= self.limit:
            return True
        else:
            return False

    def placeBet(self, bet: Bet):
        ''' Checks whether the addition of the new bet is valid
            and if it is it adds the bet to self.bets
            if it is invalid it raises InvalidBet '''
            
        if self.isValid(bet):
            self.bets.append(bet)
        else:
            raise InvalidBet('The addition of this bet is invalid because it exceeds the Table limit')

    def clearBets(self):
        self.bets = []
        
    def __iter__(self):
        all_bets = (bet for bet in self.bets)
        return all_bets

    def __str__(self):
        bet_lst = []
        for bet in self.__iter__():
            bet_lst.append(bet.__str__())
        return ', '.join(bet_lst)

class InvalidBet(Exception):
    ''' Custom exception for the cases when and invalid bet is placed '''
    pass
