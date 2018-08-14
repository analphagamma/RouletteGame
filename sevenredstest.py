import unittest
from roulette import *
from wheeltest import NonRandom

class SevenRedsTest(unittest.TestCase):

    nrnd = NonRandom(1) # rolls 1, Odd, Red
    wh = Wheel(nrnd)
    bb = BinBuilder()
    bb.buildBins(wh)
    t = Table(1000)
    game = RouletteGame(wh, t) 
    pl = SevenReds(t)
    pl.setStake(100)
    pl.setRounds(10)
    
    def test1_init(self):
        ''' Tests the initialization of the Martingale Player.
            Checks initial variables. '''
        self.assertEqual(self.pl.stake, 100)
        self.assertEqual(self.pl.roundsToGo, 10)
        self.assertEqual(self.pl.lossCount, 0)
        self.assertEqual(self.pl.betMultiple, 1)
        self.assertEqual(self.pl.redCount, 0)

    def test2_roll6reds(self):
        for roll in range(6):
            self.game.cycle(self.pl)

        self.assertEqual(self.pl.redCount, 6)

    def test3_roll2reds(self):
        for roll in range(2):
            self.game.cycle(self.pl)

        self.assertEqual(self.pl.redCount, 1)
        self.assertEqual(self.pl.betMultiple, 2)
        
if __name__ == '__main__':
    unittest.main()
