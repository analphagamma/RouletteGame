import unittest, random
from roulette import *

class NonRandom(random.Random):
    ''' A Non-random generator for testing purposes '''

    def __init__(self, value):
        self.value = value

    def setSeed(self, value):
        return value

    def choice(self, sequence):
        return sequence[self.setSeed(self.value)]


class NonRandomTest(unittest.TestCase):
    ''' Tests if the NonRandom class return 0'''

    nrnd = NonRandom(0)
    test_sequence = [1,2,3,4,5]

    def test_return_value(self):
        ''' The choice should always be the first element'''
        
        self.assertEqual(self.nrnd.choice(self.test_sequence), 1)


class WheelTest(unittest.TestCase):
    ''' Creates a number of Outcomes that would belong to 2 different Bins
        It tests the addition and the random rolls'''

    nrnd = NonRandom(0)
    wh1 = Wheel(nrnd)
    oc1 = Outcome('Number 0', 35)
    oc2 = Outcome('Line 0-00-1-2-3', 5)
    oc3 = Outcome('Split 1-2', 17)
    oc4 = Outcome('Line 1-2-3-4-5-6', 5)
    oc5 = Outcome('Red', 1)
    bb = BinBuilder()

    def test1_addOutcome(self):
        ''' Tests whether the addition of an Outcome to a Bin was successful '''
        
        self.wh1.addOutcome(0, self.oc1)
        self.wh1.addOutcome(0, self.oc2)
        self.wh1.addOutcome(1, self.oc3)
        self.wh1.addOutcome(1, self.oc4)
        self.wh1.addOutcome(1, self.oc5)
        self.assertEqual(self.wh1.bins[0].outcomes, frozenset([self.oc1, self.oc2]))
        self.assertEqual(self.wh1.bins[1].outcomes, frozenset([self.oc3, self.oc4, self.oc5]))

    def test2_bin_creation(self):
        ''' Tests whether the object instantiation was successful
            by checking the number of Bin objects in the bins variable '''
            
        self.assertEqual(len(self.wh1.bins), 38)

    def test3_outcomecollection(self):
        ''' Generates all the Bins with their corresponding Outcomes,
            then tests the all_outcomes list with the Wheel.getOutcome method '''
            
        self.bb.buildBins(self.wh1)

        self.assertEqual(self.wh1.getOutcome('00'), set(['Number 00 (odds 35:1)',
                                                         'Line 0-00-1-2-3 (odds 5:1)']))

        self.assertEqual(self.wh1.getOutcome('10'), set(['Number 10 (odds 35:1)',
                                                         'Split 7-10 (odds 17:1)',
                                                         'Split 10-11 (odds 17:1)',
                                                         'Split 10-13 (odds 17:1)',
                                                         'Street 10-11-12 (odds 11:1)',
                                                         'Corner 7-8-10-11 (odds 11:1)',
                                                         'Corner 10-11-13-14 (odds 11:1)',
                                                         'Line 7-8-9-10-11-12 (odds 5:1)',
                                                         'Line 10-11-12-13-14-15 (odds 5:1)']))

        self.assertEqual(self.wh1.getOutcome('Red'), set(['Red (odds 1:1)']))

    def test4_next(self):
        ''' Picks a rendom element from the bins and checks if it is a valid choice
            and checks the return type'''

        roll = self.wh1.next_roll()
        self.assertTrue(roll in self.wh1.bins)
        self.assertTrue(type(roll) == Bin)

    def test5_nonrandom_next(self):
        ''' Tests with a controlled roll if the right Bin was chosen '''
        
        roll = self.wh1.next_roll()
        self.assertEqual(roll, self.wh1.bins[0])

    def test6_binIterator(self):

        wh = Wheel()
        bb = BinBuilder()
        bb.buildBins(wh)
        for oc in wh.binIterator():
            print(oc)

        
if __name__ == '__main__':
    unittest.main()
