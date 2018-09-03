import unittest
from context import table, players, bet, outcome

class Passenger57Test(unittest.TestCase):

    t = table.Table(100)
    
    def test1_placebet(self):
        ''' Tests if the bet placed by the player is correctly stored in
            the Table object. '''
        pl = players.Passenger57(self.t)
        pl.setStake(100)

        pl.placeBets()
        self.assertEqual(self.t.bets[0], bet.Bet(10, outcome.Outcome('Black', 1)))

if __name__ == '__main__':
    unittest.main()
