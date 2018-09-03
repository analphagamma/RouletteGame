import unittest
from context import outcome, bet


class BetTest(unittest.TestCase):
    ''' Tests the roulette.Bet class by creating Outcome objects and
        checking the win-lose calculations '''

    oc1 = outcome.Outcome('0-00-1-2-3', 5)
    oc2 = outcome.Outcome('Red', 1)

    def test_winbet(self):
        bet1 = bet.Bet(100, self.oc1)
        self.assertEqual(bet1.winAmount(), 500)

    def test_losebet(self):
        bet2 = bet.Bet(10, self.oc2)
        self.assertEqual(bet2.loseAmount(), -10)

    def test_str(self):
        bet3 = bet.Bet(100, self.oc2)
        self.assertEqual(bet3.__str__(), '$100 on Red (odds 1:1)')

if __name__ == '__main__':
    unittest.main()
