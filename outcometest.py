import unittest
from roulette import *


class OutcomeTest(unittest.TestCase):
    ''' Tests the class:Outcome
        creates 3 instances 2 of which are identical '''

    oc1 = Outcome('1', 35)
    oc2 = Outcome('1', 35)
    oc3 = Outcome('35', 35)

    def test_equaltrue(self):
        ''' Tests equality between 2 objects '''
        
        self.assertTrue(self.oc1 == self.oc2)
        
    def test_equalfalse(self):
        ''' Tests whether the equality check faiis if needed '''
        
        self.assertFalse(self.oc1 == self.oc3)

    def test_not_equaltrue(self):
        ''' Tests "not equal" between 2 objects '''

        self.assertTrue(self.oc1 != self.oc3)
        
    def test_not_equalfalse(self):
        ''' Tests whether the "not equal" check fails if needed '''

        self.assertFalse(self.oc1 != self.oc2)

    def test_description(self):
        ''' Tests if the __str__() method returns the correct string '''

        self.assertEqual(self.oc1.__str__(), '1 (odds 35:1)')

    def test_winAmount(self):
        ''' Tests the calculation of the winning '''

        self.assertEqual(self.oc1.winAmount(10), 350)

        
if __name__ == '__main__':
    unittest.main()
    
    
