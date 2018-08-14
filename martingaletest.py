import unittest
from roulette import *

class MartingaleTest(unittest.TestCase):

    t = Table(1000)
    pl = Martingale(t)
    pl.setStake(100)
    pl.setRounds(10)
    
    def test1_init(self):
        ''' Tests the initialization of the Martingale Player.
            Checks initial variables. '''
        self.assertEqual(self.pl.stake, 100)
        self.assertEqual(self.pl.roundsToGo, 10)
        self.assertEqual(self.pl.lossCount, 0)
        self.assertEqual(self.pl.betMultiple, 1)

    def test2_loss(self):
        ''' Tests the the change in the betMultiple and lossCount
            variables in a losing condition. '''
        bet = Bet(self.pl.betMultiple, Outcome('Black', 1))
        self.assertEqual(bet.amountBet, 1)
        self.pl.lose(bet)
        self.assertEqual(self.pl.lossCount, 1)
        self.assertEqual(self.pl.betMultiple, 2)
        
        bet = Bet(self.pl.betMultiple, Outcome('Black', 1))
        self.assertEqual(bet.amountBet, 2)
        self.pl.lose(bet)
        self.assertEqual(self.pl.lossCount, 2)
        self.assertEqual(self.pl.betMultiple, 4)

    def test2_win(self):
        ''' Tests the the change in the betMultiple and lossCount
            variables in a winning condition. '''
        bet = Bet(self.pl.betMultiple, Outcome('Black', 1))
        self.assertEqual(bet.amountBet, 4)
        self.pl.win(bet)
        self.assertEqual(self.pl.lossCount, 0)
        self.assertEqual(self.pl.betMultiple, 1)

if __name__ == '__main__':
    unittest.main()
