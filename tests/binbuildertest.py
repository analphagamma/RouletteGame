import unittest
from context import binbuilder, wheel, outcome, bin


class BinBuilderTest(unittest.TestCase):
    ''' Tests all the different kinds of bets whether they return
        the correct Outcome object '''
        
    wh = wheel.Wheel()
    bb = binbuilder.BinBuilder()

    def test_straightbets(self):
        ''' Tests straight, single number bet
            Checks the 2 wildcard numbers (0,00)
            and a regular number '''
        self.assertEqual(self.bb.generateStraightBets('0'),
                         outcome.Outcome('Number 0', 35))
        self.assertEqual(self.bb.generateStraightBets('00'),
                         outcome.Outcome('Number 00', 35))
        self.assertEqual(self.bb.generateStraightBets('1'),
                         outcome.Outcome('Number 1', 35))

    def test_splitbets(self):
        ''' Tests split bets: bets on 2 numbers
            Checks the 2 wildcard numbers (0,00)
            each number from the top row
            each number from the bottom row
            each number from a row in the middle'''
        self.assertEqual(self.bb.generateSplitBets('1'),
                         (outcome.Outcome('Split 1-2', 17),
                          outcome.Outcome('Split 1-4', 17)))
        self.assertEqual(self.bb.generateSplitBets('2'),
                         (outcome.Outcome('Split 1-2', 17),
                          outcome.Outcome('Split 2-3', 17),
                          outcome.Outcome('Split 2-5', 17)))
        self.assertEqual(self.bb.generateSplitBets('3'),
                         (outcome.Outcome('Split 2-3', 17),
                          outcome.Outcome('Split 3-6', 17)))
        self.assertEqual(self.bb.generateSplitBets('4'),
                         (outcome.Outcome('Split 1-4', 17),
                          outcome.Outcome('Split 4-5', 17),
                          outcome.Outcome('Split 4-7', 17)))
        self.assertEqual(self.bb.generateSplitBets('5'),
                         (outcome.Outcome('Split 2-5', 17),
                          outcome.Outcome('Split 4-5', 17),
                          outcome.Outcome('Split 5-6', 17),
                          outcome.Outcome('Split 5-8', 17)))
        self.assertEqual(self.bb.generateSplitBets('6'),
                         (outcome.Outcome('Split 3-6', 17),
                          outcome.Outcome('Split 5-6', 17),
                          outcome.Outcome('Split 6-9', 17)))
        self.assertEqual(self.bb.generateSplitBets('34'),
                         (outcome.Outcome('Split 31-34', 17),
                          outcome.Outcome('Split 34-35', 17)))
        self.assertEqual(self.bb.generateSplitBets('35'),
                         (outcome.Outcome('Split 32-35', 17),
                          outcome.Outcome('Split 34-35', 17),
                          outcome.Outcome('Split 35-36', 17)))
        self.assertEqual(self.bb.generateSplitBets('36'),
                         (outcome.Outcome('Split 33-36', 17),
                          outcome.Outcome('Split 35-36', 17)))
        
    def test_streetbets(self):
        ''' Tests street bets: a series of three numbers
            Checks 3 numbers: one from each column '''
        self.assertEqual(self.bb.generateStreetBets('1'),
                         outcome.Outcome('Street 1-2-3', 11))
        self.assertEqual(self.bb.generateStreetBets('14'),
                         outcome.Outcome('Street 13-14-15', 11))
        self.assertEqual(self.bb.generateStreetBets('24'),
                         outcome.Outcome('Street 22-23-24', 11))

    def test_cornerbets(self):
        ''' Tests corner bets: 4 numbers in a shape of a square
            It checks the top row (1,2,3)
            the bottom row (34,35,36)
            and one of the middle rows '''
        self.assertEqual(self.bb.generateCornerBets('1'),
                         outcome.Outcome('Corner 1-2-4-5', 8))
        self.assertEqual(self.bb.generateCornerBets('2'),
                         (outcome.Outcome('Corner 1-2-4-5', 8),
                          outcome.Outcome('Corner 2-3-5-6', 8)))
        self.assertEqual(self.bb.generateCornerBets('3'),
                         outcome.Outcome('Corner 2-3-5-6', 8))
        self.assertEqual(self.bb.generateCornerBets('34'),
                         outcome.Outcome('Corner 31-32-34-35', 8))
        self.assertEqual(self.bb.generateCornerBets('35'),
                         (outcome.Outcome('Corner 31-32-34-35', 8),
                          outcome.Outcome('Corner 32-33-35-36', 8)))
        self.assertEqual(self.bb.generateCornerBets('36'),
                         outcome.Outcome('Corner 32-33-35-36', 8))
        self.assertEqual(self.bb.generateCornerBets('10'),
                         (outcome.Outcome('Corner 7-8-10-11', 8),
                          outcome.Outcome('Corner 10-11-13-14', 8)))
        self.assertEqual(self.bb.generateCornerBets('20'),
                         (outcome.Outcome('Corner 16-17-19-20', 8),
                          outcome.Outcome('Corner 17-18-20-21', 8),
                          outcome.Outcome('Corner 19-20-22-23', 8),
                          outcome.Outcome('Corner 20-21-23-24', 8)))
        self.assertEqual(self.bb.generateCornerBets('18'),
                         (outcome.Outcome('Corner 14-15-17-18', 8),
                          outcome.Outcome('Corner 17-18-20-21', 8)))
        

    def test_linebets(self):
        ''' Tests line bets: a series of 6 numbers '''
        self.assertEqual(self.bb.generateLineBets('0'),
                         outcome.Outcome('Line 0-00-1-2-3', 5))
        self.assertEqual(self.bb.generateLineBets('00'),
                         outcome.Outcome('Line 0-00-1-2-3', 5))
        self.assertEqual(self.bb.generateLineBets('1'),
                         (outcome.Outcome('Line 0-00-1-2-3', 5),
                          outcome.Outcome('Line 1-2-3-4-5-6', 5)))
        self.assertEqual(self.bb.generateLineBets('15'),
                         (outcome.Outcome('Line 10-11-12-13-14-15', 5),
                          outcome.Outcome('Line 13-14-15-16-17-18', 5)))
        self.assertEqual(self.bb.generateLineBets('36'),
                         outcome.Outcome('Line 31-32-33-34-35-36', 5))
        
    def test_dozenbets(self):
        ''' Tests dozen bets and if the right group is chosen
            checks one number from each dozen group '''
        self.assertEqual(self.bb.generateDozenBets('4'),
                         outcome.Outcome('Dozen 1', 2))
        self.assertEqual(self.bb.generateDozenBets('20'),
                         outcome.Outcome('Dozen 2', 2))
        self.assertEqual(self.bb.generateDozenBets('30'),
                         outcome.Outcome('Dozen 3', 2))

    def test_redblackbets(self):
        ''' Tests RedBlack bets '''
        self.assertEqual(self.bb.generateRedBlackBets('1'),
                         outcome.Outcome('Red', 1))
        self.assertEqual(self.bb.generateRedBlackBets('2'),
                         outcome.Outcome('Black', 1))
                         
    def test_evenoddbets(self):
        ''' Tests EvenOdd bets and checks if even numbers go in Even
            and odd numbers go in Odd '''
        self.assertEqual(self.bb.generateEvenOddBets('1'),
                         outcome.Outcome('Odd', 1))
        self.assertEqual(self.bb.generateEvenOddBets('2'),
                         outcome.Outcome('Even', 1))

    def test_highlowbets(self):
        ''' Tests HighLow bets and checks if numbers go in the correct container '''
        self.assertEqual(self.bb.generateHighLowBets('18'),
                         outcome.Outcome('Low', 1))
        self.assertEqual(self.bb.generateHighLowBets('19'),
                         outcome.Outcome('High', 1))

    def test_columnbet(self):
        ''' Tests column bets and if the right column is chosen
            Checks one number from each column '''
        self.assertEqual(self.bb.generateColumnBets('13'),
                         outcome.Outcome('Column 1', 2))
        self.assertEqual(self.bb.generateColumnBets('23'),
                         outcome.Outcome('Column 2', 2))
        self.assertEqual(self.bb.generateColumnBets('27'),
                         outcome.Outcome('Column 3', 2))

    def test_buildbins(self):
        self.bb.buildBins(self.wh)
        # case 0
        self.assertEqual(self.wh.get_bin(0),
                         bin.Bin(outcome.Outcome('Number 0', 35),
                             outcome.Outcome('Line 0-00-1-2-3', 5),
                             outcome.Outcome('Even', 1),
                             outcome.Outcome('Odd', 1)))
        # case 00
        self.assertEqual(self.wh.get_bin(37),
                         bin.Bin(outcome.Outcome('Number 00', 35),
                             outcome.Outcome('Line 0-00-1-2-3', 5),
                             outcome.Outcome('Even', 1),
                             outcome.Outcome('Odd', 1)))
        
        # case 1
        self.assertEqual(self.wh.get_bin(1),
                         bin.Bin(outcome.Outcome('Number 1', 35),
                             outcome.Outcome('Split 1-2', 17),
                             outcome.Outcome('Split 1-4', 17),
                             outcome.Outcome('Street 1-2-3', 11),
                             outcome.Outcome('Corner 1-2-4-5', 11),
                             outcome.Outcome('Line 0-00-1-2-3', 5),
                             outcome.Outcome('Line 1-2-3-4-5-6', 5),
                             outcome.Outcome('Dozen 1', 2),
                             outcome.Outcome('Column 1', 2),
                             outcome.Outcome('Red', 1),
                             outcome.Outcome('Odd', 1),
                             outcome.Outcome('Low', 1)))
        # case 2
        self.assertEqual(self.wh.get_bin(2),
                         bin.Bin(outcome.Outcome('Number 2', 35),
                             outcome.Outcome('Split 1-2', 17),
                             outcome.Outcome('Split 2-3', 17),
                             outcome.Outcome('Split 2-5', 17),
                             outcome.Outcome('Street 1-2-3', 11),
                             outcome.Outcome('Corner 1-2-4-5', 11),
                             outcome.Outcome('Corner 2-3-5-6', 11),
                             outcome.Outcome('Line 0-00-1-2-3', 5),
                             outcome.Outcome('Line 1-2-3-4-5-6', 5),
                             outcome.Outcome('Dozen 1', 2),
                             outcome.Outcome('Column 2', 2),
                             outcome.Outcome('Black', 1),
                             outcome.Outcome('Even', 1),
                             outcome.Outcome('Low', 1)))
        # case 3
        self.assertEqual(self.wh.get_bin(3),
                         bin.Bin(outcome.Outcome('Number 3', 35),
                             outcome.Outcome('Split 2-3', 17),
                             outcome.Outcome('Split 3-6', 17),
                             outcome.Outcome('Street 1-2-3', 11),
                             outcome.Outcome('Corner 2-3-5-6', 11),
                             outcome.Outcome('Line 0-00-1-2-3', 5),
                             outcome.Outcome('Line 1-2-3-4-5-6', 5),
                             outcome.Outcome('Dozen 1', 2),
                             outcome.Outcome('Column 3', 2),
                             outcome.Outcome('Red', 1),
                             outcome.Outcome('Odd', 1),
                             outcome.Outcome('Low', 1)))
        # case 10
        self.assertEqual(self.wh.get_bin(10),
                         bin.Bin(outcome.Outcome('Number 10', 35),
                               outcome.Outcome('Split 7-10', 17),
                               outcome.Outcome('Split 10-11', 17),
                               outcome.Outcome('Split 10-13', 17),
                               outcome.Outcome('Street 10-11-12', 11),
                               outcome.Outcome('Corner 7-8-10-11', 11),
                               outcome.Outcome('Corner 10-11-13-14', 11),
                               outcome.Outcome('Line 7-8-9-10-11-12', 5),
                               outcome.Outcome('Line 10-11-12-13-14-15', 5),
                               outcome.Outcome('Dozen 1', 2),
                               outcome.Outcome('Column 1', 2),
                               outcome.Outcome('Black', 1),
                               outcome.Outcome('Even', 1),
                               outcome.Outcome('Low', 1)))
        # case 20
        self.assertEqual(self.wh.get_bin(20),
                         bin.Bin(outcome.Outcome('Number 20', 35),
                               outcome.Outcome('Split 17-20', 17),
                               outcome.Outcome('Split 19-20', 17),
                               outcome.Outcome('Split 20-21', 17),
                               outcome.Outcome('Split 20-23', 17),
                               outcome.Outcome('Street 19-20-21', 11),
                               outcome.Outcome('Corner 16-17-19-20', 11),
                               outcome.Outcome('Corner 17-18-20-21', 11),
                               outcome.Outcome('Corner 19-20-22-23', 11),
                               outcome.Outcome('Corner 20-21-23-24', 11),
                               outcome.Outcome('Line 16-17-18-19-20-21', 5),
                               outcome.Outcome('Line 19-20-21-22-23-24', 5),
                               outcome.Outcome('Dozen 2', 2),
                               outcome.Outcome('Column 2', 2),
                               outcome.Outcome('Black', 1),
                               outcome.Outcome('Even', 1),
                               outcome.Outcome('High', 1)))
        # case 30
        self.assertEqual(self.wh.get_bin(30),
                         bin.Bin(outcome.Outcome('Number 30', 35),
                               outcome.Outcome('Split 27-30', 17),
                               outcome.Outcome('Split 29-30', 17),
                               outcome.Outcome('Split 30-33', 17),
                               outcome.Outcome('Street 28-29-30', 11),
                               outcome.Outcome('Corner 26-27-29-30', 11),
                               outcome.Outcome('Corner 29-30-32-33', 11),
                               outcome.Outcome('Line 25-26-27-28-29-30', 5),
                               outcome.Outcome('Line 28-29-30-31-32-33', 5),
                               outcome.Outcome('Dozen 3', 2),
                               outcome.Outcome('Column 3', 2),
                               outcome.Outcome('Red', 1),
                               outcome.Outcome('Even', 1),
                               outcome.Outcome('High', 1)))
        # case 34
        self.assertEqual(self.wh.get_bin(34),
                         bin.Bin(outcome.Outcome('Number 34', 35),
                               outcome.Outcome('Split 31-34', 17),
                               outcome.Outcome('Split 34-35', 17),
                               outcome.Outcome('Street 34-35-36', 11),
                               outcome.Outcome('Corner 31-32-34-35', 11),
                               outcome.Outcome('Line 31-32-33-34-35-36', 5),
                               outcome.Outcome('Dozen 3', 2),
                               outcome.Outcome('Column 1', 2),
                               outcome.Outcome('Red', 1),
                               outcome.Outcome('Even', 1),
                               outcome.Outcome('High', 1)))
        # case 35
        self.assertEqual(self.wh.get_bin(35),
                         bin.Bin(outcome.Outcome('Number 35', 35),
                               outcome.Outcome('Split 32-35', 17),
                               outcome.Outcome('Split 34-35', 17),
                               outcome.Outcome('Split 35-36', 17),
                               outcome.Outcome('Street 34-35-36', 11),
                               outcome.Outcome('Corner 31-32-34-35', 11),
                               outcome.Outcome('Corner 32-33-35-36', 11),
                               outcome.Outcome('Line 31-32-33-34-35-36', 5),
                               outcome.Outcome('Dozen 3', 2),
                               outcome.Outcome('Column 2', 2),
                               outcome.Outcome('Black', 1),
                               outcome.Outcome('Odd', 1),
                               outcome.Outcome('High', 1)))
        # case 36
        self.assertEqual(self.wh.get_bin(36),
                         bin.Bin(outcome.Outcome('Number 36', 35),
                               outcome.Outcome('Split 33-36', 17),
                               outcome.Outcome('Split 35-36', 17),
                               outcome.Outcome('Street 34-35-36', 11),
                               outcome.Outcome('Corner 32-33-35-36', 11),
                               outcome.Outcome('Line 31-32-33-34-35-36', 5),
                               outcome.Outcome('Dozen 3', 2),
                               outcome.Outcome('Column 3', 2),
                               outcome.Outcome('Red', 1),
                               outcome.Outcome('Even', 1),
                               outcome.Outcome('High', 1)))
        
        
if __name__ == '__main__':
    unittest.main()
