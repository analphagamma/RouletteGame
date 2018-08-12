import unittest
from roulette import *

class TableTest(unittest.TestCase):

    oc1 = Outcome('Line 0-00-1-2-3', 5)
    oc2 = Outcome('Red', 1)
    bet1 = Bet(110, oc1)
    bet2 = Bet(5, oc2)
    t0 = Table(100)
    t1 = Table(100)
    t2 = Table(200)
      
    def test1_isvalid(self):
        ''' Tests the bet validity check
            The first test will test for a True case
            the second one tests for False '''
      
        self.assertTrue(self.t1.isValid(self.bet2))
        self.assertFalse(self.t1.isValid(self.bet1))

    def test2_placebet(self):
        ''' Tests the correct handling of bet placing
            It adds a valid bet and checks if it was stored.
            Then it adds an another one making it invalid
            and expects the custom Exception '''
            
        self.t0.placeBet(self.bet2)
        self.assertEqual(self.t0.bets, [self.bet2])
        self.assertRaises(InvalidBet, self.t0.placeBet, self.bet1)
        
    def test3_str(self):
        ''' Tests the str output of the class
            It checks it with no bets added
            Then it tests with one added, then with two added. '''
            
        self.assertEqual(self.t2.__str__(),
                         '')
        self.t2.placeBet(self.bet1)
        self.assertEqual(self.t2.__str__(),
                         '$110 on Line 0-00-1-2-3 (odds 5:1)')

        self.t2.placeBet(self.bet2)
        self.assertEqual(self.t2.__str__(),
                         '$110 on Line 0-00-1-2-3 (odds 5:1), $5 on Red (odds 1:1)')

    def test4_iter(self):
        ''' Iterates through a Table object '''
        
        bets = []
        for bet in self.t2:
            bets.append(bet)

        self.assertEqual(bets, [self.bet1, self.bet2])

    def test5_clearbets(self):
        self.assertTrue(len(self.t2.bets) > 0)
        self.t2.clearBets()
        self.assertEqual(len(self.t2.bets), 0)
       

if __name__ == '__main__':
    unittest.main()
