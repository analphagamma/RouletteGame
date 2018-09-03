import unittest
from context import outcome, bin


class BinTest(unittest.TestCase):
    ''' Creates 5 instances of outcome.Outcom objects
        tests whether bin.Bin objects can be created
        adds an outcome.Outcom object to the frozenset inside the bin.Bin object'''

    oc1 = outcome.Outcome('2', 35)
    oc2 = outcome.Outcome('1-2-3-4-5-6', 5)
    oc3 = outcome.Outcome('red', 1)
    oc4 = outcome.Outcome('1-2', 17)
    oc5 = outcome.Outcome('0-00-1-2-3', 6)

    bin1 = bin.Bin(oc1, oc2, oc4) # rolls 2 - needs oc5 added
    bin2 = bin.Bin(oc2, oc3, oc4) # rolls 1 - red

    def test_add_to_bin(self):
        '''Adds a new element to the bin.Bin object's frozenset class variable
           and tests whether the addition was successful'''
        
        self.bin1.add(self.oc5)
        self.assertEqual(self.bin1.outcomes, frozenset([self.oc1, self.oc2, self.oc4, self.oc5]))


if __name__ == '__main__':
    unittest.main()
