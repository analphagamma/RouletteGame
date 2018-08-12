import unittest
from roulette import *


class BetTest(unittest.TestCase):
    ''' Tests the roulette.Bet class by creating Outcome objects and
        checking the win-lose calculations '''

    oc1 = Outcome('0-00-1-2-3', 5)
    oc2 = Outcome('Red', 1)

    def test_winbet(self):
        bet = Bet(100, self.oc1)
        self.assertEqual(bet.winAmount(), 500)

    def test_losebet(self):
        bet = Bet(10, self.oc2)
        self.assertEqual(bet.loseAmount(), -10)

    def test_str(self):
        bet = Bet(100, self.oc2)
        self.assertEqual(bet.__str__(), '$100 on Red (odds 1:1)')

if __name__ == '__main__':
    unittest.main()
