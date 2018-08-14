import unittest
from roulette import *

class Passenger57Test(unittest.TestCase):

    t = Table(100)
    
    def test1_placebet(self):
        ''' Tests if the bet placed by the player is correctly stored in
            the Table object. '''
        pl = Passenger57(self.t)
        pl.setStake(100)

        pl.placeBets()
        self.assertEqual(self.t.bets[0], Bet(10, Outcome('Black', 1)))

if __name__ == '__main__':
    unittest.main()
