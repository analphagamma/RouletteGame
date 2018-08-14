import unittest
from roulette import *


class BinTest(unittest.TestCase):
    ''' Creates 5 instances of Outcome objects
        tests whether Bin objects can be created
        adds an Outcome object to the frozenset inside the Bin object'''

    oc1 = Outcome('2', 35)
    oc2 = Outcome('1-2-3-4-5-6', 5)
    oc3 = Outcome('red', 1)
    oc4 = Outcome('1-2', 17)
    oc5 = Outcome('0-00-1-2-3', 6)

    bin1 = Bin(oc1, oc2, oc4) # rolls 2 - needs oc5 added
    bin2 = Bin(oc2, oc3, oc4) # rolls 1 - red

    def test_add_to_Bin(self):
        '''Adds a new element to the Bin object's frozenset class variable
           and tests whether the addition was successful'''
        
        self.bin1.add(self.oc5)
        self.assertEqual(self.bin1.outcomes, frozenset([self.oc1, self.oc2, self.oc4, self.oc5]))


if __name__ == '__main__':
    unittest.main()
