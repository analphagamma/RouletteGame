from modules.players import *
from modules.roulettegame import *

class Simulator:
    ''' Main body of the application.
        Creates Wheel, Table and Game objects.
        Simulates sessions
        Initializes Players and Games
        Outputs a final statistical summary of the results. '''


    def __init__(self, player: Player, game):
        self.player = player
        self.game = game

        self.initDuration = 250 # maximum number of bets in a game cycle
        self.initStake = 100 # starting amount of betting money
        self.samples = 50 # number of game cycles to simulate
        
    def session(self):
        ''' Executes a single game sessions.
            It runs until the player.playing() is false.
            
            :returns:
                list '''
        stakeVals = []
        self.player.setStake(self.initStake)
        self.player.setRounds(self.initDuration)
        while self.player.playing():
            self.game.cycle(self.player)
            stakeVals.append(self.player.stake)
        
        return stakeVals

    def gather(self):
        ''' Executes a number of games sessions in samples.

            :returns:
                tuple of 2 lists '''
        durations = [] # list of length the player remained in the game
        maxima = [] # list of maximum stakes for each player

        for n in range(self.samples):
            stakes = self.session()
            durations.append(self.initDuration - self.player.roundsToGo)
            maxima.append(max(stakes))

        return (durations, maxima)
