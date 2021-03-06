import unittest, random
from context import table, players, outcome

class NonRandom(random.Random):
    ''' A Non-random generator for testing purposes '''

    def __init__(self, value):
        self.value = value

    def setSeed(self, value):
        return value

    def randint(self, a):
        return self.value

class RandomPlayerTest(unittest.TestCase):

    #setting up non random generator
    nrnd = NonRandom(0) # always picks the first Outcome in the set
    t = table.Table(1000)
    pl = players.RandomPlayer(t, nrnd)

    def test1_nonrandomchoice(self):
        for i, oc in enumerate(self.pl.all_OC):
            if i == self.nrnd.randint(len(self.pl.all_OC)):
                self.assertEqual(oc, outcome.Outcome('Number 1', 35))
                break

if __name__ == '__main__':
    unittest.main()
