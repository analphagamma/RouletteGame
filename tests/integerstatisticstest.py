import unittest
from context import integerstatistics as IS

class IntegerStatisticsTest(unittest.TestCase):

    test_data = [9,8,5,9,9,4,5,8,10,7,8,8]

    def test1_mean(self):
        self.assertEqual(IS.IntegerStatistics.mean(self.test_data),
                         7.5)

    def test2_mean(self):
        self.assertEqual(IS.IntegerStatistics.stdev(self.test_data),
                         1.88294)

if __name__ == '__main__':
    unittest.main()
