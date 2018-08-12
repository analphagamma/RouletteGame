import unittest
from roulette import *


class BinBuilderTest(unittest.TestCase):
    ''' Tests all the different kinds of bets whether they return
        the correct Outcome object '''
        
    wh = Wheel()
    bb = BinBuilder()

    def test_straightbets(self):
        ''' Tests straight, single number bet
            Checks the 2 wildcard numbers (0,00)
            and a regular number '''
        self.assertEqual(self.bb.generateStraightBets('0'),
                         Outcome('Number 0', 35))
        self.assertEqual(self.bb.generateStraightBets('00'),
                         Outcome('Number 00', 35))
        self.assertEqual(self.bb.generateStraightBets('1'),
                         Outcome('Number 1', 35))

    def test_splitbets(self):
        ''' Tests split bets: bets on 2 numbers
            Checks the 2 wildcard numbers (0,00)
            each number from the top row
            each number from the bottom row
            each number from a row in the middle'''
        self.assertEqual(self.bb.generateSplitBets('1'),
                         (Outcome('Split 1-2', 17),
                          Outcome('Split 1-4', 17)))
        self.assertEqual(self.bb.generateSplitBets('2'),
                         (Outcome('Split 1-2', 17),
                          Outcome('Split 2-3', 17),
                          Outcome('Split 2-5', 17)))
        self.assertEqual(self.bb.generateSplitBets('3'),
                         (Outcome('Split 2-3', 17),
                          Outcome('Split 3-6', 17)))
        self.assertEqual(self.bb.generateSplitBets('4'),
                         (Outcome('Split 1-4', 17),
                          Outcome('Split 4-5', 17),
                          Outcome('Split 4-7', 17)))
        self.assertEqual(self.bb.generateSplitBets('5'),
                         (Outcome('Split 2-5', 17),
                          Outcome('Split 4-5', 17),
                          Outcome('Split 5-6', 17),
                          Outcome('Split 5-8', 17)))
        self.assertEqual(self.bb.generateSplitBets('6'),
                         (Outcome('Split 3-6', 17),
                          Outcome('Split 5-6', 17),
                          Outcome('Split 6-9', 17)))
        self.assertEqual(self.bb.generateSplitBets('34'),
                         (Outcome('Split 31-34', 17),
                          Outcome('Split 34-35', 17)))
        self.assertEqual(self.bb.generateSplitBets('35'),
                         (Outcome('Split 32-35', 17),
                          Outcome('Split 34-35', 17),
                          Outcome('Split 35-36', 17)))
        self.assertEqual(self.bb.generateSplitBets('36'),
                         (Outcome('Split 33-36', 17),
                          Outcome('Split 35-36', 17)))
        
    def test_streetbets(self):
        ''' Tests street bets: a series of three numbers
            Checks 3 numbers: one from each column '''
        self.assertEqual(self.bb.generateStreetBets('1'),
                         Outcome('Street 1-2-3', 11))
        self.assertEqual(self.bb.generateStreetBets('14'),
                         Outcome('Street 13-14-15', 11))
        self.assertEqual(self.bb.generateStreetBets('24'),
                         Outcome('Street 22-23-24', 11))

    def test_cornerbets(self):
        ''' Tests corner bets: 4 numbers in a shape of a square
            It checks the top row (1,2,3)
            the bottom row (34,35,36)
            and one of the middle rows '''
        self.assertEqual(self.bb.generateCornerBets('1'),
                         Outcome('Corner 1-2-4-5', 8))
        self.assertEqual(self.bb.generateCornerBets('2'),
                         (Outcome('Corner 1-2-4-5', 8),
                          Outcome('Corner 2-3-5-6', 8)))
        self.assertEqual(self.bb.generateCornerBets('3'),
                         Outcome('Corner 2-3-5-6', 8))
        self.assertEqual(self.bb.generateCornerBets('34'),
                         Outcome('Corner 31-32-34-35', 8))
        self.assertEqual(self.bb.generateCornerBets('35'),
                         (Outcome('Corner 31-32-34-35', 8),
                          Outcome('Corner 32-33-35-36', 8)))
        self.assertEqual(self.bb.generateCornerBets('36'),
                         Outcome('Corner 32-33-35-36', 8))
        self.assertEqual(self.bb.generateCornerBets('10'),
                         (Outcome('Corner 7-8-10-11', 8),
                          Outcome('Corner 10-11-13-14', 8)))
        self.assertEqual(self.bb.generateCornerBets('20'),
                         (Outcome('Corner 16-17-19-20', 8),
                          Outcome('Corner 17-18-20-21', 8),
                          Outcome('Corner 19-20-22-23', 8),
                          Outcome('Corner 20-21-23-24', 8)))
        self.assertEqual(self.bb.generateCornerBets('18'),
                         (Outcome('Corner 14-15-17-18', 8),
                          Outcome('Corner 17-18-20-21', 8)))
        

    def test_linebets(self):
        ''' Tests line bets: a series of 6 numbers '''
        self.assertEqual(self.bb.generateLineBets('0'),
                         Outcome('Line 0-00-1-2-3', 5))
        self.assertEqual(self.bb.generateLineBets('00'),
                         Outcome('Line 0-00-1-2-3', 5))
        self.assertEqual(self.bb.generateLineBets('1'),
                         (Outcome('Line 0-00-1-2-3', 5),
                          Outcome('Line 1-2-3-4-5-6', 5)))
        self.assertEqual(self.bb.generateLineBets('15'),
                         (Outcome('Line 10-11-12-13-14-15', 5),
                          Outcome('Line 13-14-15-16-17-18', 5)))
        self.assertEqual(self.bb.generateLineBets('36'),
                         Outcome('Line 31-32-33-34-35-36', 5))
        
    def test_dozenbets(self):
        ''' Tests dozen bets and if the right group is chosen
            checks one number from each dozen group '''
        self.assertEqual(self.bb.generateDozenBets('4'),
                         Outcome('Dozen 1', 2))
        self.assertEqual(self.bb.generateDozenBets('20'),
                         Outcome('Dozen 2', 2))
        self.assertEqual(self.bb.generateDozenBets('30'),
                         Outcome('Dozen 3', 2))

    def test_redblackbets(self):
        ''' Tests RedBlack bets '''
        self.assertEqual(self.bb.generateRedBlackBets('1'),
                         Outcome('Red', 1))
        self.assertEqual(self.bb.generateRedBlackBets('2'),
                         Outcome('Black', 1))
                         
    def test_evenoddbets(self):
        ''' Tests EvenOdd bets and checks if even numbers go in Even
            and odd numbers go in Odd '''
        self.assertEqual(self.bb.generateEvenOddBets('1'),
                         Outcome('Odd', 1))
        self.assertEqual(self.bb.generateEvenOddBets('2'),
                         Outcome('Even', 1))

    def test_highlowbets(self):
        ''' Tests HighLow bets and checks if numbers go in the correct container '''
        self.assertEqual(self.bb.generateHighLowBets('18'),
                         Outcome('Low', 1))
        self.assertEqual(self.bb.generateHighLowBets('19'),
                         Outcome('High', 1))

    def test_columnbet(self):
        ''' Tests column bets and if the right column is chosen
            Checks one number from each column '''
        self.assertEqual(self.bb.generateColumnBets('13'),
                         Outcome('Column 1', 2))
        self.assertEqual(self.bb.generateColumnBets('23'),
                         Outcome('Column 2', 2))
        self.assertEqual(self.bb.generateColumnBets('27'),
                         Outcome('Column 3', 2))

    def test_buildbins(self):
        self.bb.buildBins(self.wh)
        # case 0
        #print(self.wh.get_bin(0))
        self.assertEqual(self.wh.get_bin(0),
                         Bin(Outcome('Number 0', 35),
                               Outcome('Line 0-00-1-2-3', 5),
                               Outcome('Even', 1),
                               Outcome('Odd', 1)))
        # case 00
        self.assertEqual(self.wh.get_bin(37),
                         Bin(Outcome('Number 00', 35),
                               Outcome('Line 0-00-1-2-3', 5),
                               Outcome('Even', 1),
                               Outcome('Odd', 1)))
        
        # case 1
        self.assertEqual(self.wh.get_bin(1),
                         Bin(Outcome('Number 1', 35),
                               Outcome('Split 1-2', 17),
                               Outcome('Split 1-4', 17),
                               Outcome('Street 1-2-3', 11),
                               Outcome('Corner 1-2-4-5', 11),
                               Outcome('Line 0-00-1-2-3', 5),
                               Outcome('Line 1-2-3-4-5-6', 5),
                               Outcome('Dozen 1', 2),
                               Outcome('Column 1', 2),
                               Outcome('Red', 1),
                               Outcome('Odd', 1),
                               Outcome('Low', 1)))
        # case 2
        self.assertEqual(self.wh.get_bin(2),
                         Bin(Outcome('Number 2', 35),
                               Outcome('Split 1-2', 17),
                               Outcome('Split 2-3', 17),
                               Outcome('Split 2-5', 17),
                               Outcome('Street 1-2-3', 11),
                               Outcome('Corner 1-2-4-5', 11),
                               Outcome('Corner 2-3-5-6', 11),
                               Outcome('Line 0-00-1-2-3', 5),
                               Outcome('Line 1-2-3-4-5-6', 5),
                               Outcome('Dozen 1', 2),
                               Outcome('Column 2', 2),
                               Outcome('Black', 1),
                               Outcome('Even', 1),
                               Outcome('Low', 1)))
        # case 3
        self.assertEqual(self.wh.get_bin(3),
                         Bin(Outcome('Number 3', 35),
                               Outcome('Split 2-3', 17),
                               Outcome('Split 3-6', 17),
                               Outcome('Street 1-2-3', 11),
                               Outcome('Corner 2-3-5-6', 11),
                               Outcome('Line 0-00-1-2-3', 5),
                               Outcome('Line 1-2-3-4-5-6', 5),
                               Outcome('Dozen 1', 2),
                               Outcome('Column 3', 2),
                               Outcome('Red', 1),
                               Outcome('Odd', 1),
                               Outcome('Low', 1)))
        # case 10
        self.assertEqual(self.wh.get_bin(10),
                         Bin(Outcome('Number 10', 35),
                               Outcome('Split 7-10', 17),
                               Outcome('Split 10-11', 17),
                               Outcome('Split 10-13', 17),
                               Outcome('Street 10-11-12', 11),
                               Outcome('Corner 7-8-10-11', 11),
                               Outcome('Corner 10-11-13-14', 11),
                               Outcome('Line 7-8-9-10-11-12', 5),
                               Outcome('Line 10-11-12-13-14-15', 5),
                               Outcome('Dozen 1', 2),
                               Outcome('Column 1', 2),
                               Outcome('Black', 1),
                               Outcome('Even', 1),
                               Outcome('Low', 1)))
        # case 20
        self.assertEqual(self.wh.get_bin(20),
                         Bin(Outcome('Number 20', 35),
                               Outcome('Split 17-20', 17),
                               Outcome('Split 19-20', 17),
                               Outcome('Split 20-21', 17),
                               Outcome('Split 20-23', 17),
                               Outcome('Street 19-20-21', 11),
                               Outcome('Corner 16-17-19-20', 11),
                               Outcome('Corner 17-18-20-21', 11),
                               Outcome('Corner 19-20-22-23', 11),
                               Outcome('Corner 20-21-23-24', 11),
                               Outcome('Line 16-17-18-19-20-21', 5),
                               Outcome('Line 19-20-21-22-23-24', 5),
                               Outcome('Dozen 2', 2),
                               Outcome('Column 2', 2),
                               Outcome('Black', 1),
                               Outcome('Even', 1),
                               Outcome('High', 1)))
        # case 30
        self.assertEqual(self.wh.get_bin(30),
                         Bin(Outcome('Number 30', 35),
                               Outcome('Split 27-30', 17),
                               Outcome('Split 29-30', 17),
                               Outcome('Split 30-33', 17),
                               Outcome('Street 28-29-30', 11),
                               Outcome('Corner 26-27-29-30', 11),
                               Outcome('Corner 29-30-32-33', 11),
                               Outcome('Line 25-26-27-28-29-30', 5),
                               Outcome('Line 28-29-30-31-32-33', 5),
                               Outcome('Dozen 3', 2),
                               Outcome('Column 3', 2),
                               Outcome('Red', 1),
                               Outcome('Even', 1),
                               Outcome('High', 1)))
        # case 34
        self.assertEqual(self.wh.get_bin(34),
                         Bin(Outcome('Number 34', 35),
                               Outcome('Split 31-34', 17),
                               Outcome('Split 34-35', 17),
                               Outcome('Street 34-35-36', 11),
                               Outcome('Corner 31-32-34-35', 11),
                               Outcome('Line 31-32-33-34-35-36', 5),
                               Outcome('Dozen 3', 2),
                               Outcome('Column 1', 2),
                               Outcome('Red', 1),
                               Outcome('Even', 1),
                               Outcome('High', 1)))
        # case 35
        self.assertEqual(self.wh.get_bin(35),
                         Bin(Outcome('Number 35', 35),
                               Outcome('Split 32-35', 17),
                               Outcome('Split 34-35', 17),
                               Outcome('Split 35-36', 17),
                               Outcome('Street 34-35-36', 11),
                               Outcome('Corner 31-32-34-35', 11),
                               Outcome('Corner 32-33-35-36', 11),
                               Outcome('Line 31-32-33-34-35-36', 5),
                               Outcome('Dozen 3', 2),
                               Outcome('Column 2', 2),
                               Outcome('Black', 1),
                               Outcome('Odd', 1),
                               Outcome('High', 1)))
        # case 36
        self.assertEqual(self.wh.get_bin(36),
                         Bin(Outcome('Number 36', 35),
                               Outcome('Split 33-36', 17),
                               Outcome('Split 35-36', 17),
                               Outcome('Street 34-35-36', 11),
                               Outcome('Corner 32-33-35-36', 11),
                               Outcome('Line 31-32-33-34-35-36', 5),
                               Outcome('Dozen 3', 2),
                               Outcome('Column 3', 2),
                               Outcome('Red', 1),
                               Outcome('Even', 1),
                               Outcome('High', 1)))
        
        
if __name__ == '__main__':
    unittest.main()
