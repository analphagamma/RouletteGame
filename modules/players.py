import random
from modules.table import *
from modules.wheel import Wheel
from modules.binbuilder import BinBuilder
from modules.bet import Bet
from modules.outcome import Outcome

class Player:
    ''' This class is responsible to create Bets from valid Outcomes
        and within the Table's limit.
        It manages its account'''
        
    def __init__(self, table: Table):
        self.table = table
        self.roundsToGo = 0
        self.stake = 0

    def setStake(self, stake: int):
        ''' Sets the Player's stake. '''
        self.stake = stake

    def setRounds(self, rounds: int):
        ''' Sets the number of rounds the Player
            would play. '''
        self.roundsToGo = rounds
        
    def placeBets(self):
        ''' No body for super class. '''
        pass

    def playing(self):
        ''' Returns True if the Player is still active. '''
        if self.stake <= 0 or self.roundsToGo == 0:
            return False
        else:
            return True

    def winners(self, outcomes: set):
        ''' Returns the set of the most recent cycle's
            winner Outcomes.
            In this parent class this method simply returns the
            Outcomes.
            :returns:
                set. '''
        pass

    def win(self, bet: Bet):
        ''' When notified by Game it increases the Player's
            stake by using the Bet's winAmount() method'''
        self.stake += bet.winAmount() + bet.amountBet

    def lose(self, bet: Bet):
        ''' Because the amount bet is already deducted from the
            stake this method does nothing for now. '''
        pass

class Passenger57(Player):
    ''' A Player class that only bets on Black. '''
    
    def __init__(self, table: Table):
        super().__init__(table)
        self.black = Outcome('Black', 1)

    def placeBets(self):
        ''' Places $10 on Black. '''
        self.table.placeBet(Bet(10, self.black))

        
class Martingale(Player):
    ''' Subclass of Player
        This Player uses the Martingale strategy, that is
        doubling the bet after every loss and returning to the default
        bet after every win until reaching the Table limit. '''

    def __init__(self, table):
        self.table = table
        self.lossCount = 0
        self.betMultiple = 1
        self.black = Outcome('Black', 1)

    def placeBets(self):
        self.table.placeBet(Bet(self.betMultiple, self.black))

    def win(self, bet: Bet):
        ''' If Player wins the lossCount is reset to 0 as well as the
            betMultiple.

            :returns:
                None '''
            
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)
        super(Martingale, self).win(bet)

    def lose(self, bet: Bet):
        ''' If Player loses the lossCount is incremented by one
            and the new betMultiple is calculated.

            When the bet goes over the Table limit the betMultiple is se
            to the last valid amount.

            When the betMultiple becomes bigger than the stake, it will
            reset to 1. When this happens the session ends because the Player
            would run out of money.

            :returns:
                None '''
                
        self.lossCount += 1
        if pow(2, self.lossCount) < self.table.limit:
            self.betMultiple = pow(2, self.lossCount)
        if self.betMultiple > self.stake:
            self.betMultiple = 1
        super(Martingale, self).lose(bet)

class SevenReds(Player):
    ''' This Player waits for seven Red wins in a row and then bets
        black.
        There are 2 states of this class: waiting, and betting. '''

    def __init__(self, table):
        super().__init__(table)
        self.redCount = 0
        self.lossCount = 0
        self.betMultiple = 1
        self.black = Outcome('Black', 1)
               
    def winners(self, outcomes: set):
        ''' This method counts the Red Outcomes that is used
            to determine the behaviour of the Player.

            :returns:
                None '''
                
        for oc in outcomes:
            if oc.name == 'Red':
                self.redCount += 1

    def waiting(self):
        if self.redCount != 7:
            return True
        else:
            return False

    def placeBets(self):
        ''' Places bets on Black following the Martingale strategy
            but only if 7 Red Outcome has been rolled

            :returns:
                None '''
                
        if not self.waiting():
            self.redCount = 0
            self.table.placeBet(Bet(self.betMultiple, self.black))

    def win(self, bet: Bet):
        ''' If Player wins the lossCount is reset to 0 as well as the
            betMultiple

            :returns:
                None '''
            
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)
        super(SevenReds, self).win(bet)

    def lose(self, bet: Bet):
        ''' If Player loses the lossCount is incremented by one
            and the new betMultiple is calculated.

            When the bet goes over the Table limit the betMultiple is se
            to the last valid amount.

            When the betMultiple becomes bigger than the stake, it will
            reset to 1. When this happens the session ends because the Player
            would run out of money.

            :returns:
                None '''
                
        self.lossCount += 1
        if pow(2, self.lossCount) < self.table.limit:
            self.betMultiple = pow(2, self.lossCount)
        if self.betMultiple > self.stake:
            self.betMultiple = 1
        super(SevenReds, self).lose(bet)

class RandomPlayer(Player):

    def __init__(self, table, rng=random):
        super().__init__(table)
        self.rng = rng
        # creating a Wheel class to get a setof all Outcomes
        # TODO // Find another way to do it because this is TOO DAMN SLOW!
        wh = Wheel()
        bb = BinBuilder()
        bb.buildBins(wh)
        self.all_OC = wh.binIterator()

    def placeBets(self):
        ''' Acquires all Outcomes, randomly picks one and places a bet.'''
        
        for i, oc in enumerate(self.all_OC):
            if i == self.rng.randint(0, len(self.all_OC)):
                self.table.placeBet(Bet(10, oc))

class Player1326State():
    # endless iterating:
    # multiples = iter([1,3,2,6])
    # try:
    #   next(multiples)
    # except StopIteration:
    #   multiples = iter([1,3,2,6])
    def __init__(self, player: Player):
        self.player = player

    def currentBet(self):
        ''' Creates a Bet from an Outcome and the multiplier '''
        return None

    def nextWon(self):
        ''' Constructs a new state object based on win history. '''
        return None

    def nextLost(self):
        ''' Constructs a new state if the last bet was a loser. '''
        return None
