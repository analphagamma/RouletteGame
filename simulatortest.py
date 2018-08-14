import unittest
from roulette import *
from wheeltest import NonRandom

class SimulatorTest(unittest.TestCase):
     
    def test1_session(self):
        ''' Tests if the Simulatosession() returns the required
            list of stakes in a controlled simulation. '''

        nrnd = NonRandom(1)
        wh = Wheel(nrnd)
        bb = BinBuilder()
        bb.buildBins(wh)
        t = Table(100)
        game = RouletteGame(wh, t)        
        pl = Passenger57(t)
        sim = Simulator(pl, game)
        
        self.assertEqual(sim.session(),
                         [90,80,70,60,50,40,30,20,10,0])
    
    def test2_gather(self):
        ''' Tests the Simulatogather() method. '''
        
        wh = Wheel()
        bb = BinBuilder()
        bb.buildBins(wh)
        t = Table(100)
        game = RouletteGame(wh, t)        
        pl = Passenger57(t)

        sim = Simulator(pl, game)
        #print(sim.gather())
        

if __name__ == '__main__':
    unittest.main()
