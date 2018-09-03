import unittest
from context import wheel, binbuilder, table, roulettegame, players, simulator
from wheeltest import NonRandom

class SimulatorTest(unittest.TestCase):
     
    def test1_session(self):
        ''' Tests if the simulator.Simulatosession() returns the required
            list of stakes in a controlled simulation. '''

        nrnd = NonRandom(1)
        wh = wheel.Wheel(nrnd)
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)
        sim = simulator.Simulator(pl, game)
        
        self.assertEqual(sim.session(),
                         [90,80,70,60,50,40,30,20,10,0])
    
    def test2_gather(self):
        ''' Tests the simulator.Simulatogather() method. '''
        
        wh = wheel.Wheel()
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)

        sim = simulator.Simulator(pl, game)
        #print(sim.gather())
        

if __name__ == '__main__':
    unittest.main()
