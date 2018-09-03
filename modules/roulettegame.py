from modules.wheel import Wheel
from modules.table import *

class RouletteGame:
    ''' Main game class
        It's made up of a Wheel and a Table object
        It's used by Player to make Bets '''
        
    def __init__(self, wheel: Wheel, table: Table):
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        ''' Main game loop
            first Bets are placed by Players,
            then the Wheel is spun,
            then the Outcomes are compared '''

        # Bets placed if Player is still playing  
        if not player.playing():
            return

        self.table.clearBets() # clear the table
        player.placeBets() # place bets
        roll = self.wheel.next_roll() # Roll
        player.roundsToGo -= 1
        player.winners(roll.outcomes) # sends winner Outcomes to Player
        
        # Outcomes are compared
        for bet in self.table:
            player.stake -= bet.amountBet
            if player.stake < 0:
                player.stake = 0
                return
            if bet.outcome in roll.outcomes:
                return player.win(bet)
            else:
                return player.lose(bet)
