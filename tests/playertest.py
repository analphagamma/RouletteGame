import unittest
from roulette import *

class PlayerTest(unittest.TestCase):

    t = Table(100)
    
    def test1_setstake(self):
        ''' Tests the initialization of the player's stake '''
        pl = Player(self.t)
        self.assertEqual(pl.stake, 0)
        pl.setStake(100)
        self.assertEqual(pl.stake, 100)

    def test2_setrounds(self):
        ''' Tests the initialization of the number of rounds to go. '''
        pl = Player(self.t)
        self.assertEqual(pl.roundsToGo, 0)
        pl.setRounds(100)
        self.assertEqual(pl.roundsToGo, 100)

    def test3_playing(self):
        ''' Tests the .playing() method for various cases. '''
        pl = Player(self.t)

        self.assertFalse(pl.playing()) # stake == 0, rounds to go == 0

        pl.setStake(100)
        self.assertFalse(pl.playing()) # stake > 0, rounds to go == 0

        pl.setRounds(10)
        self.assertTrue(pl.playing()) # stake > 0, rounds to go > 0

        pl.setStake(0)
        self.assertFalse(pl.playing()) # stake == 0, rounds to go > 0

if __name__ == '__main__':
    unittest.main()
