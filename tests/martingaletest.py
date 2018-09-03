import unittest
from context import table, players, bet, outcome

class MartingaleTest(unittest.TestCase):

    t = table.Table(1000)
    pl = players.Martingale(t)
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
        ''' Tests the the change in the bet1Multiple and lossCount
            variables in a losing condition. '''
        bet1 = bet.Bet(self.pl.betMultiple, outcome.Outcome('Black', 1))
        self.assertEqual(bet1.amountBet, 1)
        self.pl.lose(bet1)
        self.assertEqual(self.pl.lossCount, 1)
        self.assertEqual(self.pl.betMultiple, 2)
        
        bet1 = bet.Bet(self.pl.betMultiple, outcome.Outcome('Black', 1))
        self.assertEqual(bet1.amountBet, 2)
        self.pl.lose(bet1)
        self.assertEqual(self.pl.lossCount, 2)
        self.assertEqual(self.pl.betMultiple, 4)

    def test2_win(self):
        ''' Tests the the change in the bet1Multiple and lossCount
            variables in a winning condition. '''
        bet1 = bet.Bet(self.pl.betMultiple, outcome.Outcome('Black', 1))
        self.assertEqual(bet1.amountBet, 4)
        self.pl.win(bet1)
        self.assertEqual(self.pl.lossCount, 0)
        self.assertEqual(self.pl.betMultiple, 1)

if __name__ == '__main__':
    unittest.main()
